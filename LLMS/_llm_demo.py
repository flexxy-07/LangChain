from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
  model="gemini-1.5-flash",
  google_api_key=api_key
)
result = llm.invoke(
  "Whats your stand on yorichi as the best waifu ?"
)

print(result.content)