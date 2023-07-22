import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TODO Add more tests relating to the home page

         # Test the presence of navigation links
        assert '<a href="/work">Work Experience</a>' in html
        assert '<a href="/education">Education</a>' in html
        assert '<a href="/hobbies">Hobbies</a>' in html
        assert '<a href="/timeline">Timeline Posts</a>' in html

        # Test the profile picture
        assert '<img src="./static/img/me.jpeg">' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page
        response_timeline_page = self.client.get("/timeline")
        assert response_timeline_page.status_code == 200
        html = response_timeline_page.get_data(as_text=True)
        assert "<h2>Create Post</h2>" in html

         # Test POST request to /api/timeline_post
        post_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": "This is a test post.",
        }
        response = self.client.post("/api/timeline_post", data=post_data)
        print("RESPONSE STATUS CODE:")
        print(response.status_code)
        assert response.status_code == 200
        assert response.is_json
        json_data = response.get_json()
        assert "id" in json_data
        assert "name" in json_data
        assert "email" in json_data
        assert "content" in json_data
        assert json_data["name"] == "John Doe"
        assert json_data["email"] == "john@example.com"
        assert json_data["content"] == "This is a test post."

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        print(html)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "abcxyz", "content": "Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
