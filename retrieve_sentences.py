import pandas as pd
from link_scraper import get_10qs, query_api
from html_to_text import *
import re
import random
import nltk
from nltk.collocations import *

random.seed(15)  # set rng seed for reproducibility
# nltk.download('punkt')#NEED TO download sentence parser (if not already done)


#Select random 10-q from list of all
all_urls = open('links.txt').read().splitlines()
num_urls = len(all_urls)
rand_url = random.randint(0, num_urls - 1)
url = all_urls[rand_url]

#Retrieve document
document = html_to_text(url)

#An example of retrieving sentences
sentences = nltk.sent_tokenize(document)
print(len(sentences))
num_good_sents = 0
good_sents = []
def check_for_formatting(string):
    #Ignore sentences with annoying syntax
    #TODO: figure out how to remove backslash and maybe also remove tabs?
    regex = re.compile('[☒_☐@#^&*()<>?/\|}{~:]|\s\s')
    if(regex.search(string) == None):
        return True

for sentence in sentences:
    if check_for_formatting(sentence):
        num_good_sents = num_good_sents+1
        good_sents.append(sentence)
        print(sentence)

print("Total acceptable sentences =",num_good_sents)
#Converting the sentences to a document
good_doc = " ".join(good_sents)

# DOESN'T work yet
# # Taken from https://stackoverflow.com/questions/2452982/how-to-extract-common-significant-phrases-from-a-series-of-text-entries
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# trigram_measures = nltk.collocations.TrigramAssocMeasures()
# finder = TrigramCollocationFinder.from_words(good_doc)
# finder.apply_freq_filter(3)
# print('Best Trigrams')
# print(finder.nbest(trigram_measures.pmi, 10))
# ## For looking at sentences
# # for counter in range(5):
# #     print(sentences[3+counter])

