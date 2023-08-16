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
possible_queries = []

def check_related_questions(question, limit):
    for i in range(len(questions_list)):
        if (int(fuzz.ratio(question.lower(), questions_list[i].lower())) >= limit):
            if (int(fuzz.ratio(question.lower(), questions_list[i].lower())) >= 10):
                possible_queries.append(questions_list[i])
    if len(possible_queries) == 1:
        print("Here is the question that we found most closely related to your query:")
        print(possible_queries[0])
        print(questions[possible_queries[0]])
    elif len(possible_queries) > 0:
        print("Here are the possible questions we got based on the keyword. Please type which one you are interested in.")
        print("0. None of these")
        for j in range(len(possible_queries)):
            print(j+1,f". {possible_queries[j]}")
        x = int(input("Which query are you interested in? "))
        if x <= len(possible_queries) or x >= 0:
            if x == 0:
                print("Sorry, please try another input.")
            else:
                print(questions[possible_queries[x-1]])
    else:
        print("Sorry, please try another input.")
    
"""
    if curr >= limit:
        print("The closest question that we could find was:", questions_list[number])
        print("The answer to your question is:", questions[questions_list[number]])
    else:
        print("Sorry, I'm not sure.")
"""



print("Hello! Welcome to the Amador Chat Bot!")
while True:
    print("What is the question that you have?")
    print("Type \"pass\" or \"exit\" if you want to stop chatting!")
    query = input("Type your querry here: ")
    if (query == "pass" or query == "exit"):
        break
    check_related_questions(query, 30)

        