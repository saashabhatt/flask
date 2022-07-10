from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    title = satisfaction_survey.title
    inst = satisfaction_survey.instructions
    for num in range(len(satisfaction_survey.questions)):
        session[f'selections/{num}'] = ""
    responses = []
    return render_template("home.html", title=title, inst=inst)

@app.route('/questions/<number>')
def ask_question(number):
    num = int(number)
    
    if (len(responses) != num):
        num = len(responses)
        flash("Invalid URL")
        return redirect(f'/questions/{num}')
    
    elif (len(responses) == len(satisfaction_survey.questions)):
        flash("Survey Complete")
        return redirect('/thankyou')
    
    ask_quest = satisfaction_survey.questions[num].question
    options = satisfaction_survey.questions[num].choices
   
    return render_template("questions.html", ask_quest=ask_quest,
    options=options, num=num)

@app.route('/answers/<num>', methods=['POST'])
def store_answ(num):
    num = int(num)

    num_of_q = len(satisfaction_survey.questions)
    k = f"/questions/{num + 1}" if num < (num_of_q - 1) else '/thankyou'
    session[f'selections/{num}'] = request.form[f'answers/{num}']
    responses.append(session[f'selections/{num}'])
    return redirect(k)

@app.route('/thankyou')
def thanks():
    return render_template("thanks.html")