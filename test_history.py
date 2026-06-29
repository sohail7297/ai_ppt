from core.project_manager import (
    save_project,
    load_projects
)

save_project(
    topic="Artificial Intelligence",
    style="Technical",
    slide_count=10,
    ppt_file="generated/ppt/ai.pptx",
    pdf_file="generated/pdf/ai.pdf"
)

projects = load_projects()

print(projects)