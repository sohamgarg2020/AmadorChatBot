from fuzzywuzzy import fuzz
import speech_recognition as sr
import pyttsx3

questions = {
    "How do you get a schedule change?": "Go to the amador valley counseling website and then you can request a schedule change.",
    "How to access access?": "Go to flexisched, and you can change your access teacher that way",
    "Where can I find the list of classes that I can take?": "You can find that on the counseling department website: https://sites.google.com/pleasantonusd.net/amadorhighschoolcounseling/academic-planning?authuser=0",
    "What are the required credits you need for graduation?": "You can find the link here: https://docs.google.com/document/d/12QCY1r2GNhbyZ3QtIP9eP1Ljam4XiVw8D68ItOZlf7Q/edit",
    "How do I know if a specific volunteer location is valid with PUSD?": "All the registered organizations are listed on this document: https://docs.google.com/document/d/1wvrMqZwB4R3azA-FFGXDXcOsHSigQFJw9312pvYeTro/edit",
    "Where can I check my grades?": "You can check your grades at the new student portal: https://pleasantvue.com/",
    "Does the school offer a student drivers ed?": "Yes: https://www.pleasantondriversed.com/",
    "Where can I find the clubs at our school?": "Here is a list of all the clubs at our school: https://sites.google.com/site/avstudentweb/clubs"
}

questions_list = list(questions.keys())

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()





def check_related_questions(question):
    possible_queries = []

    for q in questions_list:
        ratio = fuzz.ratio(question.lower(), q.lower())
        if ratio >= 50:
            print("Here is the question that we found most closely related to your query:")
            print(q)
            print(questions[q])
            return
        if ratio >= 25:
            possible_queries.append((q, ratio))

    possible_queries.sort(key=lambda x: x[1], reverse=True)

    if not possible_queries:
        print("Sorry, I'm not sure.")
    elif len(possible_queries) == 1:
        print("Here is the question that we found most closely related to your query:")
        print(possible_queries[0][0])
        print(questions[possible_queries[0][0]])
    else:
        print("Here are the possible questions we got based on the keyword. Please type which one you are interested in.")
        print("0. None of these.")
        count = 1
        for j in possible_queries:
            print(f"{count}. {j[0]}")
            count += 1
        x = input("Which query are you interested in? ")
        works = False
        while True:
            try:
                x = int(x)
                while True:
                    if x == 0:
                        return
                        works = True
                    if x >= 0 and x <= len(possible_queries):
                        print(questions[possible_queries[x - 1][0]])
                        works = True
                        break
                    else:
                        x = input("Sorry that isn't one of the options. Please try again. ")
                        break
            except:
                x = input("Sorry that isn't one of the options. Please try again. ")
            if works:
                break


def main():
    recognizer = sr.Recognizer()

    # Using the default system microphone as audio source
    with sr.Microphone(sample_rate=44100, chunk_size=512) as source2:
        print("Say something...")
        audio = recognizer.listen(source2)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Request error: {e}")

if __name__ == "__main__":
    main()

"""
print("Hello! Welcome to the Amador Chat Bot!")

while True:
    print("What is the question that you have?")
    print("Type \"exit\" if you want to stop chatting!")
    query = input("Type your query here: ").strip().lower()

    if query == "exit":
        break

    check_related_questions(query)
"""