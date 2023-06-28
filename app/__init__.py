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
        {'company': 'Company A', 'position': 'Position A', 'duration': '2010-2012'},
        {'company': 'Company B', 'position': 'Position B', 'duration': '2013-2015'},
        {'company': 'Company C', 'position': 'Position C', 'duration': '2016-2018'}
    ]
    return render_template('work.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences)


@app.route('/education')
def education():
    school_experiences = [
        {'school': 'School A', 'degree': 'Degree A', 'duration': '2010-2012'},
        {'school': 'School B', 'degree': 'Degree B', 'duration': '2013-2015'},
        {'school': 'School C', 'degree': 'Degree C', 'duration': '2016-2018'}
    ]
    return render_template('education.html', title="MLH Fellow", url=os.getenv("URL"),
                           school_experiences=school_experiences)


@app.route('/hobbies')
def hobbies():
    hobby_experiences = [
        {'type': 'Hobby A', 'description': 'Description A', 'image': './img/hobbies/hobby_image1.jpeg'},
        {'type': 'Hobby B', 'description': 'Description B', 'image': './img/hobbies/hobby_image2.jpg'},
        {'type': 'Hobby C', 'description': 'Description C', 'image': './img/hobbies/hobby_image3.jpeg'}
    ]
    return render_template('hobbies.html', title="MLH Fellow", url=os.getenv("URL"), hobby_experiences=hobby_experiences)
