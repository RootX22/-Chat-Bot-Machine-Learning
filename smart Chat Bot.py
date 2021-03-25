# description : this is  smart   Chat Bot Using Python & Machine Learning
# import lib
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Download  the  Punkt Packege
nltk.download('punkt', quiet=True)

# Get The Article  Packege
article = Article(
    'https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text

# Print The Article text
# print(corpus)

# Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)  # A list of  sentences


# Print the  list of sentences
# print(sentence_list)


# A  function to return random greeting  responses  to aa  users greeting
def Greeting_response(tsxt):
    text = text.lower()

    # Bots greeting responses
    boot_greeting = ['howdy', 'hi', 'hey', 'hello', 'hola']
    # users greeting
    user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(boot_greeting)

# function of  index  Packege


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

                return list_index


#  create the  bots  responses
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similary_score = cosine_similarity(cm[-1], cm)
    similary_score_list = similary_score.flatten()
    index = index_sort(similary_score_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similary_score_list[index[i]] < 0.0:
            bot_response = bot_response + ''+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response + ''+"I apologize, I don't understant. "

    sentence_list.remove(user_input)

    return bot_response


# Note  that now  we start  the smart  chat  command
print('Doc Bot : I am  Doctor  Bot  or  Doc  Bot for  short . I will answer your question about chronic kidney Disease If you to  exit, type bye.')

exit_list = ['exit', 'see you later ', 'bye', 'quit']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc Bot : Chat with you later !')
        break
    else:
        if Greeting_response(user_input) != None:
            print('Doc Bot : ' + Greeting_response(user_input))
