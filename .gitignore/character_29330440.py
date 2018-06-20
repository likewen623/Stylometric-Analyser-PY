# -*- coding: utf-8 -*-
"""
Created on Tue May 22 00:39:59 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 24 2018
Description:
    In this task, the class is defined for analysing the number of occurrences for each character from a given tokenised list,
    including any letter, numerals, and punctuations.
"""

class CharacterAnalyser:
    def __init__(self):
        import pandas as pd
        pd.options.mode.chained_assignment = None
        # Build A-Z and 0-9 to be keys in Dictionary
        cha = []
        for i in range(65,91):
            cha.append(chr(i))
        for i in range(0,10):
            cha.append(str(i))
        # Put A-Z and 0-9 (keys) and counts(values) to DataFrame
        self.df = pd.DataFrame(cha, columns = ['character'])
        self.df['cha_count'] = 0
        # Put punctuations to DataFrame
        self.dfpun = pd.DataFrame([',', '.', '?', '!', ';', ':', '\'', '-'], columns = ['punctuation'])
        self.dfpun['pun_count'] = 0
    
    def __str__(self):
        output = 'The occurrences for each character are: \n'
        answer = ''
        # Readbale format print
        for value in range(self.df.shape[0]):
            answer += str(self.df.character[value]) + '\t' + ':' + str(self.df.cha_count[value]) + '\n'
        # If no occurrence, show error message.
        if answer != '':
            return output + answer
        else:
            return 'No characters occurrence.'
        
    def analyse_characters(self, tokenised_list):
        for token in tokenised_list:
            for letter in token:
                # Find the charater in dataframe and add count
                for key in range(self.df.shape[0]):
                    if letter.upper() == self.df.character[key]:
                        self.df.cha_count[key] += 1
                        break
                # Find the punctuations in dataframe and add count
                for key in range(self.dfpun.shape[0]):
                    if letter == self.dfpun.punctuation[key]:
                        self.dfpun.pun_count[key] += 1
    
    def get_character_frequency(self):
        if any(self.df):
            return self.df 
    
    def get_punctuation_frequency(self):
        if any(self.dfpun):
            return self.dfpun     
        
