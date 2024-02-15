import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("The opposite of hot is")
print(response.text)  # cold.
