import openai
import os
from contexts import pizza_shop_context

class OpenAITools:
    def __init__(self):
        self.context = []
        self.model = "gpt-3.5-turbo"
        self.client = None
    
    def set_api_key(self, api_key):
        os.environ['OPENAI_API_KEY'] = api_key
        self.client = openai.OpenAI()

    def set_model(self, model):
        self.model = model

    def get_completion(self, prompt, temperature=0):
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content

    def get_completion_from_messages(self, messages, temperature=0):
        print(self.model)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content

    def set_context(self, store_type):
        try:
            self.context = eval(self.get_completion(f"create a prompt like this ```{pizza_shop_context}``` but for {store_type}, ensure it has the same format"))
            return self.context, "", f"Your {store_type} order bot is ready"
        except:
            return [], "", f"There is somenthing wrong with your Open AI API key"

        
    #     print(str(response.choices[0].message))
        return response.choices[0].message.content