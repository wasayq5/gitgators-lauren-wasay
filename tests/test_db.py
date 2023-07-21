# tests.py
import unittest
from peewee import *
from app import TimelinePost
import requests
import json

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
        first_post = TimelinePost.create(name='John Doe', email='john@exampele.com', content='Hello world, I\'m John.')
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane')

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    # def clear_timeline_posts(self):
    #     # Clear all records from the TimelinePost table
    #     TimelinePost.delete().execute()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@exampele.com', content='Hello world, I\'m John.')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane')
        assert second_post.id == 2

        # Get the timeline posts using the API endpoint
        response = requests.get('http://198.199.86.119:5000/api/timeline_post')  

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON, makes JSON data available as a python dictionary stored in the variable 'data'
        data = response.json()
        print("response.json as stored in 'data'", data)

        # Ensure 'data' contains the key "timeline_posts"
        self.assertIn('timeline_posts', data)

        # Get the timeline posts from the response
        timeline_posts = data['timeline_posts']

        # Perform assertions on the timeline posts
        print("Fetched Timeline Posts:", timeline_posts)

        self.assertEqual(len(timeline_posts), 2)

        # Check the first post
        self.assertEqual(timeline_posts[0]['id'], 1)
        self.assertEqual(timeline_posts[0]['name'], 'John Doe')
        self.assertEqual(timeline_posts[0]['email'], 'john@example.com')
        self.assertEqual(timeline_posts[0]['content'], "Hello world, I'm John.")

        # Check the second post
        self.assertEqual(timeline_posts[1]['id'], 2)
        self.assertEqual(timeline_posts[1]['name'], 'Jane Doe')
        self.assertEqual(timeline_posts[1]['email'], 'jane@example.com')
        self.assertEqual(timeline_posts[1]['content'], "Hello World, I'm Jane")



       