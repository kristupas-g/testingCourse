import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def get_random_email():
    rand_str = get_random_string(12)
    return rand_str + "@gmail.com"
