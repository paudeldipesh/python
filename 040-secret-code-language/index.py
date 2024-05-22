# Write a Python program to translate a message into secret code language.
# Use the rules below to translate normal English into secret code language:

# Coding:
#  - If the word contains at least 3 characters:
#      - Remove the first letter and append it to the end.
#      - Append three random characters at the beginning and the end.
#  - Else:
#      - Simply reverse the string.

# Decoding:
#  - If the word contains less than 3 characters:
#      - Reverse the string.
#  - Else:
#      - Remove 3 random characters from the start and end.
#      - Remove the last letter and append it to the beginning.

# Your program should ask whether you want to code or decode the message.