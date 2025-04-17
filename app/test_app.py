import pytest
from app import app, db, Task  # Import your Flask app and db model

@pytest.fixture
def client():
    """Setup and teardown for Flask tests."""
    with app.test_client() as client:
        # Create tables before testing
        with app.app_context():
            db.create_all()
        yield client
        # Teardown: Drop tables after tests
        with app.app_context():
            db.drop_all()

def test_index(client):
    """Test for the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Todo List' in response.data  # Check if the page contains 'Todo List'

def test_add_task(client):
    """Test adding a task."""
    response = client.post('/', data={
        'task': 'Test Task',
        'deadline': '2025-12-31'
    })
    assert response.status_code == 302  # Redirects back to the index page after adding task
    # Check if the task appears in the database
    task = Task.query.filter_by(description='Test Task').first()
    assert task is not None
    assert task.deadline == '2025-12-31'

def test_delete_task(client):
    """Test deleting a task."""
    # Add a task first
    task = Task(description='Task to delete')
    db.session.add(task)
    db.session.commit()

    response = client.post('/', data={'delete': task.id})
    assert response.status_code == 302  # Redirects after deletion
    # Check if the task has been deleted from the database
    task = Task.query.get(task.id)
    assert task is None
