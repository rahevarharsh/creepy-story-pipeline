import streamlit as st
import json

# Load JSON file (array of story objects)
with open("story.json", "r", encoding="utf-8") as fp:
    stories_data = json.load(fp)

st.set_page_config(page_title="Creepy Stories Dashboard", layout="wide")
st.title("🎬 Creepy Stories Dashboard")

# Sidebar to select story
story_names = [story.get("story_name", f"Story {i+1}") for i, story in enumerate(stories_data)]
selected_story_name = st.sidebar.selectbox("Select a story:", story_names)

# Get selected story
selected_story = next(story for story in stories_data if story.get("story_name") == selected_story_name)

# ===== STORY HEADER =====
st.markdown("## Story Overview")
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader(selected_story.get("story_name", ""))
    st.write(selected_story.get("description", ""))
with col2:
    st.metric("🔥 Viral Chance", f"{int(selected_story.get('viral_chance', 0)*100)}%")

st.markdown("---")

# ===== VIRAL TAGS =====
st.markdown("## 🔖 Viral Tags")
tags = selected_story.get("viral_tags", [])
st.write(", ".join([f"`{tag}`" for tag in tags]))

# ===== FULL SCRIPT =====
st.markdown("## 📝 Full Script")
st.text_area("Script", value=selected_story.get("full_script", ""), height=300)

st.markdown(f"""`Total words` :{len(selected_story.get("full_script", "").split(" "))}""")
st.markdown("---")

# ===== IMAGE PROMPTS =====
st.markdown("## 🖼️ Image Prompts")
image_prompts = selected_story.get("image_prompts", [])
for i, prompt in enumerate(image_prompts, 1):
    st.info(f"{i}. {prompt}")

st.markdown("---")

# ===== VIDEO EFFECTS =====
st.markdown("## 🎥 Video Effect Prompts")
video_effects = selected_story.get("video_effect_prompts", [])
for i, effect in enumerate(video_effects, 1):
    st.warning(f"{i}. {effect}")

st.markdown("---")

# ===== EDITING & MUSIC =====
st.markdown("## ✂️ Editing Suggestions")
st.write(selected_story.get("editing_suggestions", ""))

st.markdown("## 🎶 Background Music")
st.write(selected_story.get("background_music", ""))

# ===== SHORTS TITLE =====
st.markdown("## 🎞️ Shorts Title")
st.write(selected_story.get("shorts_title", ""))
