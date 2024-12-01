import json

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api import YouTubeTranscriptApi

import objects as obj


class questionBank:
    def __init__(self):
        self.question=None
        self.a=None
        self.b=None
        self.c=None
        self.d=None
        self.answer=None
    def set_question(self,question):
        self.question=question
    def set_a(self,a):
        self.a=a
    def set_b(self,b):
        self.b=b
    def set_c(self,c):
        self.c=c
    def set_d(self,d):
        self.d=d
    def set_answer(self,answer):
        self.answer=answer
    def get_question(self):
        return self.question
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def get_d(self):
        return  self.d
    def ger_answer(self):
        return self.answer



def stringify(url):
    id = url.split('watch?v=')
    srt = YouTubeTranscriptApi.get_transcript(id[1])
    tran = ''
    for i in srt:
        var = i["text"]
        # print(i["text"])
        # print(var)
        tran += var
    return tran






'''
two='https://www.youtube.com/watch?v=TQMbvJNRpLE'
srt,name=trans('https://www.youtube.com/watch?v=-kqrVJGXqj8')



#print(tran)
#data = requests.post('https://theholylemonlord.pythonanywhere.com/export', json={"context": tran,"type":"multiple_choice","questions":None})
data=requests.get('https://theholylemonlord.pythonanywhere.com/connect')
print(data.status_code)
#print(data.content)
#print(data.json())
question=data.json()['quiz']
print(question)
print(type(question[0]),"Type of questions")
'''

def cleaner(data):
    print(type(data),"after cleaner")
    test={"key":"value","key2":"value2"}
    obj_list=[]
    try:
        questions = json.loads(data)
        print(type(questions),"in try block")
        print(questions)
        if type(questions) == type(obj_list):
            for item in questions:
                q_obj = obj.multiplechoice()
                q_obj.set_question(item['question'])
                q_obj.set_a(item['options'][0])
                q_obj.set_b(item['options'][1])
                q_obj.set_c(item['options'][2])
                q_obj.set_d(item['options'][3])
                q_obj.set_answer(item['answer'])
                obj_list.append(q_obj)
        return obj_list
    except Exception:
        return "Something went wrong try again later" + Exception




def export(typ,context,questions=None):
    prompt = get_prompt(typ)
    if typ=='answers':
        export = "context: "+str(context)+" prompt: "+str(prompt)+" questions: "+str(questions)
        return export
    else:
        export="context: "+str(context)+" prompt: "+str(prompt)
        return export




def get_prompt(typ):
    temp='''
    [{'question': 'What is the capital of France?', 'options': ['Berlin', 'Paris', 'Rome', 'Madrid'], 'answer': 'Paris'},
    {'question': 'What is the highest mountain in the world?', 'options': ['K2', 'Kangchenjunga', 'Mount Everest', 'Lhotse'], 'answer': 'Mount Everest'}]'''
    prompt_dic= {
        "questions": "Generate ten multiple choice questions based on the given context, provide four possible options for each question, use this format"+temp ,
        "answers": "Generate answers for each of the questions provided in the context"
     }
    prompt=prompt_dic[typ]
    return prompt




#obj_list=cleaner(data)
#print(obj_list)
'''
for item in real_final:
	q_obj=obj.multiplechoice()
	split_q=item.split("{questions': '")[1]
	str_q=split_q.split("',")
	q_obj.set_question(str_q[0])

	split_op1=str_q[1].split("'options': ['")[1]
	str_op1=split_op1.split("',")
	q_obj.set_a(str_op1[0])

	split_op2=str_op1[1].split("', '")[1]
	str_op2=split_op2.split("',")
	q_obj.set_b(str_op2[0])

	split_op3=str_op2[1].split("', '")[1]
	str_op3=split_op3.split("',")
	q_obj.set_c(str_op3[0])

	split_op4=str_op3[1].split("', '")[1]
	str_op4=split_op4.split("'],'answer': '")
	q_obj.set_d(str_op4[0])

	split_a=str_op4[1]
	str_a=split_a.split("'}")
	q_obj.set_answer(str_a[0])

	obj_list.append(q_obj)
'''

'''
for item in obj_list:
	print(item.question,item.a,item.b,item.c,item.d,item.answer)


with open(name+".txt", "w") as f:
	for i in srt:
		f.write("{}\n".format(i["text"]))

'''
one='https://www.youtube.com/watch?v=-kqrVJGXqj8'


one='-kqrVJGXqj8'
# using the srt variable with the list of dictionaries
# obtained by the .get_transcript() function

