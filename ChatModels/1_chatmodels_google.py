from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# NOTES : Temperature is a parameter that controls the randomness 
#         of languauge model's output. It affects how creative or 
#         creative or deterministic the responses are.

# Factual ans(math,code,facts) : 0.0 - 0.3
# Balanced response(general QA, explainations) : 0.5 - 0.7
# Creative writing, storytelling, jokes : 0.9 - 1.2
# Maximum randomness(wild, ideas, brainstorming) : 1.5+

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')

result = model.invoke("What is the capital of India")

print(result.content)