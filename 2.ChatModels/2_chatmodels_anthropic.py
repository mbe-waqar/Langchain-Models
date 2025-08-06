from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "text-davinci-003", api_key = os.getenv("API_KEY"))

result = model.invoke("what is the meaning of life")

print(result.content)