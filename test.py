import google.generativeai as genai

genai.configure(api_key="AIzaSyB7Y68ObTZWb3Zx43nHL0Nwe8NRmX94keE")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("What is the capital of India?")
print(response.text)
