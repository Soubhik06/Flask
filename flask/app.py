from flask import Flask,render_template
###wsgi application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask course</H1<html>"
@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
