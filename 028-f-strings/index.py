sentence = "{} is a good {}"
name = "Dipesh"
profession = "programmer"

print(sentence.format(name, profession))

letter = "{1} is the {0} guy"
print(letter.format(profession, name))

print(f"{name} is a good {profession}")

text = "For only {price:.2f} dollars"
print(text.format(price=49.0999))

price = 5.123456
print(f"The {{price}} is {price:.2f}")