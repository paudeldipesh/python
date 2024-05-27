def greet(function):
    def modified_function(*args, **kwargs):
        print("Good Morning!")
        function(*args, **kwargs)
        print("Thanks for using this function!")

    return modified_function


@greet  # Easy way to use greet(hello)()
def hello():
    print("Hello!")


hello()


@greet  # Easy way to use greet(add)(arg_one, arg_two)
def add(a, b):
    print(a + b)


add(7, 8)
