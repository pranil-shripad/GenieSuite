import requests
import json
import re

def summarize_content(content, style="paragraph", model="llama3.2"):
    style_instruction = {
        "paragraph": "Summarize the following content in 3 to 5 sentences.",
        "bullet-points": "Summarize the following content as bullet points (3 to 5 points)."
    }

    prompt = f"""{style_instruction[style]}

{content}

Only return the summary. No explanations or introductions.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True
        )

        if response.status_code == 200:
            summary = ""
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            summary += data["response"]
                    except json.JSONDecodeError:
                        continue

            if style == "bullet-points":
                # Use regex to split by bullet and clean each point
                parts = re.split(r"[•\-*]\s*", summary)
                lines = []
                for part in parts:
                    cleaned = part.strip()
                    if cleaned:
                        lines.append(f"• {cleaned}")
                return "\n".join(lines)
            else:
                return summary.strip()

        else:
            return f"[Error] Status {response.status_code}: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"[Connection Error] {e}"
