# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:39:41 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 24 2018
Description:
    This file tests all the classes defined before.
    I have defined a function called main() that will drive the flow of execution of the program.
    Below are the import part of other classes and the sequence of tasks that execute within the main() function. 

"""
import os # Work directory
work_path = 'D:/Desktop/FIT9133-ASS3'
os.chdir(work_path) # Change work directory

import pandas as pd

from preprocessor_29330440 import Preprocessor as Preprocessor
from character_29330440 import CharacterAnalyser as CharacterAnalyser
from word_29330440 import WordAnalyser as WordAnalyser
from visualiser_29330440 import AnalysisVisualiser as AnalysisVisualiser



def main(userinput_list):
    userinput_list = read_input
    
    # Initialization
    character_list = []
    punctuation_list = []
    stopword_list = []
    length_list = []
    
    
    # Process different books in Task1-Task3 one by one
    for userinput in userinput_list:
        my_Preprocessor = Preprocessor()
        file = userinput
        my_Preprocessor.tokenise(file + '.tok')
        tokenised_list = my_Preprocessor.get_tokenised_list()
        
        my_CharacterAnalyser = CharacterAnalyser()
        my_CharacterAnalyser.analyse_characters(tokenised_list)
        character_frequency = my_CharacterAnalyser.get_character_frequency()
        punctuation_frequency = my_CharacterAnalyser.get_punctuation_frequency()
        character_list = character_list + [character_frequency]
        punctuation_list = punctuation_list + [punctuation_frequency]
        
        my_WordAnalyser = WordAnalyser()
        my_WordAnalyser.analyse_words(tokenised_list)
        stopword_frequency = my_WordAnalyser.get_stopword_frequency()
        stopword_list = stopword_list + [stopword_frequency]
        word_length_frequency = my_WordAnalyser.get_word_length_frequency()
        length_list = length_list + [word_length_frequency]
        
        print(userinput, ' processed! \n')
        
        
    # Print output into .csv files
    dfcharacter = pd.DataFrame(columns=['character']) 
    for i in character_list:
        dfcharacter = pd.merge(dfcharacter, i, how = 'outer',on='character')
    dfcharacter.columns = ['character'] + userinput_list
    for i in userinput_list:
#        dfcharacter[i] = dfcharacter[i].astype('int64')
        dfcharacter[i] = dfcharacter[i] / dfcharacter[i].sum()
    dfcharacter.to_csv(r'./character.csv', index=False, sep=',')
    print('Character printed! \n')
    
    dfpunctuation = pd.DataFrame(columns=['punctuation']) 
    for i in punctuation_list:
        dfpunctuation = pd.merge(dfpunctuation, i, how = 'outer',on='punctuation')
    dfpunctuation.columns = ['punctuation'] + userinput_list
    for i in userinput_list:
#        dfpunctuation[i] = dfpunctuation[i].astype('int64')
        dfpunctuation[i] = dfpunctuation[i] / dfpunctuation[i].sum()
    dfpunctuation.to_csv(r'./punctuation.csv', index=False, sep=',')
    print('Punctuation printed! \n')

    dfstopword = pd.DataFrame(columns=['stopword']) 
    for i in stopword_list:
        dfstopword = pd.merge(dfstopword, i, how = 'outer',on='stopword')
    dfstopword.columns = ['stopword'] + userinput_list
    for i in userinput_list:
        dfstopword[i] = dfstopword[i].astype('int64')
        dfstopword[i] = dfstopword[i] / dfstopword[i].sum()    
    dfstopword.to_csv(r'./stopword.csv', index=False, sep=',')
    print('Stopword printed! \n')

    dflength = pd.DataFrame(columns=['length']) 
    for i in length_list:
        dflength = pd.merge(dflength, i, how = 'outer',on='length')
    dflength.columns = ['length'] + userinput_list
    for i in userinput_list:
#        dflength[i] = dflength[i].astype('int64')
        dflength[i] = dflength[i] / dflength[i].sum() 
    dflength.to_csv(r'./length.csv', index=False, sep=',')
    print('Word length printed! \n')
    
    # Plot pictures and save them
    analysis_output = [dfcharacter, dfpunctuation, dfstopword, dflength]
    my_AnalysisVisualiser = AnalysisVisualiser(analysis_output, userinput_list)
    my_AnalysisVisualiser.visualise_character_frequency()
    my_AnalysisVisualiser.visualise_punctuation_frequency()
    my_AnalysisVisualiser.visualise_stopword_frequency()
    my_AnalysisVisualiser.visualise_word_length_frequency()
    print('Pictures saved! \n')

def read_input():
    # Initialization
    booknames = ['Edward_II_Marlowe', 'Hamlet_Shakespeare', 'Henry_VI_Part1_Shakespeare', 'Henry_VI_Part2_Shakespeare', 'Jew_of_Malta_Marlowe', 'Richard_II_Shakespeare']
    bookcount = [0]*6
    output = []
    
    # Keep reading input until all the 6 books have been entered
    while sum(bookcount) < 6:
        inputdesc = ''
        for i in range(len(booknames)):
            if bookcount[i] == 0 :
                inputdesc = inputdesc + '\n' + booknames[i]
        
        userinput = input('Please input any of the following books :' + inputdesc + '\n================== \n')        
        for i in range(len(booknames)) :
            if booknames[i] == userinput and bookcount[i] == 0:
                bookcount[i] += 1
                output = output + [userinput]
                break
            if booknames[i] == userinput and bookcount[i] == 1:
                print('This book exists! \n')
                break
            if i == len(booknames)-1 and booknames[i] != userinput:
                print('Invalid input! \n')
    print('Please wait for the output! It might take a long time ... \n')
    return output
                
if __name__ == '__main__':
    main(read_input())
        
        