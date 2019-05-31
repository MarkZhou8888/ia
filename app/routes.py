from flask import *
from app import app
from app.models import giphy

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/facts')
def facts():
    return render_template('facts.html')

@app.route('/shoData',methods=['GET','POST'])
def shoData():
    userdata = dict(request.form)
    print(userdata)
    return render_template('shoData.html', name=userdata['name'][0], age=userdata['age'][0])

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/form2')
def form2():
    return render_template('form2.html')

@app.route('/shoData2',methods=['GET','POST'])
def shoData2():
    userdata = dict(request.form)
    #parse out user input
    search_term = userdata["meme"][0]
    data = giphy.api_call(search_term)
    return render_template('shoData2.html', data=data)
