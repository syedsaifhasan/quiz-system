def main(cursor):
    print "HERE IS THE LIST OF QUIZZES YOU CAN ATTEMPT"
    print "PLEASE CHOOSE ANY OF THEM:"

    sql = "SELECT * from quiz_names"
    cursor.execute(sql)
    result = cursor.fetchall()

    count = 0
    for a, b in result:
        count+=1
        print count,". ",b

    user_option = raw_input("\n YOUR OPTION: ")
    user_option1 = int(user_option)

    user_option = result[user_option1 - 1][1]
    user_option_id = result[user_option1 - 1][0]
    user_option_id = str(user_option_id)

    print "_______________________"
    print user_option
    print "_______________________"

    sql = "SELECT * from questions WHERE quiz_id=%s"
    cursor.execute(sql, [user_option_id])
    result = cursor.fetchall()

    count = 0
    grading = []
    total_marks = len(result)

    print "TOTAL QUESTIONS: ", total_marks, "\n"
    for a,b,c,d,e in result:
        answer = None;
        count+=1
        print "Question ",count,": ", b
        if (d == 'TF'):
            print "Your options: "
            print "1. TRUE"
            print "2. FALSE"
        elif (d == "Numeric"):
            pass
        elif (d == "MCQ"):
            sql = "SELECT * from mcq_options WHERE question_id=%s"
            cursor.execute(sql, [str(a)])
            options = cursor.fetchall()
            print "Your options:"
            optioncount = 0
            for option, x in options:
                optioncount+=1
                print optioncount, ". ",option
        else:
            print "INVALID QUESTION TYPE!"
            break
        answer = raw_input("YOUR ANSWER: ")
        print "\n"
        if (answer != c):
            grading.append((count, c, answer))

    print "YOUR RESULTS:"
    for question_num, correct_answer, wrong_answer in grading:
        print "Your answer to question ",question_num, " is incorrect!"
        print "CORRECT ANSWER: ",correct_answer
        print "YOUR ANSWER: ", wrong_answer,"\n"

    print "YOUR SCORE: ", total_marks - len(grading), "/", total_marks

