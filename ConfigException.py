class ConfigException(BaseException):
    pass


class InvalidPath(ConfigException):
    def __init__(self, message):
        self.message = message


class InvalidArgName(ConfigException):
    def __init__(self, message):
        self.message = message


class InvalidFirstArg(ConfigException):
    def __init__(self, message):
        self.message = message


class InvalidLastArg(ConfigException):
    def __init__(self, message):
        self.message = message