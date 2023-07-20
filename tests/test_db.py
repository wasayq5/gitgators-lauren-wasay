# tests.py
import unittest
from peewee import *
from app import TimelinePost

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
        # Create two timeline posts for testing
    first_post = TimelinePost.create(name='John Doe', email='john@example.com', content="Hello world, I'm John.")
    second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content="Hello World, I'm Jane")

    # Fetch the timeline posts
    timeline_posts = TimelinePost.query.all()

    # Perform assertions
    assert len(timeline_posts) == 2

    assert timeline_posts[0].id == 1
    assert timeline_posts[0].name == first_post.name
    assert timeline_posts[0].email == first_post.email
    assert timeline_posts[0].content == first_post.content

    assert timeline_posts[1].id == 2
    assert timeline_posts[1].name == second_post.name
    assert timeline_posts[1].email == second_post.email
    assert timeline_posts[1].content == second_post.content