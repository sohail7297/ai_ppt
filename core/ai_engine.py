# core/ai_engine.py

from google import genai
from config import GEMINI_API_KEY
import json
import re

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_presentation_content(topic, style, slide_count):

    prompt = f"""
Create a professional presentation.

Topic: {topic}
Style: {style}
Slides: {slide_count}

Return ONLY valid JSON.

Format:

{{
  "slides":[
    {{
      "title":"Slide Title",
      "points":[
        "point 1",
        "point 2",
        "point 3",
        "point 4"
      ],
      "speaker_notes":"Detailed explanation"
    }}
  ]
}}

Generate exactly {slide_count} slides.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        text = match.group()

    return json.loads(text)


def generate_summary(topic):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Write a professional summary about {topic}."
    )

    return response.text


def generate_image_prompt(title, points):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Generate a professional image prompt.

Title:
{title}

Points:
{points}
"""
    )

    return response.text


def generate_presentation_from_document(
        document_text,
        style,
        slide_count
):

    prompt = f"""
Create a professional presentation from the
following document.

DOCUMENT:

{document_text[:12000]}

STYLE:
{style}

SLIDES:
{slide_count}

Return JSON in the format:

{{
 "slides":[
   {{
      "title":"",
      "points":[],
      "speaker_notes":""
   }}
 ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    import re
    import json

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if match:
        text = match.group()

    try:
        return json.loads(text)
    except Exception as e:
        raise Exception(
            f"AI returned invalid JSON.\n\n{text[:500]}"
        )