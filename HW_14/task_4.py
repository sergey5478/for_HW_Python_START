import pytest
import json
from task_1 import User
from task_2 import LevelException, AccessException
from task_3 import Project


@pytest.fixture
def temp_file(tmp_path):
    filename = tmp_path / "test_users.json"
    yield filename
    filename.unlink()


@pytest.fixture
def sample_project():
    users = [
        User("001", "Alice", 1),
        User("002", "Bob", 2),
        User("003", "Carol", 3),
    ]
    return Project(users)


def test_login_valid(sample_project):
    sample_project.login("001", "Alice")
    assert sample_project.admin is not None
    assert sample_project.admin.user_id == "001"


def test_login_invalid(sample_project):
    with pytest.raises(AccessException):
        sample_project.login("009", "Eve")


def test_add_user_valid(sample_project):
    sample_project.login("001", "Alice")
    sample_project.add_user("010", "Dave", 4)
    assert any(user.user_id == "010" for user in sample_project.users)


def test_add_user_invalid(sample_project):
    sample_project.login("003", "Carol")
    with pytest.raises(LevelException):
        sample_project.add_user("012", "Frank", 3)


def test_project_load(temp_file):
    data = {
        "1": {"001": "Alice"},
        "2": {"002": "Bob"},
        "3": {"003": "Carol"},
    }
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    project = Project.load(temp_file)
    assert project is not None
    assert len(project.users) == 3


def test_user_name_not_empty():
    user = User("001", "Alice")
    assert user.name != ""


def test_user_name_initialized():
    user = User("001", "Alice")
    assert user.name == "Alice"


if __name__ == '__main__':
    pytest.main()
