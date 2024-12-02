import json

# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template,request,session

import objects as object
import requests

import utils
import utils as trans
from bs4 import BeautifulSoup
import requests

import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
REMOTE_SERVER='https://theholylemonlord.pythonanywhere.com/export'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz',methods=['POST'])
def quiz():
    data=request.form
    questions = genMC(data['url'])
    if questions==[]:
        return render_template("error.html")
    else:
        if data['choice'] == 'MultipleChoice':
            print(data['url'])
            print(data['choice'])
            return render_template('multipleChoice.html', data=questions)
            # return render_template('test.html',data=questions)
        else:
            return render_template('fillInTheBlanks.html', data=questions)


@app.route('/score',methods=['POST'])
def showSore():
    print(request.form.keys())

    answ=[]
    real=[]
    values =list(request.form.listvalues())
    keys=list(request.form.keys())
    for i in range(len(keys)):
        print(keys[i])
        if keys[i].startswith("answers"):
            answ.append(values[i])
        else:
            real.append(values[i])




    print(answ)
    print(real)
    #export=[]
    answers=[]
    #for d in data:
     #   print(d[0])
     #   export.append(d[0])
        #answers.append(d[0]['real_answer'])
    #print(export)
    #print(answers)
    result=check_answers(answ,real)
    print("FINAL SCORE IS: ",result,"%")
    render_result=[]
    if result>=85:
        render_result.append(result)
        render_result.append("THE FORCE IS STRONG WITH THIS ONE")
    elif result>=75:
        render_result.append(result)
        render_result.append("Wow! Looks like someone was paying attention..")
    elif result>=65:
        render_result.append(result)
        render_result.append("Hmmm ok i guess...")
    elif result >=50:
        render_result.append(result)
        render_result.append("I FIND YOUR LACK OF A HIGH SCORE DISTURBING!")
    else:
        render_result.append(result)
        render_result.append("THESE AREN'T THE SCORES YOU'RE LOOKING FOR!")


    return render_template("score.html",data=render_result)



def prompt_request(transcript,type,questions=None):
    export=utils.export(type,transcript,questions)
    #export_obj={"prompt":export}
    #print(json.dumps(export_obj))
    data = requests.post(REMOTE_SERVER,{"prompt":export})
    print(data.content)
    return data
def check_answers(answ,real):
    #answers=[]
    count=0
    #for i in range(10):
    #    answers.append("Ankara")

    for i in range (len(answ)):
        if str(answ[i]).lower() ==str(real[i]).lower():
            count+=1
    score=int(count/len(answ)*100)
    return score

def genMC(url):
    transcript=trans.stringify(url)
    data=prompt_request(transcript,"questions")
    print(type(data.text),"before cleaner")

    cleaned_data=utils.cleaner(data.text)
    print(cleaned_data)
    if type(cleaned_data)!=type(''):
        return cleaned_data
    else:
        return []




app.run(port=9999)