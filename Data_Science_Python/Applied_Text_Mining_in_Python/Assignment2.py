'''Assignment 2 - Introduction to NLTK
In part 1 of this assignment you will use nltk to explore the Herman Melville novel Moby Dick. Then in 
part 2 you will create a spelling recommender function that uses nltk to find words similar to the 
misspelling.'''

'''Part 1 - Analyzing Moby Dick'''

import nltk
import pandas as pd
import numpy as np

nltk.download('punkt')
# If you would like to work with the raw text you can use 'moby_raw'
with open('moby.txt', 'r') as f:
    moby_raw = f.read()
    
# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)

#-----------------------------------------------------------------------
'''Example 1
How many tokens (words and punctuation symbols) are in text1?

This function should return an integer.'''

#---------- ANSWER CODE ----------
def example_one():
    
    return len(nltk.word_tokenize(moby_raw)) # or alternatively len(text1)

example_one()

#---------- ANSWER ----------
255038

#-----------------------------------------------------------------------
'''Example 2
How many unique tokens (unique words and punctuation) does text1 have?

This function should return an integer.'''

#---------- ANSWER CODE ----------
def example_two():
    
    return len(set(nltk.word_tokenize(moby_raw))) # or alternatively len(set(text1))

example_two()

#---------- ANSWER ----------
20742

#-----------------------------------------------------------------------
'''Example 3
After lemmatizing the verbs, how many unique tokens does text1 have?

This function should return an integer.'''

#---------- ANSWER CODE ----------
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

def example_three():

    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w,'v') for w in text1]

    return len(set(lemmatized))

example_three()

#---------- ANSWER ----------
16887

#-----------------------------------------------------------------------
'''Question 1
What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of 
tokens)

This function should return a float.'''

#---------- ANSWER CODE ----------
def answer_one():
    
    
    return len(set(moby_tokens))/len(moby_tokens)

answer_one()

#---------- ANSWER ----------
0.08132905684643073


#-----------------------------------------------------------------------
'''Question 2
What percentage of tokens is 'whale'or 'Whale'?

This function should return a float.'''

#---------- ANSWER CODE ----------
def answer_two():
    
    dist = nltk.FreqDist(text1)
    return (dist['whale']+ dist['Whale']) / len(moby_tokens)*100# Your answer here

answer_two()

#---------- ANSWER ----------
0.41248755087477157

#-----------------------------------------------------------------------
'''Question 3
What are the 20 most frequently occurring (unique) tokens in the text? What is their frequency?

This function should return a list of 20 tuples where each tuple is of the form (token, frequency). 
The list should be sorted in descending order of frequency'''

#---------- ANSWER CODE ----------
def answer_three():
    from collections import Counter
    dist = nltk.FreqDist(text1)
    return Counter(dist).most_common(20)
#     sorted_x = sorted(dist.items(), key=lambda kv: kv[1])
#     return sorted_x[::-1][:20]# Your answer here

answer_three()

#---------- ANSWER ----------
'''
[(',', 19204),
 ('the', 13715),
 ('.', 7306),
 ('of', 6513),
 ('and', 6010),
 ('a', 4545),
 ('to', 4515),
 (';', 4173),
 ('in', 3908),
 ('that', 2978),
 ('his', 2459),
 ('it', 2196),
 ('I', 2113),
 ('!', 1767),
 ('is', 1722),
 ('--', 1713),
 ('with', 1659),
 ('he', 1658),
 ('was', 1639),
 ('as', 1620)]'''

#-----------------------------------------------------------------------
'''Question 4
What tokens have a length of greater than 5 and frequency of more than 150?

This function should return an alphabetically sorted list of the tokens that match the above constraints. 
To sort your list, use sorted()'''

#---------- ANSWER CODE ----------
def answer_four():
    dist = nltk.FreqDist(text1)
    vocab1 = dist.keys()
    freq = [w for w in vocab1 if len(w) > 5 and dist[w] > 150]
    
    return sorted(freq)# Your answer here

answer_four()

#---------- ANSWER ----------
'''
['Captain',
 'Pequod',
 'Queequeg',
 'Starbuck',
 'almost',
 'before',
 'himself',
 'little',
 'seemed',
 'should',
 'though',
 'through',
 'whales',
 'without']'''

#-----------------------------------------------------------------------
'''Question 5
Find the longest word in text1 and that word's length.

This function should return a tuple (longest_word, length)'''

#---------- ANSWER CODE ----------
def answer_five():
    mt = np.array(list(set(moby_tokens)))
    lens = np.array([len(w) for w in mt])
    
    return mt[lens == np.max(lens)][0],np.max(lens)#lens[lens == np.max(lens)]# Your answer here

answer_five()

#---------- ANSWER ----------
("twelve-o'clock-at-night", 23)

#-----------------------------------------------------------------------
'''Question 6
What unique words have a frequency of more than 2000? What is their frequency?

"Hint: you may want to use isalpha() to check if the token is a word and not punctuation."

This function should return a list of tuples of the form (frequency, word) sorted in descending order of 
frequency.'''

