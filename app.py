import streamlit as st
from agents.title_generator import generate_title
from agents.summarizer import summarize_content
from agents.hashtag_optimizer import generate_hashtags

if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

FREE_LIMIT = 3


st.set_page_config(page_title="🧠 Smart Content Tools", layout="centered")
st.title("🧠 Smart Content Agent Bundle")

tabs = st.tabs(["🎯 Title Generator", "📝 Content Summarizer", "🏷️ Hashtag Optimizer"])

# === Title Generator Tab ===
with tabs[0]:
    st.subheader("🎯 Title Generator")
    content = st.text_area("Enter content to generate a title:", height=200)
    style = st.selectbox("Choose a style", ["catchy", "SEO-friendly", "professional", "funny", "mysterious"])
    
    if st.button("Generate Title"):
        if st.session_state.usage_count < FREE_LIMIT:
            if content.strip():
                with st.spinner("Generating title..."):
                    title = generate_title(content, style)
                    st.session_state.usage_count += 1
                    st.success(title)
            else:
                st.warning("Please enter content.")
        else:
            st.warning("⚠️ You’ve reached the free limit. Upgrade for unlimited use.")
            st.markdown("[🔓 Unlock Full Access](https://your-gumroad-link)", unsafe_allow_html=True)

# === Summarizer Tab ===
with tabs[1]:
    st.subheader("📝 Content Summarizer")
    long_text = st.text_area("Paste your long content here:", height=300)
    style = st.selectbox("Choose summary style", ["paragraph", "bullet-points"])

    if st.button("Summarize Content"):
        if st.session_state.usage_count < FREE_LIMIT:
            if long_text.strip():
                with st.spinner("Summarizing..."):
                    summary = summarize_content(long_text, style=style)
                    st.session_state.usage_count += 1
                    with st.expander("📝 Summary Output", expanded=True):
                        st.markdown(summary, unsafe_allow_html=True)
            else:
                st.warning("Please enter some content to summarize.")
        else:
            st.warning("⚠️ You’ve reached the free limit. Upgrade for unlimited use.")
            st.markdown("[🔓 Unlock Full Access](https://your-gumroad-link)", unsafe_allow_html=True)

# === Hashtag Optimizer Tab ===
with tabs[2]:
    st.subheader("🏷️ Hashtag Optimizer")
    caption = st.text_area("Paste your caption, description, or short content:", height=200)

    if st.button("Generate Hashtags"):
        if st.session_state.usage_count < FREE_LIMIT:
            if caption.strip():
                with st.spinner("Generating hashtags..."):
                    hashtags = generate_hashtags(caption)
                    st.session_state.usage_count += 1
                    st.markdown("### 📌 Suggested Hashtags")
                    st.code(hashtags, language="markdown")
            else:
                st.warning("Please enter some content.")
        else:
            st.warning("⚠️ You’ve reached the free limit. Upgrade for unlimited use.")
            st.markdown("[🔓 Unlock Full Access](https://your-gumroad-link)", unsafe_allow_html=True)
