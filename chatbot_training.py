from msilib.schema import Directory
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import os

#To create a chatbot instance

bot = ChatBot('A.R.G.U.S.',
              logic_adapters = [{
                  'import_path': 'chatterbot.logic.BestMatch',
                  'default_response': 'I do not understand. I am still learning. Please contact alihaiderkhannews@gmail.com for further assistance.',
                  'maximum_similarity_threshold': 0.90
              }],
              read_only = True,
              preprocessors = ['chatterbot.preprocessors.clean_whitespace',
                               'chatterbot.preprocessors.unescape_html',
                               'chatterbot.preprocessors.convert_to_ascii']
              )

#To locate training folder
directory = 'training_data'

for filename in os.listdir(directory):
    if filename.endswith(".txt"): #put .txt at end of convo file
        print('\n Chatbot training with '+os.path.join(directory, filename)+'file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(bot)
        trainer.train(training_data)
    else:
        continue


decision = input('Train chatbot with English Corpus? (Y/N): ')

if decision == 'Y':
    print('\n Chatbot training with English corpus data')
    trainer_corpus = ChatterBotCorpusTrainer(bot)
    trainer_corpus.train('chatterbot.corpus.english')
