class GistFile(object):

    def __init__(self, filename, type, language, raw_url, size, truncated=None, content=None):
        self.filename = filename
        self.type = type
        self.language = language
        self.raw_url = raw_url
        self.size = size
        self.truncated = truncated
        self.content = content

    @classmethod
    def from_json(cls, response):
        return cls(**response)
