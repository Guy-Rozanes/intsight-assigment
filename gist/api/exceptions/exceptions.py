class GistApiException(Exception):
    pass


class GistApiInvalidResponse(GistApiException):
    pass


class GistGeneralFunctionalityError(GistApiException):
    pass
