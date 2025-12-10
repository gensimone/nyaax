class NyaaXError(Exception):
    """ Base NyaaX error """


class NoResultsFound(NyaaXError):
    """ No results found error """


class UnexpectedError(NyaaXError):
    """ Unexpected error """
    def __init__(self, exc: BaseException, error_msg: str):
        self.exc = exc
        super().__init__(error_msg)
