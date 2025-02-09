class InvalidTimeException(Exception):
    """Thrown when the Time class has an issue with a value"""
    def __init__(self, message):
        super().__init__(message)

class NegativeTimeException(InvalidTimeException):
    """We don't like negative times"""
    def __init__(self):
        super().__init__("Negative times are not supported")


class DataError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DataInputError(DataError):
    """Thrown when checking a data stream if there's something abnormal"""
    def __init__(self, file, reason):
        super().__init__(f"<ERROR> In file `{file}`: {reason}")

class DataReadError(DataError):
    """Thrown when there is an error with the data post-input.
    This is quite serious, as some data may have already been read and inserted, making the clean up messy"""
    def __init__(self, file, reason):
        super().__init__(f"<ERROR> In file `{file}`: {reason}")

class NoDataError(DataError):
    """Thrown when we try to access data that doesn't exist"""
    def __init__(self, file, reason):
        super().__init__(f"<ERROR> In file `{file}`: {reason}")