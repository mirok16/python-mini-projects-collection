tasks = []
def add_task(task):
    tasks.append(task)
def list_tasks():
    return tasks
if __name__ == "__main__":
    add_task("Learn GitHub")
    print(list_tasks())
