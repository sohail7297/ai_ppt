from core.ai_engine import generate_presentation_content
from core.ppt_generator import create_presentation

data = generate_presentation_content(
    topic="Artificial Intelligence",
    style="Technical",
    slide_count=5
)

ppt_file = create_presentation(
    topic="Artificial Intelligence",
    slides_data=data["slides"],
    theme_name="Black Gold"
)

print("Presentation Created:")
print(ppt_file)