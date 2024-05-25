import random
import string

message = input("Enter message: ")
words = message.split(" ")


def generate_random_string(length=3):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for iterator in range(length))


coding = input("1 for coding or 0 for decoding: ")
coding = True if coding == "1" else False
new_words = []

if coding:
    for word in words:
        random_one = generate_random_string()
        random_two = generate_random_string()
        if len(word) >= 3:
            word = word[1:] + word[0]
            word = random_one + word + random_two
            new_words.append(word)
        else:
            new_words.append(word[::-1])
    new_message = " ".join(new_words)

else:
    for word in words:
        if len(word) >= 3:
            word = word[3:-3]
            word = word[-1] + word[:-1]
            new_words.append(word)
        else:
            new_words.append(word[::-1])
    new_message = " ".join(new_words)

print(new_message)
