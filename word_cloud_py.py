# -*- coding: utf-8 -*-
"""Word_cloud.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e8QrhXFRmpBhyQlOn9A2A5o4WAjqnCmh
"""

#!pip install fileupload
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys
import fileupload
print('libraries imported')

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    non_punctuation_text=""
    for char in file_contents:
        if char not in punctuations:
            non_punctuation_text=non_punctuation_text+char
    words=non_punctuation_text.split()
    clean_words=[]
    frequencies={}

    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word]=1
        else:
            frequencies[alpha_word]+=1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display your wordcloud image
#path=r
#fo=open(path,'r')
#file_contents=fo.read()
file_contents="""Before you start, you will need Python on your computer.

Check whether you already have an up to date version of Python installed by entering python in a command line window. If you see a response from a Python interpreter it will include a version number in its initial display. Generally any Python 3.x version will do, as Python makes every attempt to maintain backwards compatibility within major Python versions. Python 2.x and Python 3.x are intentionally not fully compatible. If python starts a Python 2.x interpreter, try entering python3 and see if an up to date version is already installed.

On Windows, try py first - this is the relatively recent Python Launcher, which has a better chance of avoiding some of the path problems that might occur because on Windows programs don't install into any of the small set of common locations that are searched by default. The Python launcher can also let you select any of the various versions you may have installed from a single command.

If you need to install Python, you may as well download the most recent stable version. This is the one with the highest number that isn't marked as an alpha or beta release. Please see the Python downloads page for the most up to date versions of Python. They are available via the yellow download buttons on that page."""
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()