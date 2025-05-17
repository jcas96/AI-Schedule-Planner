import pandas as pd
from datetime import datetime, timedelta
import random

tasks = pd.DataFrame({
    'task': ['Math hw', 'Physics ASSI.', 'history proj', 'chem lab','prog prac'],
    'deadline': ['2025-04-30', '2025-04-28', '2025-04-26', '2025-04-25', '2025-04-27'],
    'estimated_time': [2, 3, 4, 1, 2]  # in hours
})

tasks['deadline'] = pd.to_datetime(tasks['deadline'])

def create_study_sched(tasks):
    schedule = []
    current_time = datetime.now()

    for index, task in tasks.iterrows():
        task_time = task['estimated_time']
        deadline = task['deadline']

        time_left = deadline - current_time

        study_day = current_time + timedelta(days=random.randint(1, time_left.days))
        schedule.append((task['task'], study_day.strftime("%Y-%m-%d %H:%M:%S"), task_time))

    return schedule

study_schedule = create_study_sched(tasks)
for task in study_schedule:
    print(f"Study '{task[0]}' on {task[1]} for {task[2]} hours.")
