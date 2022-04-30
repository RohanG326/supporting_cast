from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json
import random as rand


create_tk = Blueprint('createtask', __name__,
                      url_prefix='/ct/',
                      template_folder='templates',
                      static_folder='static', static_url_path='static/createtask')

darkmode="darkmode"


class Trivia:
    def __init__(self, question, answer, value):
        self.question = question
        self.answer = answer
        self.value = value

    def checkanswer(self, guess):
        if guess == self.answer:
            return True
        else:
            return False


score1 = 0
display = ""
state = True
question1 = Trivia("Who won the world series in 1988 ", "Dodgers", 1)
question2 = Trivia("Who won superbowl 50 ", "Broncos", 1)
question3 = Trivia("Who won the F1 constructors championship in 2021 ", "Max Verstappen", 1)
question4 = Trivia("Which player has the most Superbowl wins in NFL History", "Tom Brady", 1)
question5 = Trivia("What is the square root of 49 ", "7", 1)
question6 = Trivia("What's the capital of Chile ", "Santiago", 1)
question7 = Trivia("What is the capital of France ", "Paris", 1)
question8 = Trivia("Who is the current President of the USA ", "Joe Biden", 1)
question9 = Trivia("What does CRUD stand for ", "Create Read Update Delete", 1)
question10 = Trivia("What movie was the song \"Life is a Highway\" In ", "Cars", 1)
question11 = Trivia("What does OOP stand for", "Object Oriented Programming", 1)
question12 = Trivia("The olympics are held every how many years(enter answer as a word not number)", "Four", 1)
question13 = Trivia("In American Football, six points are scored for a what", "Touchdown", 1)
question14 = Trivia("Which tennis player has won more grandslams, Roger Federer or Andy Murray", "", 1)
question15 = Trivia("What does NFL stand for", "National Football League", 1)




questionList = [
    question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,
    question11,question12, question13, question14, question15
]


@create_tk.route('/createtask/', methods=['GET', 'POST'])
def createtask():
    global score1
    global display
    global state
    display = " "
    h = request.args.get('answer', '')
    userinput = request.form.get('userinput')

    if state:
        display = " "
    else:
        if userinput == h:
            score1 = score1 + 1
            print("it works")
            print(score1)
            display = "Correct!"
        else:
            # questionList.remove(random_value1)
            print("it doesnt work")
            display = "Incorrect, the correct answer was: " + h

    random_value1 = questionList[rand.randint(0, len(questionList) - 1)]
    state = False
    return render_template("createtask.html", randomvalue=random_value1, score1=score1, display=display)

@create_tk.route('/rcreatetask/', methods=['GET','POST'])
def rohancreatetask():
    return render_template("rohancreatetask.html")

if __name__ == "__main__":
    userquestions = input("How many questions do you want")
    for i in range(int(userquestions)):
        randomValue = questionList[rand.randint(0, len(questionList)-1)]
        guess = input(randomValue.question)
        if randomValue.checkanswer(guess):
            score = score + 1
            print("Correct!")
            print(f"Your score is {score}")
        else:
            print("Incorrect!")
            print("The correct answer was " + randomValue.answer)
        questionList.remove(randomValue)

