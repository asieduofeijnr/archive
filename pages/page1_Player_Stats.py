import streamlit as st

st.set_page_config(
    page_title="MSDS_NBA_GROUP_34",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)


images = ["Eric/peric2.png", "Eric/peric1.png", "Eric/eric5.png"]

current_image_index = st.session_state.get("current_image_index", 0)

st.image(
    images[current_image_index],
    caption=f"Page {current_image_index + 1}",
    use_column_width=True,
)

if st.button("Next Image"):
    current_image_index = (current_image_index + 1) % len(images)
    st.session_state.current_image_index = current_image_index
