from lib.todo_list import *

# Given a task
# TodoList adds task to the incomplete tasks list 

def test_adds_task_to_incomplete_tasks_list_when_given_a_task():
    todo_list = TodoList()
    todo_list.add_task("Book dentist appointment")
    result = todo_list.show_incomplete_tasks()
    assert result == ["Book dentist appointment"]


# Given a completed task as a string 
# TodoList removes the task from the list 

def test_given_a_completed_task_as_a_string_it_removes_the_task_from_the_list():
    todo_list = TodoList()
    todo_list.add_task("Book dentist appointment")
    todo_list.mark_complete("Book dentist appointment")
    result = todo_list.show_incomplete_tasks()
    assert result == []

""""
# Given no tasks 
# show_incomplete_tasks returns and empty list 

todo_list = TodoList()
todo_list.show_incomplete_tasks() # => []

# Given multiple tasks 
# show_incomplete_tasks returns all incomplete tasks 

todo_list = TodoList()
todo_list.add_task("Book dentist appointment")
todo_list.add_task("Buy milk")
todo_list.show_incomplete_tasks() # => ["Book dentist appointment", "Buy milk"]
"""