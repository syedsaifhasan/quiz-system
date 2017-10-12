def main(cursor):
    print "____________________________________________________"
    print "QUIZ MAKER"
    print "____________________________________________________"
    nameofquiz = raw_input("Name of Quiz: ")
    sql = "INSERT INTO quiz_names(name) VALUES(%s)"
    cursor.execute(sql, [nameofquiz])
    last_quiz_entry = cursor.lastrowid
    print "Quiz id is ", last_quiz_entry
    count = 0
    options = []

    print "Lets start adding questions.\n"

    while(True):
        add = raw_input("Want to add a question?(Y\N)\n")
        if (add == "N"):
            print "Quiz made succesfully!"
            break

        count+=1
        print "QUESTION ", count
        question = raw_input("Write your question:\n")
        answer = raw_input("ENTER THE CORRECT ANSWER FOR THIS QUESTION: ")

        while True:
            typeofquestion = raw_input(
                "TYPE OF QUESTION(TF = True/False, MCQ = Multiple Choice Question, Numeric): ")

            if (typeofquestion == "TF"):
                break
            elif (typeofquestion == "MCQ"):
                print "ENTER FOUR OPTIONS FOR THIS QUESTION: \n"
                for i in range(1, 5):
                    print "OPTION ", i
                    if (options.append(raw_input())):
                        print "Option added successfully!\n"
                break
            elif (typeofquestion == "Numeric"):
                break
            else:
                print "Invalid choice"
                print "Please enter the correct choice!"


        sql = "INSERT INTO questions(question, answer, question_type, quiz_id) VALUES (%s, %s, %s, %s)"
        entry = (question, answer, typeofquestion, last_quiz_entry)
        if (cursor.execute(sql, entry)):
            print "QUESTION ADDED SUCCESSFULLY!"

        last_question_entry = cursor.lastrowid
        for option in options:
            sql = "INSERT INTO mcq_options(option_text, question_id) VALUES(%s,%s)"
            entry = (option, last_question_entry)
            cursor.execute(sql, entry)
