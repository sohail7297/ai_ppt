import json
import os
from datetime import datetime

HISTORY_FILE = "history/projects.json"


def initialize_history():

    os.makedirs("history", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)


def load_projects():

    initialize_history()

    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def save_project(
        topic,
        style,
        slide_count,
        ppt_file=None,
        pdf_file=None
):

    projects = load_projects()

    project = {
        "topic": topic,
        "style": style,
        "slide_count": slide_count,
        "ppt_file": ppt_file,
        "pdf_file": pdf_file,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    projects.insert(0, project)

    with open(HISTORY_FILE, "w") as file:
        json.dump(
            projects,
            file,
            indent=4
        )


def delete_project(index):

    projects = load_projects()

    if 0 <= index < len(projects):
        projects.pop(index)

    with open(HISTORY_FILE, "w") as file:
        json.dump(
            projects,
            file,
            indent=4
        )