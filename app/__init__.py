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
        {'company': 'Cadence', 'position': 'Application Engineer', 'duration': 'Jun 2023 - Present'},
        {'company': 'Intel', 'position': 'Firmware Validation Engineering and SSD Technical Intern', 'duration': 'June 2020 - Dec 2021'},
        {'company': 'NASA', 'position': 'Public Education and Outreach Intern', 'duration': 'Aug - Dec 2018'}
    ]
    return render_template('work.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences)


@app.route('/education')
def education():
    school_experiences = [
        {'school': 'CSU Sacramento', 'degree': 'Electrical and Electronics Engineering - BS', 'duration': '2019 - 2023'},
        {'school': 'Sacramento City College', 'degree': 'Electrical and Electronics Engineering - AS', 'duration': '2018'},
        {'school': 'Fresno City College', 'degree': 'Electrical and Electronics Engineering - AS', 'duration': '2016 - 2018'}
    ]
    return render_template('education.html', title="MLH Fellow", url=os.getenv("URL"),
                           school_experiences=school_experiences)


@app.route('/hobbies')
def hobbies():
    hobby_experiences = [
        {'type': 'Tarantula Husbandry', 'description': 'I like to collect and take care of tarantulas! I currently have 5 species of New World Tarantulas.', 'image': './img/hobbies/hobby_image1.jpeg'},
        {'type': 'Drinking Coffee', 'description': 'I love coffee! My favorite drink right now is an iced vanilla latte.', 'image': './img/hobbies/hobby_image2.jpg'},
        {'type': 'Growing Plants', 'description': 'Plants are very cute! I want to start my own garden, but for now I am just sticking to indoor plants.', 'image': './img/hobbies/hobby_image3.jpeg'}
    ]
    return render_template('hobbies.html', title="MLH Fellow", url=os.getenv("URL"), hobby_experiences=hobby_experiences)
