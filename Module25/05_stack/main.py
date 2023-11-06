class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, description, priority):
        task = (description, priority)
        self.tasks.push(task)

    def remove_task(self, description):
        temp_stack = Stack()
        while not self.tasks.is_empty():
            task = self.tasks.pop()
            if task[0] != description:
                temp_stack.push(task)
        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

    def __str__(self):
        sorted_tasks = sorted(self.tasks.items, key=lambda task: task[1])
        task_dict = {}
        for task in sorted_tasks:
            description, priority = task
            if priority in task_dict:
                task_dict[priority].append(description)
            else:
                task_dict[priority] = [description]
        result = []
        for priority, descriptions in task_dict.items():
            result.append(f"{priority} {'; '.join(descriptions)}")
        return "\n".join(result)


manager = TaskManager()
manager.new_task("", 4)
manager.new_task("", 2)
manager.new_task("", 1)
manager.new_task("", 4)
print(manager)

manager.remove_task("")
print(manager)

