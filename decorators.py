def add_borders(func):
    def wrap_function(*args, **kwargs):
        print("***************************")
        func(*args, **kwargs)
        print("***************************")
    return wrap_function

@add_borders
def print_welcome_message(message):
    print(message)

@add_borders
def print_goodbye_message(message: str, is_final: bool) -> None:
    print(message)
    if is_final:
        print("THE END!")

print_welcome_message("Welcome to the starry sky")
print_goodbye_message("So long, safe travels", True)
