import openai as ai
import os

__name__ = "__main__"

def chat_with_ai(question,username):

  if __name__ == "__main__":
    ai.api_key = os.environ.get('openai_TOKEN') 
    completion = ai.Completion()

    start_chat_log = """Human: Hello, I am """+str(username).split('#')[0]+'.'+"""AI: Hello, human I am ColdiBOT.
    """

    prompt = f"{start_chat_log}Human: {question}\nAI:"

    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.7,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=1,max_tokens=10,stop = "\nHuman: ",n=1)

    return response.choices[0].text

