from openai import OpenAI
import openai
from django.conf import settings

print(settings.OPENAPI_KEY)
client = OpenAI(api_key=settings.OPENAPI_KEY) 

def get_response(context):
    # try:
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{context}"}]
    )
    return chat_completion.choices[0].message.content
    # except:
    #     raise ValueError(f"OpenAI API returned an Some Error")
    
