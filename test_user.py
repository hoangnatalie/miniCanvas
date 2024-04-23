import pytest
from user import UserManager, User
from unittest.mock import Mock

@pytest.fixture
def user_manager():
    usermanager = UserManager()
    usermanager.create_a_user("Alice", "password123", "teacher")
    return usermanager

def test_user_creation(user_manager, mocker):
    mock_user = Mock()
    mocker.patch.object(user_manager, 'create_a_user', return_value=mock_user)
    user = user_manager.create_a_user("Alice", "password123", "teacher")
    assert user == mock_user

def test_find_users(user_manager):
    users = user_manager.find_users([1])
    assert len(users) == 1
    assert users[0].name == "Alice"
    assert users[0].type == "teacher"