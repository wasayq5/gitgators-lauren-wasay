# tests.py
import unittest
from peewee import *
from app import TimelinePost
# import requests
# import json

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@exampele.com', content='Hello world, I\'m John.')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane')
        assert second_post.id == 2

        # Step 1: Send POST requests to create timeline posts
        post_data_1 = {'name': 'John Doe', 'email': 'john@example.com', 'content': "Hello world, I'm John."}
        post_data_2 = {'name': 'Jane Doe', 'email': 'jane@example.com', 'content': "Hello World, I'm Jane"}

        response_1 = requests.post('/api/timeline_post', data=post_data_1)
        assert response_1.status_code == 200
        first_post_id = response_1.json()['id']
        assert first_post_id == 1  # Assuming the first post ID is 1

        response_2 = requests.post('/api/timeline_post', data=post_data_2)
        assert response_2.status_code == 200
        second_post_id = response_2.json()['id']
        assert second_post_id == 2  # Assuming the second post ID is 2

        # Step 2 and 3: Send GET request to fetch timeline posts
        response = requests.get('/api/timeline_post')
        assert response.status_code == 200

        # Step 4: Compare the attributes of the fetched timeline posts
        timeline_posts = response.json()['timeline_posts']

        assert len(timeline_posts) == 2

        assert timeline_posts[0]['id'] == first_post_id
        assert timeline_posts[0]['name'] == 'John Doe'
        assert timeline_posts[0]['email'] == 'john@example.com'
        assert timeline_posts[0]['content'] == "Hello world, I'm John."

        assert timeline_posts[1]['id'] == second_post_id
        assert timeline_posts[1]['name'] == 'Jane Doe'
        assert timeline_posts[1]['email'] == 'jane@example.com'
        assert timeline_posts[1]['content'] == "Hello World, I'm Jane"