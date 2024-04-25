country = "Nepal"
print(len(country))
print(country.upper())
print(country.lower())
print(country.replace("Ne", "Go"))
print(country)  # Strings are immutable

animal = "  Elephant  "
print(animal.strip())
pet = "??Dog??"
print(pet.lstrip("?"))
print(pet.rstrip("?"))

question = "How are you?"
print(question.split(" "))

blog_heading = "introduction to Python"
print(blog_heading.capitalize())
print(blog_heading.center(50))
print(blog_heading.count("o"))
print(blog_heading.startswith("in"))
print(blog_heading.endswith("on"))
print(blog_heading.endswith("du", 0, 7))
print(blog_heading.find("hello"))
print(blog_heading.index("trod"))
print(blog_heading.isalnum())
print(blog_heading.isalpha())  # Due to space character
print(blog_heading.islower())
print(blog_heading.isprintable())
print(blog_heading.title())

space_character = "    "
print(space_character.isspace())

title_text = "Hello Python In Nepal"
print(title_text.istitle())
print(title_text.isupper())
print(title_text.swapcase())