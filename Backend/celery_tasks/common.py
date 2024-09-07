def set_task_progress(task_details, progress: int):
    progress = str(progress)
    task_details.update_state(state='PROGRESS', meta={'progress': progress})
