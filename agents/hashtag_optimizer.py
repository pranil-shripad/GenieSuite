import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_hashtags(content, model="meta-llama/llama-3-8b-instruct"):
    prompt = f"""
Based on the following content, generate 5 to 10 relevant and trending hashtags for social media (Instagram, YouTube, X). Do not include the '#' symbol — just return them comma-separated.

Content:
{content}

Only return the hashtags separated by commas. No explanations.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://instacontentai.up.railway.app/",  # Replace this later
        "X-Title": "Smart Content Tools"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content'].strip()
        else:
            return f"[Error {res.status_code}] {res.text}"
    except Exception as e:
        return f"[Connection Error] {str(e)}"
