# -*- coding: utf-8 -*-
"""
Created on Tue May 22 07:29:26 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 24 2018
Description:
    In this task, the calss is defined for visualising the stylometic analysis.
    I haved defined a number of methods in this class to present four stylistic features for each of the six input texts that I have analysed through the methods provided in classes from Task 2 and Task 3.
"""

class AnalysisVisualiser:
    def __init__(self, all_text_stats, bookname_list):
        import pandas as pd
        pd.options.mode.chained_assignment = None
        self.all_text_stats = all_text_stats
        self.booknames_list = bookname_list
        
    # Plot the different frequencies of charactets
    def visualise_character_frequency(self):    
        import matplotlib.pyplot as plt
        df = self.all_text_stats[0]
        df.plot(kind = 'line', y= self.booknames_list, x = 'character') # Use line plot to show the result
        plt.savefig("character.png")
    
    # Plot the different frequencies of punctuations       
    def visualise_punctuation_frequency(self):    
        import matplotlib.pyplot as plt
        df = self.all_text_stats[1] 
        df.plot(kind = 'line', y= self.booknames_list, x = 'punctuation') # Use line plot to show the result
        plt.savefig("punctuation.png")

    # Plot the different frequencies of stopword        
    def visualise_stopword_frequency(self):    
        import matplotlib.pyplot as plt
        df = self.all_text_stats[2]
        df.plot(kind = 'line', y= self.booknames_list, x = 'stopword') # Use line plot to show the result
        plt.savefig("stopword.png")      

    # Plot the different frequencies of word length        
    def visualise_word_length_frequency(self):    
        import matplotlib.pyplot as plt
        df = self.all_text_stats[3]
        df.plot(kind = 'bar', y= self.booknames_list, x = 'length') # Use bar plot to show the result
        plt.savefig("word_length.png")    
        
        


