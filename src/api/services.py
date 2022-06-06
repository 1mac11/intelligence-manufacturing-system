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
