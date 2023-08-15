from fuzzywuzzy import fuzz

questions = {"How do you get a schedule change": "Go to the amador valley counseling website and then you can request a schedule change.", 
        "How to access access": "Go to flexisched, and you can change your access teacher that way",
        "Where can I find the list of classes that I can take": "You can find that on the counseling department website: https://sites.google.com/pleasantonusd.net/amadorhighschoolcounseling/academic-planning?authuser=0",
        "What are the required credits you need for graduation": "You can find the link here: https://docs.google.com/document/d/12QCY1r2GNhbyZ3QtIP9eP1Ljam4XiVw8D68ItOZlf7Q/edit",
        "How do I know if a specific volunteer location is valid with PUSD": "All the registered organizations are listed on this document: https://docs.google.com/document/d/1wvrMqZwB4R3azA-FFGXDXcOsHSigQFJw9312pvYeTro/edit",
        "Where can I check my grades?": "You can check your grades at the new student portal: https://pleasantvue.com/",
        "Does the school offer a student drivers ed": "Yes: https://www.pleasantondriversed.com/",
        "Where can I find the clubs at our school?": "Here is a list of all the clubs at our school: https://sites.google.com/site/avstudentweb/clubs"}

questions_list = list(questions.keys())

def check_related_questions(question, limit):
    curr = 0
    number = -1
    for i in range(len(questions_list)):
        if (int(fuzz.ratio(question.lower(), questions_list[i].lower())) >= curr):
            number = i
            curr = int(fuzz.ratio(question.lower(), questions_list[i].lower()))

    if curr >= limit:
        print("The closest question that we could find was:", questions_list[number])
        print("The answer to your question is:", questions[questions_list[number]])
    else:
        print("Sorry, I'm not sure.")




print("Hello! Welcome to the Amador Chat Bot!")
while True:
    query = input("What is the question that you have? Type pass or exit if you want to quit. ")
    if (query == "pass" or query == "exit"):
        break
    check_related_questions(query, 40)

        