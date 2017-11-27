class Error(Exception):
    """
    Base class for errors.
    """
    def __init__(self, code, title, details, href):
        """
        Initializes and error object
        @type  code: string
        @param code: The code of the error.
        @type  title: string
        @param title: The title of the error.
        @type  details: string
        @param details: The description of the error.
        @type  code: string
        @param code: The link to more information about of the error.
        """
        self.code = code
        self.title = title
        self.details = details
        self.href = href

class InvalidInputError(Error):
    """
    Error class for invalid input type.
    @type  message: string
    @param message: The custom message of the error.
    """
    def __init__(self, message):
        code = 'ERR-0001'
        title = 'Invalid Parameter Exception'
        details = message
        href = 'http://example.com/docs/errors/#ERR-0001'

        super(InvalidInputError, self).__init__(code, title, details, href)

class NotFoundError(Error):
    def __init__(self, message):
        """
        Error class for record not found.
        @type  message: string
        @param message: The custom message of the error.
        """
        code = 'ERR-0002'
        title = 'Record Not Found Exception'
        details = message
        href = 'http://example.com/docs/errors/#ERR-0002'

        super(NotFoundError, self).__init__(code, title, details, href)
