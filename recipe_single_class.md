# TodoList Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

Clarifying notes: 
- Tasks are stored as strings.
- The list shows only incomplete tasks.
- When a task is marked complete, it disappears from the list. 


## 2. Design the Class Interface
_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TodoList :
    # User-facing properties:
    #   None 

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        # Creates/stores an empty list of tasks on the object 
        pass 

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass

    def show_incomplete_tasks(self):
        # Parameters:
        #   None 
        # Returns:
        #   A list of all incomplete tasks 
        # Side-effects:
        #   None 
        pass 

    def mark_complete(self, completed_task):
        # Parameters:
        #   completed_task: a string representing the task to mark as complete
        # Returns:
        #   Nothing
        # Side-effects:
        #   Removes the task from the list of incomplete tasks  
        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# Given a task
# TodoList adds task to the incomplete tasks list 

todo_list = TodoList()
todo_list.add_task("Book dentist appointment")
todo_list.show_incomplete_tasks() # => ["Book dentist appointment"]

# Given a completed task as a string 
# TodoList removes the task from the list 

todo_list = TodoList()
todo_list.add_task("Book dentist appointment")
todo_list.mark_complete("Book dentist appointment")
todo_list.show_incomplete_tasks() # => []

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
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

