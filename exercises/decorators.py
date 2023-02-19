# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(user):
        if user['valid']:
            fn(user)
        else:
            print("User is not authenticated")

    return wrapper

@authenticated
def message_friends(user):
    print(f"Message has been sent, sender: {user['name']}")

message_friends(user1)
