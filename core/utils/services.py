import random
import string
from oauthlib.common import generate_client_id, UNICODE_ASCII_CHARACTER_SET


class BaseHashGenerator(object):
    def hash(self):
        raise NotImplementedError()


class IDGenerator(BaseHashGenerator):
    def __init__(self, lng):
        self.lng = lng

    def hash(self):
        return generate_client_id(length=self.lng, chars=UNICODE_ASCII_CHARACTER_SET)


def id_generator(lng=16):
    generator = IDGenerator(lng)
    return generator.hash()


def get_random_string(length=10, starts_with='', ends_with=''):
    letters = string.ascii_lowercase
    return (starts_with + ''.join(random.choice(letters) for _ in range(length)) + ends_with).title()
