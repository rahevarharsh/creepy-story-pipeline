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
st.markdown( f""" {selected_story.get("full_script", "")}""")

st.markdown(f"""`Total words` :{len(selected_story.get("full_script", "").split(" "))}""")
st.markdown("---")

# ===== IMAGE PROMPTS =====
st.markdown("## 🖼️ Image Prompts")
# Ensure selected_story is defined before using it

image_prompts = selected_story.get("image_prompts", []) 
if "style" not in st.session_state:
    if st.button("madhubani style"):
        st.session_state.style = "madhubani"

    
for i, prompt in enumerate(image_prompts, 1):
    if "style" not in st.session_state:
        st.markdown(f"```text\nGenerate visuals using this prompt template:{prompt[2:]}, drawn in a dark, cinematic cartoon style, with heavy shadows, dramatic lighting, night-time setting, detailed linework, and an eerie, surreal atmosphere. Inspired by adult animated shows and noir comics. Subtle neon glow, slightly distorted facial expressions, thick outlines, VHS effect, muted colors, and vintage textures. Stylized background with twilight skies, mysterious environments, and emotional tension. 4K, highly detailed, digital painting. Aspect ratio 9:16\n```")
    elif "style" in st.session_state:
        st.markdown(f"""```text\n{prompt[2:]}, illustrated in a Madhubani folk-art style blended with dark cinematic cartoon aesthetics. Flat color planes, dense decorative patterns, double black outlines, and traditional motifs (lotus, fish, peacock, vines) integrated into characters and environment. Night-time atmosphere with dramatic lighting, heavy shadows, subtle neon glow, and slightly distorted facial expressions for a surreal, eerie tone. Background filled with symbolic Madhubani details and stylized elements of Bengal folklore (temples, riverbanks, terracotta walls, monsoon sky). Thick outlines, detailed linework, muted earthy palette with occasional neon accents, VHS grain, vintage textures. Emotional tension in composition: [CAMERA ANGLE], [ACTION MOMENT], [FACIAL EXPRESSION]. Decorative border framing the scene with traditional motifs. 4K, highly detailed, digital painting, aspect ratio 9:16.\n```""")
else:
    st.warning("selected_story is not defined.")


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
