import streamlit as st
import pandas as pd
import plotly.express as px

from core.ai_engine import (
    generate_presentation_content,
    generate_presentation_from_document
)

from core.ppt_generator import create_presentation
from core.pdf_export import export_to_pdf
from core.file_parser import parse_uploaded_file

from core.project_manager import (
    save_project,
    load_projects
)

from core.dashboard import (
    get_dashboard_stats
)
st.markdown("""
# 🚀 AI Presentation Studio

### Create Professional Presentations in Seconds

Generate PowerPoint presentations and PDFs using AI.

- 📊 PPT Export
- 📄 PDF Export
- 🤖 Gemini AI
- 📁 Document Upload
- 🎨 Multiple Themes
""")
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Presentation Studio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.metric-card{
    padding:15px;
    border-radius:12px;
    background:#f5f5f5;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("⚙ Settings")

    generation_mode = st.radio(
        "Mode",
        [
            "Topic to PPT",
            "Document to PPT"
        ]
    )

    theme = st.selectbox(
        "Theme",
        [
            "Black Gold",
            "Corporate",
            "Startup Pitch",
            "Academic"
        ]
    )

    style = st.selectbox(
        "Presentation Style",
        [
            "Technical",
            "Business",
            "Research",
            "Marketing",
            "Educational"
        ]
    )

    slide_count = st.slider(
        "Slides",
        5,
        20,
        10
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 AI Presentation Studio")
st.caption(
    "Generate Professional PPTs using Gemini AI"
)

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

stats = get_dashboard_stats()

if stats["styles"]:

    fig = px.pie(
        names=list(stats["styles"].keys()),
        values=list(stats["styles"].values()),
        title="Presentation Styles Usage"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Projects",
        stats["projects"]
    )

with col2:
    st.metric(
        "Slides Generated",
        stats["slides"]
    )

st.divider()

# --------------------------------------------------
# TOPIC MODE
# --------------------------------------------------

if generation_mode == "Topic to PPT":

    topic = st.text_input(
        "Presentation Topic"
    )

    if st.button("Generate Presentation"):

        if not topic:
            st.warning(
                "Enter a topic first."
            )

        else:

            with st.spinner(
                "Generating presentation..."
            ):

                data = generate_presentation_content(
                    topic,
                    style,
                    slide_count
                )

                ppt_file = create_presentation(
                    topic,
                    data["slides"],
                    theme
                )

                pdf_file = export_to_pdf(
                    topic,
                    data["slides"]
                )

                save_project(
                    topic,
                    style,
                    slide_count,
                    ppt_file,
                    pdf_file
                )

            st.success(
                "Presentation Generated!"
            )

            col1, col2 = st.columns(2)

            with col1:

                with open(
                    ppt_file,
                    "rb"
                ) as file:

                    st.download_button(
                        "⬇ Download PPT",
                        file,
                        file_name=f"{topic}.pptx"
                    )

            with col2:

                with open(
                    pdf_file,
                    "rb"
                ) as file:

                    st.download_button(
                        "⬇ Download PDF",
                        file,
                        file_name=f"{topic}.pdf"
                    )

# --------------------------------------------------
# DOCUMENT MODE
# --------------------------------------------------

else:

    uploaded_file = st.file_uploader(
        "Upload PDF / DOCX / TXT",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        if st.button(
            "Generate from Document"
        ):

            with st.spinner(
                "Reading document..."
            ):

                document_text = parse_uploaded_file(
                    uploaded_file
                )

                data = generate_presentation_from_document(
                    document_text,
                    style,
                    slide_count
                )

                topic = uploaded_file.name

                ppt_file = create_presentation(
                    topic,
                    data["slides"],
                    theme
                )

                pdf_file = export_to_pdf(
                    topic,
                    data["slides"]
                )

                save_project(
                    topic,
                    style,
                    slide_count,
                    ppt_file,
                    pdf_file
                )

            st.success(
                "Presentation Generated!"
            )

            st.subheader("📑 Slide Preview")

            for i, slide in enumerate(data["slides"], start=1):

                with st.expander(
                    f"Slide {i}: {slide['title']}"
                ):

                    for point in slide["points"]:
                        st.write(f"• {point}")

                    st.caption(
                    slide["speaker_notes"]
                    )

            with open(
                ppt_file,
                "rb"
            ) as file:

                st.download_button(
                    "📊 Download PowerPoint",
                    file,
                    file_name=f"{topic}.pptx"
                )

# --------------------------------------------------
# HISTORY
# --------------------------------------------------

st.divider()

st.subheader("📂 Project History")

projects = load_projects()

if projects:

    for project in projects:

        with st.container():

            st.markdown(
                f"""
                ### 📂 {project['topic']}

                **Style:** {project['style']}

                **Slides:** {project['slide_count']}

                **Created:** {project['created_at']}
                """
            )

        st.divider()
else:

    st.info(
        "No projects generated yet."
    )

st.divider()

st.markdown("""
### ❤️ AI Presentation Studio

Built using:

- Streamlit
- Gemini AI
- Python-PPTX

Created by Sohail Khan
""")