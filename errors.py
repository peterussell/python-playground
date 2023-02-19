while True:
    try:
        age = int(input("What is your age? "))
        sub_age = 10 / age
    except ValueError as err:
        print(f"Age must be a number: {err}") # Age must be a number: invalid literal for int() with base 10: 'asdf'
    except ZeroDivisionError as err:
        print(f"Age must be higher than 0: {err}")
    else:
        print("Thanks!")
        print(f"Your age is {age}")
        break
    finally:
        print("Finally called -- all done!")

# Raising errors...
# raise ValueError("Kill it with fire")
# raise Exception("I'm a general exception, let's get out of here!")