# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:18:43 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 24 2018
Description:
    In this file, I have defined a class that will perform the basic preprocessing on each input text.
    This class have one instance variable which is a list that holds the individual tokends of the entire text,
    as a result of applying the tokenise() method defined in this class.
"""

class Preprocessor:
    def __init__(self):
        self.tokenlist = []
    
    def __str__(self):
        answer = 'The total number of tokens is: \n'
        # Readbale format print
        if any(self.tokenlist):
            return answer + str(len(self.tokenlist))
        else:
            return 'There is no token. The total number is 0.'
       
    def tokenise(self, input_sequence):
        file_handle = open(input_sequence, 'r') # Open the exact book file.
        for line in file_handle:
            self.tokenlist.append(line) # Read in lines
        file_handle.close() # Close the file
        
    def get_tokenised_list(self):
        if any(self.tokenlist):
            return self.tokenlist

