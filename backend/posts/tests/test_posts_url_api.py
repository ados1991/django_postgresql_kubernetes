import pytest

# tests can be refactored
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

    def test_filter_posts_should_return_all_posts_belongs_to_specified_user_id(self, client, seed_data_for_api):
        test_user_id = 4
        response = client.get('/posts', {'user_id': test_user_id})
        results = response.json()
        assert len(results) == 2
        assert all(x['user_id'] == test_user_id for x in results)

    def test_get_specified_post_should_succeed(self, client, seed_data_for_api):
        post_id = 1
        response = client.get(f'/posts/{post_id}')
        result = response.json()
        assert isinstance(result, dict)
        assert result['id'] == post_id

    def test_put_specified_post_should_succeed(self, client, seed_data_for_api):
        post_id = 1
        response = client.get(f'/posts/{post_id}')
        params = response.json()
        assert params['body'] == "dummy"
        params['body'] = "new_dummy"
        client.put(f'/posts/{post_id}', params, content_type='application/json')
        response = client.get(f'/posts/{post_id}')
        new_body_value = response.json()['body']
        assert new_body_value == "new_dummy"

    def test_delete_specified_post_should_succeed(self, client, seed_data_for_api):
        post_id = 1
        response = client.get(f'/posts/{post_id}')
        assert response.status_code == 200
        data = response.json()
        assert data['body'] == 'dummy'
        client.delete(f'/posts/{post_id}')
        response = client.get(f'/posts/{post_id}')
        assert response.status_code == 404
