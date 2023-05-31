import prompt_formats as pf
import openai
import os

from dotenv import load_dotenv, find_dotenv  # need local .env file
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = pf.evaluation_text 
