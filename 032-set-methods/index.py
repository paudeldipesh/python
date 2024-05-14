set_one = {1, 2, 3, 4}
set_two = {4, 5, 6, 7}
print(set_one.union(set_two))
print(set_one.intersection(set_two))
print(set_one.symmetric_difference(set_two))
print(set_one.difference(set_two))
# set and the set_method_update, update the set that is passed as an argument
print(set_one.isdisjoint(set_two))
print(set_one.issuperset(set_two))
print(set_two.issubset(set_one))

set_countries = {"India", "Pakistan", "Nepal", "Bangladesh"}
set_countries.add("China")
set_countries.remove("Bangladesh")
print(set_countries)
print(set_countries.pop())
print(set_countries.clear())

info = {"Dipesh", "Python Django Developer", 23, True}
if "Python Django Developer" in info:
  print("Yes")