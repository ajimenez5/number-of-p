'''
Created on Feb 17, 2018

@author: ITAUser
'''
num_words = 0
num_char = 0;

fname = "constituton.txt"
f=open(fname,"r+")


for line in f: 
    words=line.split()
    num_words = len(words) + num_words
    for word in words: 
        word.count("p")
        num_char = word.count("p") + num_char
        
print(num_char); 
