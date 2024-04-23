from fastapi.testclient import TestClient
from main import app
from unittest.mock import Mock, patch

client = TestClient(app)

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to our miniCanvas!"

@patch('main.coursemanager.create_a_course')
@patch('main.coursemanager.find_a_course')
@patch('main.usermanager.find_users')
def test_create_a_course(mock_find_users, mock_find_a_course, mock_create_a_course):
    mock_create_a_course.return_value = 1
    mock_find_users.return_value = [Mock(name="Teacher")]
    mock_find_a_course.return_value = Mock(course_code="COSC341", semester="Winter 2024", teacher_list=[Mock(name="Teacher")])

    response = client.post("/courses/COSC341", json={"semester": "Winter 2024", "teacher_id_list": [1]})
    assert response.status_code == 200
    assert response.json() == 1

@patch('main.coursemanager.find_a_course')
@patch('main.usermanager.find_users')
def test_import_students(mock_find_users, mock_find_a_course):
    course_mock = Mock()
    course_mock.course_id = 1
    course_mock.student_id_list = [1, 3, 5]
    mock_find_a_course.return_value = course_mock
    mock_find_users.return_value = [Mock(name="Student")]

    response = client.put("/courses/1/students", json=[0])
    assert response.status_code == 200
    course_mock.import_students.assert_called_once()