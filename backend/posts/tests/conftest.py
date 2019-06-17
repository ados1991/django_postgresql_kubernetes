import pytest
from posts.models import Post

@pytest.fixture
@pytest.mark.django_db
def seed_data_for_db_delete():
    Post(userId=1, title='dummy', body='dummy').save()
    Post(userId=2, title='dummy', body='dummy').save()


@pytest.fixture
@pytest.mark.django_db
def seed_data_for_db_update():
    Post(userId=3, title='dummy', body='dummy').save()


@pytest.fixture
@pytest.mark.django_db
def seed_data_for_api():
    Post(userId=3, title='dummy', body='dummy').save()
    Post(userId=4, title='dummy', body='dummy').save()
    Post(userId=4, title='dummy', body='dummy').save()
