from flask import Flask, escape, request, render_template, jsonify
import sys
sys.path.append('../')
import main1 as m

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index_basic.html')

@app.route('/parse', methods=['POST'])
def my_form_post():
    sentence = request.form['text']
    print("Sentence: ", sentence)
    error = m.setSentence(sentence, 2)
    if error:
        return jsonify("fail")
    else:
        return jsonify("ok")

