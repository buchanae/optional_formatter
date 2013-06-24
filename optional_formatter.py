import string


__version__ = '0.1'


class FormatKeyError(Exception):
    def __init__(self, key):
        self.key = key


class OptionalFormatter(string.Formatter):

    def get_field(self, field_name, args, kwargs):
        try:
            return super(OptionalFormatter, self).get_field(field_name, args, kwargs)
        except FormatKeyError as e:
            return '{' + field_name + '}', e.key

    def get_value(self, key, args, kwargs):
        try:
            return super(OptionalFormatter, self).get_value(key, args, kwargs)
        except KeyError:
            raise FormatKeyError(key)


format = OptionalFormatter().format
