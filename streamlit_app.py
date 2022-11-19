import sys
from pathlib import Path
import streamlit as st
from demos import orchestrator


file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

from demos import orchestrator

# Create opening page
def draw_main_page():
    st.write(
        f"""
        # Surprise 2022! 👋
        """
    )
    st.write("intro")
    st.write("release_notes")

# Dict with all pages
demo_pages = {
    "Start": draw_main_page,
    "Tabletje... Tabletje": orchestrator.show_examples,
    "test2": orchestrator.show_examples,
}




# Draw sidebar
pages = list(demo_pages.keys())

if len(pages):
    # Add title to side bar
    st.sidebar.title(f"Surprise 2022 🎈")

    selected_demo = st.sidebar.radio("", pages, key="Start")


# Draw main page
if selected_demo in demo_pages:
    demo_pages[selected_demo]()
