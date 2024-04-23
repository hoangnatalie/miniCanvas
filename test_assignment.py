import pytest
from assignment import Assignment
from unittest.mock import Mock

@pytest.fixture
def assignment():
    return Assignment(assignment_id = 1, due_date = '2024-04-30', course_id = 101)

def test_assignment_creation(assignment, mocker):
    mock_assignment = Mock()
    mocker.patch.object(assignment, '__init__', return_value = mock_assignment)
    assignment = assignment.__init__("Homework 1", "Description of Homework 1", 1)
    assert assignment == mock_assignment

def test_assignment_submit(assignment):
    assignment.submit("Test Submission")
    assert len(assignment.submission_list) == 1
    assert assignment.submission_list[0] == "Test Submission"