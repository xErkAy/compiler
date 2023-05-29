class LogicError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ImmutableError(Exception):
    message = 'Cannot assign to immutable variable <%s>'

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.message % self.name


class UnexpectedEndError(Exception):
    def __str__(self):
        return "Unexpected end of statement"


class UnexpectedTokenError(Exception):
    def __init__(self, token: str):
        self.token = token

    def __str__(self):
        return self.token

