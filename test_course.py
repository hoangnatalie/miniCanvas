import pytest
from course import Course, CourseManager
from unittest.mock import Mock

@pytest.fixture
def course_manager():
    return CourseManager()

def test_create_a_course_and_find_a_course(course_manager, mocker):
    mock_course = Mock()
    mocker.patch.object(course_manager, 'generate_id', return_value = mock_course)
    course_id = course_manager.create_a_course("COSC341", "Winter 2024", ["Natalie Hoang"])
    course = course_manager.find_a_course(mock_course)
    assert course_id == mock_course
    assert course is not None
    assert course.course_code == "COSC341"
