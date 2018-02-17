'''
Created on Feb 3, 2018

@author: ITAUser
'''

filename = "number.txt"
numberfile=open("number.txt", "r+");


numberline = 0;
numberwords = 0;
numberchara = 0;

for line in numberfile: 
    words = line.split();
    
    numberline = numberline +1;
    numberwords = len(words);
    numberchara = len()
