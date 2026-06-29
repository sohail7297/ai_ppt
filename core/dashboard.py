from core.project_manager import load_projects


def get_dashboard_stats():

    projects = load_projects()

    total_projects = len(projects)

    total_slides = sum(
        project["slide_count"]
        for project in projects
    )

    styles = {}

    for project in projects:

        style = project["style"]

        styles[style] = (
            styles.get(style, 0) + 1
        )

    return {
        "projects": total_projects,
        "slides": total_slides,
        "styles": styles
    }