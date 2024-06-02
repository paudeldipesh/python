import re

pattern = r"[A-Z]here"
text = "Where is There."

# match_word = re.search(pattern, text)
# print(match_word)

match_words = re.finditer(pattern, text)
for word in match_words:
    print(word.span())
    print(text[word.span()[0] : word.span()[1]])

# Website: https://regexr.com/
