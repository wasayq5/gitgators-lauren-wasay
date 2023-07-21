import os
import logging
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

logging.basicConfig(level=logging.INFO)

load_dotenv()
app = Flask(__name__)
# We want to use an in-memory instance of the database when executing tests so that our tests are not dependent upon a separate mysql instance. We can do this by setting the mydb variable to an in-memory sqlite database during testing.
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb=MySQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD"),host=os.getenv("MYSQL_HOST"),port=3306)

# if mydb.is_closed():
#     mydb.connect()
#     logging.info("Database connection established.")
# else:
#     logging.info("Database connection already open.")

class TimelinePost(Model):
    name=CharField()
    email=CharField()
    content=TextField()
    created_at=DateTimeField(default=datetime.datetime.now)

    class Meta:
        database=mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name=request.form['name']
    email=request.form['email']
    content=request.form['content']
    timeline_post=TimelinePost.create(name=name,email=email,content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline', methods=['GET', 'POST'])
def timeline():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']
        timeline_post = TimelinePost.create(name=name, email=email, content=content)

    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())

    return render_template('timeline.html', title="Timeline", timeline_posts=timeline_posts)


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
