from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
import os


def export_to_pdf(
        topic,
        slides_data,
        output_dir="generated/pdf"
):

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        output_dir,
        f"{topic.replace(' ','_')}.pdf"
    )

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            topic,
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    for slide in slides_data:

        story.append(
            Paragraph(
                slide["title"],
                styles["Heading2"]
            )
        )

        for point in slide["points"]:

            story.append(
                Paragraph(
                    f"• {point}",
                    styles["BodyText"]
                )
            )

        story.append(
            Spacer(1, 12)
        )

        story.append(
            Paragraph(
                "<b>Speaker Notes</b>",
                styles["Heading3"]
            )
        )

        story.append(
            Paragraph(
                slide["speaker_notes"],
                styles["BodyText"]
            )
        )

        story.append(
            PageBreak()
        )

    doc.build(story)

    return file_path