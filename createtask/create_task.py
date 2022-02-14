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


score = 0
question1 = Trivia("Who won the world series in 1988 ", "Dodgers", 1)
question2 = Trivia("Who won superbowl 50 ", "Broncos", 1)
question3 = Trivia("Who won the F1 constructors championship in 2012 ", "Sebastian Vettel", 1)
question4 = Trivia("Which player the most Superbowl wins", "Tom Brady", 1)
question5 = Trivia("What is the square root of 49 ", "7", 1)
question6 = Trivia("Whats the capital of Chile ", "Santiago", 1)
question7 = Trivia("What is the capital of France ", "Paris", 1)
question8 = Trivia("Who is the current President of the USA ", "Joe Biden", 1)
question9 = Trivia("What does CRUD stand for ", "create read update delete", 1)
question10 = Trivia("Who made Rockstar Made ", "CARTI", 1)



questionList = [
    question1, question2, question3, question4, question5, question6, question7, question8, question9, question10
]

@create_tk.route('/createtask/', methods=['GET','POST'])
def createtask():
    userinput = request.form['userinput']
    randomValue = questionList[rand.randint(0, len(questionList)-1)]
    if randomValue.checkanswer():
        score = score + 1
    else:
        questionList.remove(randomValue)

    return render_template("createtask.html", randomValue=randomValue, score=score)

@create_tk.route('/rohancreatetask/', methods=['GET','POST'])
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

