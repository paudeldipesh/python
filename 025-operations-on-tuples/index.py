countries = ("Spain", "Italy", "China", "India", "Germany")
modified_countries = ("Nepal", "Bangladesh") + countries[1:]
print(modified_countries)

fruits_one = ("Banana", "Apple")
fruits_two = ("Orange", "Mango", "Apple")
fruits_tuple = fruits_one + fruits_two
print(fruits_tuple)
print(fruits_tuple.count("Apple"))
print(fruits_tuple.index("Mango", 1, 4))