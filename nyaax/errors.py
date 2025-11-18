class NyaaXError(Exception):
    """ Base NyaaX error """


class FormatterError(NyaaXError):
    """ Base Formatter error """


class InvalidCategory(FormatterError):
    """ Invalid category error """


class InvalidSubcategory(FormatterError):
    """ Invalid subcategory error """


class InvalidPage(FormatterError):
    """ Invalid page error """


class ExtractionError(NyaaXError):
    """ Base Extraction error """


class NoResultsFound(ExtractionError):
    """ No results found error """


class UnexpectedError(ExtractionError):
    """ Unexpected error """
    def __init__(self, exc: BaseException, error_msg: str):
        self.exc = exc
        super().__init__(error_msg)
