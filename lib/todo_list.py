class TodoList :

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_incomplete_tasks(self):
        return self.tasks 

    def mark_complete(self, completed_task):
        self.tasks.remove(completed_task)
