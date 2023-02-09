import pandas as pd 
import regex
import matplotlib.pyplot as plt
import googletrans


def most_common_words(df):
    #find the 50 most common words
    words = df["Town-Village Name"].value_counts().head(50).index.tolist()
    return words

df = pd.read_csv("census_data_towns_and_vilalges.csv")

def town_name_origin(df, ending):
    l1 = df.find_words(df["Town-Village Name"].tolist(), ending)
    #remove the ending from all words in l1
    l2 = [word[:-len(ending)] for word in l1]
    #print first 10 words in l2 and l1
    print(l1[:10])
    print(l2[:10])

        
def what_language(s):
    #detect the language of s
    return googletrans.Translator().detect(s).lang

def find_language(lan):
    if what_language(lan) == "ar" or "ur" or "fa":
        return False
    return True

#create a new dataframe that is a copy of df but with a column that is the language of the town name
df["Language"] = df["Town-Village Name"].head(100).apply(what_language)

print(df.head(100))
        