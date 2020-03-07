from flask import Flask, escape, request, render_template
import sys
sys.path.append('../')
import main1 as m

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index_basic.html')

@app.route('/', methods=['POST'])
def my_form_post():
	sentence = request.form['sentence']
	print(sentence)
	m.setSentence(sentence, 2)

	return sentence

