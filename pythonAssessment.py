import re 

# Open the file and read it into the article variable
with open("News Article for Python Assessment.txt", "r", encoding="utf-8") as file:
    article = file.read()


# Most commond word
pattern = re.compile("[a-zA-Z]+")   
words = re.findall(pattern, article.lower())
# print(words)

# Dictionary for storing the words with the number of occurences
article_words = {}
for word in words:
    if word in article_words.keys():
        article_words[word] = article_words[word] + 1
    else:
        article_words[word] = 1

word_list = [(value, key) for (key, value) in article_words.items()]


sorted_word_list = sorted(word_list, reverse=True)

most_common_word = sorted_word_list[0]
# print(most_common_word[1])

def count_specific_word(str1, str2):
    # Edge case: empty string should return 0
    return

def identify_most_common_word(str):
    # Edge case: empty string should return None
    
    return

def calculate_average_word_length(str):
    # Edge case: empty string should return 0
    return

def count_paragraphs(str):
    # Edge case: empty string should return 1
    return

def count_sentences(str):
    # Edge case: empty string should return 1
    return