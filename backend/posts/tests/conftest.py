import pytest
from posts.models import Post

@pytest.fixture
@pytest.mark.django_db
def seed_data_for_db_delete():
    Post(user_id=1, title='dummy', body='dummy').save()
    Post(user_id=2, title='dummy', body='dummy').save()


@pytest.fixture
@pytest.mark.django_db
def seed_data_for_db_update():
    Post(user_id=3, title='dummy', body='dummy').save()