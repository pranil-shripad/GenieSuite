import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")  # put in Railway env vars

def generate_title(content, style="catchy", model="meta-llama/llama-3-8b-instruct"):
    style_instruction = {
        "catchy": "Generate a catchy and attention-grabbing title.",
        "SEO-friendly": "Generate an SEO-optimized title.",
        "professional": "Generate a clear and professional title.",
        "funny": "Generate a humorous and witty title.",
        "mysterious": "Generate a curious and mysterious title."
    }

    prompt = f"""{style_instruction[style]}

Text:
{content}

Only return the generated title. No quotes or explanations.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://yourdomain.com",  # replace later
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
