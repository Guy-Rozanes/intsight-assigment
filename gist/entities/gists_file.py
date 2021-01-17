class GistFile(object):

    def __init__(self, file_name, content):
        self._file_name = file_name
        self._content = content

    def to_json(self):
        return {
            self._file_name: {
                'content': self._content
            }
        }

    def get_file_name(self):
        return self._file_name

    def get_file_content(self):
        return self._content
