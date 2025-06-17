import requests
import json

def generate_title(content, style="catchy", model="llama3.2"):
    prompt = f"""Generate a {style} title for the following content:

{content}

Only return the title, no explanations.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True
        )

        if response.status_code == 200:
            title = ""
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            title += data["response"]
                    except json.JSONDecodeError:
                        continue
            return title.strip()
        else:
            return f"[Error] Status {response.status_code}: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"[Connection Error] {e}"
