import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

APP_NAME = "AI Presentation Studio"

APP_ICON = "🚀"

GENERATED_PPT_DIR = "generated/ppt"
GENERATED_PDF_DIR = "generated/pdf"
GENERATED_IMG_DIR = "generated/images"

HISTORY_FILE = "history/projects.json"

SUPPORTED_FILES = [
    "pdf",
    "docx",
    "txt"
]

THEMES = {
    "Black Gold": {
        "primary": "#FFD700",
        "background": "#111111"
    },
    "Corporate": {
        "primary": "#1565C0",
        "background": "#FFFFFF"
    },
    "Academic": {
        "primary": "#2E7D32",
        "background": "#FFFFFF"
    },
    "Startup Pitch": {
        "primary": "#8E24AA",
        "background": "#FFFFFF"
    }
}