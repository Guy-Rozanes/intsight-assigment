class GistError(object):

    def __init__(self, message, documentation_url):
        self.message = message
        self.documentation_url = documentation_url

    @classmethod
    def from_json(cls, error_response):
        return cls(**error_response)


