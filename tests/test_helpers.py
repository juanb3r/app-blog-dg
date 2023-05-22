import pytest
from app_blog.helpers import hash_sha256


@pytest.mark.django_db
def test_hash_sha256():
    value = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
    result = hash_sha256("12345")
    assert result == value
