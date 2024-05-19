list_one = [2, 8, 9, 4]


def get_value(index):
  try:
    print(list_one[index])
    return 0
  except Exception:
    print("Something went wrong")
    return 1
  finally:
    print("This is from finally")
  # print("This is from outside the try except block") # It has no effect so we use finally


print(get_value(2))