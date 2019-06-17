import pytest
from posts.models import Post

@pytest.mark.django_db
def test_create_post():
    p = Post(userId=1, title='dummy', body='dummy')
    p.save()
    assert p.userId == 1

@pytest.mark.django_db
def test_update_post(seed_data_for_db_update):
    # warning updates all posts with userId=3
    Post.objects.filter(userId=3).update(title='dummy2')
    assert Post.objects.filter(userId=3)[0].title == 'dummy2'

@pytest.mark.django_db
def test_delete_post(seed_data_for_db_delete):
    posts = Post.objects.filter(userId=1)
    for post in posts:
        post.delete()
    assert len(Post.objects.filter(userId=1)) == 0
