from todo_app.todo import add_task, list_tasks

def test_add_task():
    add_task("Test")
    assert "Test" in list_tasks()
