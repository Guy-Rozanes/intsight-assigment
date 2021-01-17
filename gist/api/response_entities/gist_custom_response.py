from gist.api.conf.conf import ERROR_STATUS_CODES
from gist.api.exceptions.exceptions import GistApiInvalidResponse
from gist.api.response_entities.error import GistError


class GistCustomResponse(object):

    def __init__(self, http_response, model):
        self.error = None
        self.status_code = http_response.status_code
        try:
            if self.status_code in ERROR_STATUS_CODES:
                self.error = GistError.from_json(http_response.content)
                self.content = http_response.content
            else:
                if not model:
                    self.content = http_response.content
                else:
                    if isinstance(http_response.content, list):
                        self.content = [model.from_json(item) for item in http_response.content]
                    else:
                        self.content = model.from_json(http_response.content)

        except GistApiInvalidResponse:
            self.content = http_response.content
