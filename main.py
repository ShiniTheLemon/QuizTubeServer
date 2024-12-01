from flask import Flask, render_template

app = Flask(__name__)

import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('models/gemini-1.5-flash')
@app.route("/")
def index():
	model.generate_content()
	response=model.generate_content("What is the capital of turkey?")
	print(response.text)
	return response.text


if __name__ == "__main__":
	response=model.generate_content("What is the capital of turkey?")
	print(response.text)
  
	#app.run()

