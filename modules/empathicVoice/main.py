#libaries

from empath import Empath
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import spacy

# text data cleanup-tokenize, lemmatize, remove stopwords, remove punctuation pipeline

# create empath class

class empath():
    lexicon = Empath()

    def get_empath(self, text, normalize=True):
        nlp = self.lexicon.analyze(text, normalize=normalize)
        return nlp

    def hot_topics(self, text):
        nlp = self.lexicon.analyze(text, normalize=True)
        for key, v in nlp.items():
            if v > 0.01:
                print(key, v)
    
    def map_dataframe(self, df):
        """
        maps empath analysis to dataframe with text content in each row.
        creates a column for each empath topic output and maps to score for each row of text.
        """
        def get_emp_cols(self, text):
            """
            Returns a list of empath topics for a given text in a dictionary. 
            Used to map a dataframe.
            """
            nlp = self.lexicon.analyze(text, normalize=True)
            keys = list(nlp.keys()) # get a list of the keys
            return keys

        def add_emp_cols(df):
            """
            add empath columns to df
            """
            emp_cols = get_emp_cols(df.content.iloc[1])
            for i in emp_cols:
                df[i] = df[i]=np.nan
            return df


        def apply_empath(df):
            """
            apply the empath analysis to each row of text in the df
            """
            for row in range(len(df.content)):
                content = df['content'].iloc[row]
                emp = self.lexicon.analyze(content, normalize=True)
                new_df = pd.DataFrame(emp, index=[0])
                new_df.insert(0, 'content', content)
                ind = df.iloc[[row]]
                new_df.index = ind.index
                df.update(new_df)
            return df