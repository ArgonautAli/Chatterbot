from urllib import response
from chatterbot import ChatBot
from requests import request

bot=ChatBot('A.R.G.U.S.',
            logic_adapters = [{
                'import_path': 'chatterbot.logic.BestMatch', 
                'default_response': 'I do not understand. I am still learning. Please contact alihaiderkhannews@gmail.com for further assistance.', 
                'maximum_similarity_threshold': 0.80
                
            }],
            read_only = True,
            preprocessor = ['chatterbot.preprocessors.clean_whitespace', 'chatterbot.preprocessors.unescape_html', 'maximum_preprocessors.convert_to_ascii']
            )

#running and getting a response

name = input('Enter your name: ')
print('Hi! I am A.R.G.U.S. A chabot! How can I help')

while True:

    request = input(name+': ')
    request = request.lower()
     
    if request == 'bye' or request== 'goodbye' or request== 'chal nikal' or request == 'see ya' or request == 'jaa lawde':
        print('A.R.G.U.S: ok bye bye')
        break
    else:
        response = bot.get_response(request)
        print('A.R.G.U.S.: ', response)

