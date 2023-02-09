import pandas as pd 
import regex
import matplotlib.pyplot as plt


#from a list of words, find the 50 most common series of letters that appear at the end of the word
def find_common_letters(words):
    endings = []
    for word in words:
        #find the last 50 characters of the word
        word = word[-50:]
        #find the last series of letters in the word
        word = regex.findall(r"[a-zA-Z]+$", word)
        #if there are any letters, add them to the list
        if len(word) > 0:
            endings.append(word[0])
    #find the 50 most common series of letters
    endings = pd.Series(endings).value_counts().head(50).index.tolist()
    return endings

endings = find_common_letters(pd.read_csv("census_data_towns_and_vilalges.csv")["Town-Village Name"].tolist())
#remove duplicates
endings = list(dict.fromkeys(endings))
print(endings)

#for each ending in endings, find the number of words that end with that ending
def find_endings(words, endings):
    endings_count = []
    for ending in endings:
        count = 0
        for word in words:
            if word.endswith(ending):
                count += 1
        endings_count.append(count)
    return endings_count

endings_count = find_endings(pd.read_csv("census_data_towns_and_vilalges.csv")["Town-Village Name"].tolist(), endings)

#for each ending in ending, return a list of words that end with that ending
def find_words(words, endings):
    words_endings = []
    for ending in endings:
        words_ending = []
        for word in words:
            if word.endswith(ending):
                words_ending.append(word)
        words_endings.append(words_ending)
    return words_endings

words_endings = find_words(pd.read_csv("census_data_towns_and_vilalges.csv")["Town-Village Name"].tolist(), endings)

#on a graph, plot the number of words that end with each ending, but only for the 10 most common endings
plt.bar(endings[:10], endings_count[:10])

#save the graph
plt.savefig("endings.png")

plt.show()



