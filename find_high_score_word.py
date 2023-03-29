# Assignment 2
from alphabets import alphabet_values # import alphabet_values() from alphabets module

def high_score_word(input_string): # define a function to take input as an argument
    values = alphabet_values() # assign the json value to values json
    word_score = [] # create an empty word_value list
    list_of_words = input_string.split() # store the input string in term of list of words
    print(list_of_words) # print the words list
    for word in list_of_words: # looping over list_of_words and itterate over each word
        score = score_of_word(word,values) # vall schore_of_word function to get the score of each word
        word_score.append(score) # append the score to the word_score list
    max_score = max(word_score) # using mx function get the maximum score in the word_score list
    index_no = word_score.index(max_score) # get the index number of the max_score
    print('highest scoring word is : '+list_of_words[index_no]) # print the highest scoring word from the sentence to the console

def score_of_word(word,values): # define the score_of_word function that takes word and values json as input parameters
    value = 0 # initialise value to 0
    for char in word: # looping on the word and itterating on each character 'char'
        value = value + values[char] # add value of the character to value variable and store in value
    return value # return value which will have score of the word

high_score_word(input('Enter the string (containing only alphabets , in smaller case)to check : ')) # call high_score_word method and as the user to enter the string in console