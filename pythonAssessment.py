import re 

# Open the file and read it into the article variable
with open("News Article for Python Assessment.txt", "r", encoding="utf-8") as file:
    article = file.read()


def count_specific_word(search_string, search_word):
    # Edge case: empty string should return 0
    if search_word == "":
        return 0
    else:
        words = re.findall(search_word.lower(), search_string.lower())
    
    return len(words)


def identify_most_common_word(str):
    # Edge case: empty string should return None
    if str == "":
        return None
    else:
        pattern = re.compile("[a-zA-Z]+")   
        words = re.findall(pattern, str.lower())

        # Dictionary for storing the words with the number of occurences
        article_words = {}
        for word in words:
            # if the word exists in the dictionary add to the number and if not add it to dictionary
            if word in article_words.keys():
                article_words[word] = article_words[word] + 1
            else:
                article_words[word] = 1

        # Loop through the dictionary and get the word list
        word_list = [(value, key) for (key, value) in article_words.items()]
        sorted_word_list = sorted(word_list, reverse=True)
        most_common_word = sorted_word_list[0]
        return most_common_word[1], most_common_word[0]


def calculate_average_word_length(str):
    # Edge case: empty string should return 0
    if str == "":
        return 0
    else:
        pattern = re.compile("[a-zA-Z]+")   
        words = re.findall(pattern, str.lower())

        # Dictionary for storing the words with the number of occurences
        article_words = {}
        for word in words:
            # if the word exists in the dictionary add to the number and if not add it to dictionary
            if word in article_words.keys():
                article_words[word] = article_words[word] + 1
            else:
                article_words[word] = 1

        word_sum = 0
        word_length_list = []
        for word in article_words.keys():
            word_sum += len(word)
            word_length_list.append(len(word))

        word_length_average = word_sum // len(word_length_list)
    
        return word_length_average


def count_paragraphs(str):
    # Edge case: empty string should return 1
    if str == "":
        return 1
    else:
        paragraphs = re.split(r'\n\s*\n', str)
        return len(paragraphs)


def count_sentences(str):
    # Edge case: empty string should return 1
    if str == "":
        return 1
    else:
        pattern = re.compile(r'[^.!?]+(?:[.!?]+|$)')
        sentences = re.findall(pattern, article)
        return len(sentences)

# Edge cases
print("Edge cases:")
print(f"The count of the specific word is {count_specific_word(article, "zoo")}")
print(f"Empty string for most common word count {identify_most_common_word("")}")
print(f"Empty average word length {calculate_average_word_length("")}")
print(f"Empty count paragraphs {count_paragraphs("")}")
print(f"Empty count sentences {count_sentences("")}")
print("\n")
print("Correct cases:")
print(f"The count of the specific word is {count_specific_word(article, "apple")}")
most_common_word, most_common_word_count = identify_most_common_word(article)
print(f"The most common word is '{most_common_word}' with {most_common_word_count} occurences.")
print(f"The average word length is {calculate_average_word_length(article)}")
print(f"There are {count_paragraphs(article)} paragraphs.")
print(f"There are {count_sentences(article)} sentences.")
