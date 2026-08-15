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


# Average word length 
word_sum = 0
word_length_list = []
for word in article_words.keys():
   word_sum += len(word)
   word_length_list.append(len(word))

print(word_length_list)
print("List length", len(word_length_list))
print("Word sum", word_sum)
word_length_average = word_sum // len(word_length_list)
print("Word length average", word_length_average)


# Count paragraphs
paragraphs = re.split(r'\n\s*\n', article)
# paragraphs = re.findall(pattern, article)
print(len(paragraphs))

# Count sentences
pattern = re.compile(r'[^.!?]+(?:[.!?]+|$)')
sentences = re.findall(pattern, article)
# print(sentences)
print(len(sentences))

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