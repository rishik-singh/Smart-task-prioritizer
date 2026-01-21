MAX_DEADLINE = 5 #u can change the max_deadline days accordingly
MAX_IMPORTANCE = 5 #u can change the max_importance wise list accordingly

def calculate_priority(task):
    deadline = task["deadline"]
    importance = task["importance"]
    # Edge case handling
    if deadline > MAX_DEADLINE:
        deadline = MAX_DEADLINE
    if importance > MAX_IMPORTANCE:
        importance = MAX_IMPORTANCE
    priority_score = importance + (MAX_DEADLINE - deadline)
    return priority_score

def prioritize_tasks(task_list):
    for task in task_list:
        task["priority_score"] = calculate_priority(task)
    return sorted(
        task_list,
        key=lambda x: x["priority_score"],
        reverse=True
    )

def get_tasks_from_user():
    tasks = []
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        print(f"\nTask {i + 1}")
        title = input("Title: ")
        deadline = int(input("Deadline (days): "))
        importance = int(input("Importance (1-5): "))
        tasks.append({
            "title": title,
            "deadline": deadline,
            "importance": importance
        })
    return tasks

if __name__ == "__main__":
    tasks = get_tasks_from_user()
    prioritized_tasks = prioritize_tasks(tasks)
    print("\nToday's Task Order:\n")
    for index, task in enumerate(prioritized_tasks, start=1):
        print(f"{index}. {task['title']}")
