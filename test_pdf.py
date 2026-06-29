from core.ai_engine import generate_presentation_content
from core.pdf_export import export_to_pdf

data = generate_presentation_content(
    topic="Artificial Intelligence",
    style="Technical",
    slide_count=5
)

pdf_file = export_to_pdf(
    topic="Artificial Intelligence",
    slides_data=data["slides"]
)

print(pdf_file)