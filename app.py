from flask import Flask, render_template, request, redirect, url_for, flash, session
import urllib2, json, os

my_app = Flask(__name__)
my_app.secret_key = os.urandom(64)

@my_app.route('/')
def root():
    return render_template('choose.html')

@my_app.route('/trivia')
def trivia():
    return render_template("trivia.html")

@my_app.route('/nasa')
def nasa():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=t36Ut0AZaGzL4mvtyCVaIKciVYrvDLoleqChpBkW")
    data_string = u.read()
    dic = json.loads(data_string)
    picture = dic["url"]
    comment = dic["explanation"]
    print comment
    print "done"
    return render_template('nasa.html' , picture = picture , comment = comment)

@my_app.route('/show', methods = ["GET","POST"])
def show():
    if request.method == 'POST':
        num = int(request.form['num'])
        amount = "amount" + "=" + request.form['num'] + "&"
        category = "category" + "=" + request.form["genre"] + "&"
        difficulty = "difficulty" + "=" + request.form["difficulty"] + "&"
        Type = "type" + "=" + request.form["type"]
        layout = request.form["type"]
        snippet = amount + category + difficulty + Type
        u = urllib2.urlopen("https://opentdb.com/api.php?" + snippet)
        data_string = u.read()
        dic = json.loads(data_string)
        questions = []
        answers = []
        incorrect = []
        if dic['response_code'] == 0:
            results = dic["results"]
            for i in range(num):
                questions.append(results[i]["question"])
                answers.append(results[i]["correct_answer"])
                incorrect.append(results[i]['incorrect_answers'])
            return render_template("results.html", Q = questions, A = answers, B = incorrect)
        else:
            flash("Sorry, we don't have enough of those questions. Try again!")
            return render_template("trivia.html")
    else:
        return render_template("trivia.html")

if __name__ == '__main__':
   my_app.debug = True
   my_app.run()
