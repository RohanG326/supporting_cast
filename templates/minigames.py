from flask import Flask, Blueprint, render_template, request
import requests
from __init__ import app
import json

mini_game = Blueprint('minigames', __name__,
                      url_prefix='/minigames',
                      template_folder='templates',
                      static_folder='static', static_url_path='static/minigames')

darkmode="darkmode"

@mini_game.route('/minigames', methods=['GET', 'POST'])
def minigames():
    if request.form:
        word1 = request.form.get("word1")
        word2 = request.form.get("word2")
        if len(word1) < len(word2):
            shorterlen = len(word1)
            difference = len(word2) - len(word1)
        else:
            shorterlen = len(word2)
            difference = len(word1) - len(word2)
        for x in range(0, shorterlen):
            if word1[x] != word2[x]:
                difference += 1
        return render_template("pbl/minigames.html", result=difference, darkmode=darkmode)
    return render_template("pbl/minigames.html", darkmode=darkmode)

@mini_game.route('/jeopardy', methods=['GET', 'POST'])
def jeopardy():
    return render_template("pbl/jeopardy.html", darkmode=darkmode)