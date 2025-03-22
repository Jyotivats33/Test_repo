import os

import openai
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from openai import OpenAI
load_dotenv()

#api_key = os.environ.get("OPENAI_API_KEY")
# model = ChatOpenAI(model="gpt-4", api_key= API_KEY)
# res = model.invoke("What is an AI")
client = OpenAI(

    api_key=os.environ.get("API_KEY"),
)
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "what is AI"}
    ],
)

print(completion.choices[0].message.content)