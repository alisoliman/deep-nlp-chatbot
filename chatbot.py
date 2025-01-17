"""
Creating a chatbot that uses NLP Deep Learning
@author: alisoliman
"""

# Importing libraries
import tensorflow as tf
import numpy as np
import re
import time


# Importing the dataset
lines = open('movie_lines.txt', encoding='UTF-8', errors='ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding='UTF-8', errors='ignore').read().split('\n')


# Creating a dictionary that maps each line to its ID
id2line = {}

for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]
        
        
# Creating a list of all the conversation lists
conversation_ids = []

for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversation_ids.append(_conversation.split(','))
    

# Creating a list of questions and a list of answers
questions = []
answers = []
for conversation in conversation_ids:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        

# Doing a first cleaning for the texts
def clean_text(text):
    text = text.lower() # Change the text to lower case
    text = re.sub(r"i'm","i am",text)
    text = re.sub(r"he's","he is",text)
    text = re.sub(r"she's","she is",text)
    text = re.sub(r"it's","it is",text)
    text = re.sub(r"that's","that is",text)
    text = re.sub(r"what's","what is",text)
    text = re.sub(r"where's","where is",text)
    text = re.sub(r"\'ll"," will",text)
    text = re.sub(r"\'ve"," have",text)
    text = re.sub(r"\'re"," are",text)
    text = re.sub(r"\'d"," would",text)
    text = re.sub(r"won't","will not",text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]","",text)
    return text


# Cleaning the questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))
    
# Cleaning the answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))   
    
    
# Creating a dictionary that maps each word and it's number of occurences
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1


# Creating two dictionaries that map the questions words and the answers words to a unique integer
threshold = 20
questionswords2int = {}
word_number = 0
for word, count in word2count.items():
    if count >= threshold:
        questionswords2int[word]= word_number
        word_number += 1
answerswords2int = {}
word_number = 0
for word, count in word2count.items():
    if count >= threshold:
        answerswords2int[word]= word_number
        word_number += 1
    
    
    
# Adding the last tokens to these two dictionaries
tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
for token in tokens:
    questionswords2int.append[token] = len(questionswords2int) + 1
    answerswords2int.append[token] = len(answerswords2int) + 1
    
    
    
    
    
    
    
    
    
    
    