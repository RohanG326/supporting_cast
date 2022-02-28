# import "packages" from flask

from flask import render_template, request
from __init__ import app
import requests

from templates.travel import travel_pg
app.register_blueprint(travel_pg)

from templates.about import about_pg
app.register_blueprint(about_pg)

from api.webapi import api_bp
app.register_blueprint(api_bp)

from createtask.create_task import create_tk
app.register_blueprint(create_tk)

from algorithm.algorithm import app_algorithm
app.register_blueprint(app_algorithm)

from crud.app_crud import app_crud
app.register_blueprint(app_crud)

from database.app_database import app_database
app.register_blueprint(app_database)

from flight.app_flight import app_flight
app.register_blueprint(app_flight)

from page.app_page import app_page
app.register_blueprint(app_page)

from crud.app_crud_api import app_crud_api
app.register_blueprint(app_crud_api)

from templates.minigames import mini_game
app.register_blueprint(mini_game)

darkmode="darkmode"

tictactoearray=[["","",""],["","",""],["","",""]]
# connects default URL to render index.html

@app.route('/')
def index():
    return render_template("index.html", darkmode=darkmode)

@app.route('/navbarsearch', methods=['GET', 'POST'])
def navbarsearch():
    if request.form:
        term = request.form.get("term")
        if len(term) != 0:
            return render_template("navbarsearch.html", navbarsearch=term, darkmode=darkmode)

@app.route('/searchtest/')
def searchtest():
    return render_template("searchtest.html", darkmode=darkmode)

@app.route('/hangman/')
def hangman():
    return render_template("brian_divya_create_task.html", darkmode=darkmode)

@app.route('/darkmode', methods=['GET', 'POST'])
def toggleDarkMode():
    global darkmode
    if darkmode == "darkmode":
        darkmode="lightmode"
    else:
        darkmode = "darkmode"
    print(darkmode)
    return ('', 200)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8081)
