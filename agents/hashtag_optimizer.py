import requests
import json

def generate_hashtags(content, model="llama3.2"):
    prompt = f"""
You are a social media expert. Based on the following content, generate a list of 5 to 10 relevant and trending hashtags. Do not include explanations. Only output the hashtags, separated by spaces or new lines.

Content:
{content}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True
        )

        if response.status_code == 200:
            output = ""
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            output += data["response"]
                    except json.JSONDecodeError:
                        continue

            # Cleanup: Remove leading "#" if needed, split, and reformat
            hashtags = [tag.strip(" #") for tag in output.replace("\n", " ").split()]
            unique_tags = sorted(set(filter(lambda x: x, hashtags)))
            return "\n".join(f"#{tag}" for tag in unique_tags)

        else:
            return f"[Error] Status {response.status_code}: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"[Connection Error] {e}"
