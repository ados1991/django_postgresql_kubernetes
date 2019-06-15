import pytest

@pytest.mark.django_db
class TestPosts:

    def test_get_posts_should_return_200(self, client):
        response = client.get('/posts')
        assert response.status_code == 200

    def test_get_posts_should_return_0_posts(self, client):
        response = client.get('/posts')
        assert len(response.json()) == 0

    def test_add_post_should_succeed(self, client):
        data = {'title': 'title1', 'body': 'body1', 'user_id': 1}
        response = client.post('/posts', data=data, content_type='application/json')
        assert response.status_code == 201
