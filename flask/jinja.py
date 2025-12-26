### jinja2 template engine
'''
{{}} expressions to print output in html
{%...%} statements for logic like if,for etc
{#..#} comments
'''
from flask import Flask,render_template,request
###wsgi application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask course</H1<html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello,{name}!'
    return render_template('form.html')
## variable rules
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam!"
    return render_template('result.html',result = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam!"
    exp = {'score':score,"result":res}
    return render_template('result1.html',result = exp)

if __name__ == "__main__":
    app.run(debug = True)
