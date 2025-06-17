import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

def summarize_content(content, style="paragraph", model="meta-llama/llama-3-8b-instruct"):
    instructions = {
        "paragraph": "Summarize the following content in 3 to 5 clear sentences.",
        "bullet-points": "Summarize the following content in 3 to 5 bullet points. Start each point on a new line with '•'."
    }

    prompt = f"""{instructions[style]}

Content:
{content}

Only return the summary. No explanations or introductions.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://your-deployed-app-url",  # Replace this later
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
