import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/work')
def work():
    work_experiences = [
        {'company': 'Example Company', 'position': 'Example Position', 'duration': 'Example Duration'},
        {'company': 'Example Company', 'position': 'Example Position', 'duration': 'Example Duration'}
    ]
    return render_template('work.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences)


@app.route('/education')
def education():
    school_experiences = [
        {'school': 'Swarthmore College', 'degree': 'Computer Science', 'duration': '2020-2024'}
    ]
    return render_template('education.html', title="MLH Fellow", url=os.getenv("URL"),
                           school_experiences=school_experiences)


@app.route('/hobbies')
def hobbies():
    hobby_experiences = [
        {'type': 'Example hobby', 'description': 'Example description', 'image': './img/hobbies/hobby_image1.jpeg'}
    ]
    return render_template('hobbies.html', title="MLH Fellow", url=os.getenv("URL"), hobby_experiences=hobby_experiences)