#---------- ANSWER CODE ----------
def answer_six():
    unique = answer_three()
    answer = [(f,w) for w,f in unique if w.isalpha() and f>2000]
    return answer

answer_six()

#---------- ANSWER ----------
'''
[(13715, 'the'),
 (6513, 'of'),
 (6010, 'and'),
 (4545, 'a'),
 (4515, 'to'),
 (3908, 'in'),
 (2978, 'that'),
 (2459, 'his'),
 (2196, 'it'),
 (2113, 'I')]'''

#-----------------------------------------------------------------------
'''Question 7
What is the average number of tokens per sentence?

This function should return a float.'''

#---------- ANSWER CODE ----------
def answer_seven():
    sentences = nltk.sent_tokenize(moby_raw)
    sentence_token = np.array([len(nltk.word_tokenize(s)) for s in sentences])

    
    return sentence_token.mean()# Your answer here

answer_seven()

#---------- ANSWER ----------
25.886926512383273

#-----------------------------------------------------------------------
'''Question 8
What are the 5 most frequent parts of speech in this text? What is their frequency?

This function should return a list of tuples of the form (part_of_speech, frequency) sorted in descending 
order of frequency.'''

#---------- ANSWER CODE ----------
nltk.download('averaged_perceptron_tagger')
def answer_eight():
    from collections import Counter
    pos_tag = nltk.pos_tag(text1) #moby_tokens)
    tag = [t for p,t in pos_tag ]
    dist = nltk.FreqDist(tag)

    return Counter(dist).most_common(5)# Your answer here

answer_eight()

#---------- ANSWER ----------
[('NN', 32729), ('IN', 28663), ('DT', 25879), (',', 19204), ('JJ', 17613)]

#-----------------------------------------------------------------------
'''Part 2 - Spelling Recommender
For this part of the assignment you will create three different spelling recommenders, that each take a 
list of misspelled words and recommends a correctly spelled word for every word in the list.
For every misspelled word, the recommender should find find the word in correct_spellings that has the 
shortest distance*, and starts with the same letter as the misspelled word, and return that word as a 
recommendation.
*Each of the three different recommenders will use a different distance measure (outlined below).
Each of the recommenders should provide recommendations for the three default words provided: 
['cormulent', 'incendenece', 'validrate'].'''

from nltk.corpus import words
nltk.download('words')
correct_spellings = words.words()

#-----------------------------------------------------------------------
'''Question 9
For this recommender, your function should provide recommendations for the three default words provided above using the following distance 
metric:

Jaccard distance on the trigrams of the two words.

This function should return a list of length three: 
['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].'''

#---------- ANSWER CODE ----------
def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    
    dic = {}
    for entrie in entries:

        jd = [( word, 
                nltk.jaccard_distance(
                    set(nltk.ngrams(entrie,n=3)),
                    set(nltk.ngrams(word,n=3))
                )
              ) for word in correct_spellings if word[0] == entrie[0]
            ]
        dic[entrie] = pd.DataFrame(jd,columns =['word','jd'])
    
    answer = [dic[k][dic[k].jd==dic[k].jd.min()].word.values[0] for k in entries]
                        
    return answer # Your answer here
    
answer_nine()

#---------- ANSWER ----------
['corpulent', 'indecence', 'validate']

#-----------------------------------------------------------------------
'''Question 10
For this recommender, your function should provide recommendations for the three default words provided 
above using the following distance metric:

Jaccard distance on the 4-grams of the two words.

This function should return a list of length three: 
['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].'''

#---------- ANSWER CODE ----------
def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
     
    dic = {}
    for entrie in entries:

        jd = [( word, 
                nltk.jaccard_distance(
                    set(nltk.ngrams(entrie,n=4)),
                    set(nltk.ngrams(word,n=4))
                )
              ) for word in correct_spellings if word[0] == entrie[0]
            ]
        dic[entrie] = pd.DataFrame(jd,columns =['word','jd'])
    
    answer = [dic[k][dic[k].jd==dic[k].jd.min()].word.values[0] for k in entries]
                        
    return answer # Your answer here
    
answer_ten()

#---------- ANSWER ----------
['cormus', 'incendiary', 'valid']

#-----------------------------------------------------------------------
'''Question 11
For this recommender, your function should provide recommendations for the three default words provided 
above using the following distance metric:

Edit distance on the two words with transpositions.

This function should return a list of length three: 
['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].'''

#---------- ANSWER CODE ----------
def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
       
    dic = {}
        
    for entrie in entries:
        jd = [( word, 
                nltk.edit_distance(entrie, word)
              ) for word in correct_spellings if word[0] == entrie[0]
            ]
        dic[entrie] = pd.DataFrame(jd,columns =['word','jd'])
    
    answer = [dic[k][dic[k].jd==dic[k].jd.min()].word.values[0] for k in entries]
        
    return answer # Your answer here
    
answer_eleven()
#---------- ANSWER ----------
['corpulent', 'intendence', 'validate']
#-----------------------------------------------------------------------