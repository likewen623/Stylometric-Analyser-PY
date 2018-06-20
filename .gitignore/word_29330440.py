# -*- coding: utf-8 -*-
"""
Created on Tue May 22 03:01:35 2018
Name: Kewen Deng
Student ID: 29330440
Last modified date: May 24 2018
Description:
    In this task, the class is defined for analysing the number of occurrences for each word from a given tokenised list.
    
"""

class WordAnalyser:     
    def __init__(self):
        import pandas as pd
        pd.options.mode.chained_assignment = None
        self.df = pd.DataFrame(columns = ['word', 'total', 'length'])
        
    def __str__(self):    
        output = 'The occurrences for each word are: \n'
        answer = ''
        # Readbale format print
        for value in range(self.df.shape[0]):
            answer += str(self.df.word[value]) + '\t' + ':' + str(self.df.total[value]) + '\n'
        # If no occurrence, show error message.
        if answer != '':
            return output + answer
        else:
            return 'No words occurrence.'
    
    def analyse_words(self, tokenised_list):
        punctuations = ['.', ',', '?', '!']
        for tokens in tokenised_list:
            word = ''
            # Replace punctuations
            for punctuation in punctuations:
                tokens = tokens.replace(punctuation, '')
            tokens = tokens + ' '
            
            for letter in tokens:
                exist = False # Judge the word exists or not
                if letter != ' ':
                    word = word + letter
                else:
                    if len(self.df) > 0 :
                        for key in range(len(self.df)):
                            if self.df.word[key] == word: # If the word is in dataframe, add count.
                                self.df.total[key] += 1
                                exist = True
                                break
                    if exist == False and word !='': # If the word is not in dataframe, add new word and new count.
                        self.df.loc[len(self.df)] = {'word':word, 'total':1, 'length':0}
                    word = ''
        self.df = self.df.sort_values(by='word') 
                
    def get_stopword_frequency(self):
        # Initialization and predefined stopword
        import pandas as pd
        stopwords = ['about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'just', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'quite', 'rather', 'really', 'right', 'right', 'room', 'rooms', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'very', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours']
        self.dfstop = pd.DataFrame(stopwords, columns = ['stopword'])
        self.dfstop['total'] = '0'
        # Get length of the stopwords and save them in the dataframe of stopwords
        for key1 in range(len(self.df)):
            for key2 in range(len(self.dfstop)):
                if self.df.word[key1] == self.dfstop.stopword[key2]:
                    self.dfstop.total[key2] = self.df.total[key1]
                    break
        return self.dfstop
    
    def get_word_length_frequency(self):
        # Initialization
        import pandas as pd
        self.dflength = pd.DataFrame(columns = ['length'])
        self.dflength['length_count'] = 0
        # Get length of the words and save them in the dataframe of words
        for key in range(len(self.df)):
            self.df.length[key] = len(self.df.word[key])
            exist = False
            if len(self.dflength) >0 :
                for i in range(len(self.dflength)):
                    if self.dflength.length[i] == len(self.df.word[key]):
                        self.dflength.length_count[i] += 1
                        exist = True
                        break
            if exist == False:
                self.dflength.loc[len(self.dflength)] = {'length':len(self.df.word[key]), 'length_count':1}
        self.dflength = self.dflength.sort_values(by='length') 
        return self.dflength
