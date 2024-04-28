number = int(input("Enter a number: "))

match number:
  case 0:
    print("Number is zero")

  case 4:
    print("Number is four")

  case _ if number / 7 == 1:
    print("Number is seven")

  case _:
    print("Number dosen't match")