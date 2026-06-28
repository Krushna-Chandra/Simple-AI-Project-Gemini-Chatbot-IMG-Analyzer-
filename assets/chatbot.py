# now making it like real simple chatbot
## revise the way

import google.generativeai as genai
from dotenv import load_dotenv
import os




# load .env file
load_dotenv()
# now we have to get the api key configure it:
Api_key=os.getenv('API_KEY')
genai.configure(api_key = Api_key)
list(genai.list_models())
model_name = "gemini-2.5-flash"
Model = genai.GenerativeModel(model_name)
# response = Model.generate_content('Who are top five cricketers in India')
# we can use input way
while True:
    user_input=input('Enter your query: ')
    if user_input=='byy' or user_input=='exit':
        print("The you for talking with me, have a good day, byy byy!")
        break
    response = Model.generate_content(user_input)
    print(response.text)