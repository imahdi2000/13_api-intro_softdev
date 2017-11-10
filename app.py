from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('choose.html')

@my_app.route('/trivia')
def trivia():


@my_app.route('/nasa')
def nasa():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=t36Ut0AZaGzL4mvtyCVaIKciVYrvDLoleqChpBkW")
    data_string = u.read()
    dic = json.loads(data_string)
    picture = dic["url"]
    comment = dic["question"]
    print "done"
    return render_template('nasa.html' , picture = picture , comment = comment)



if __name__ == '__main__':
   my_app.debug = True
   my_app.run() #run the web app
