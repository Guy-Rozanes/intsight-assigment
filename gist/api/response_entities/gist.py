from gist.api.exceptions.exceptions import GistApiInvalidResponse
from gist.api.response_entities.gist_file import GistFile


class Gist(object):

    def __init__(self, response):
        try:
            self.url = response["url"]
            self.forks_url = response["forks_url"]
            self.commits_url = response["commits_url"]
            self.id = response["id"]
            self.node_id = response["node_id"]
            self.git_pull_url = response["git_pull_url"]
            self.git_push_url = response["git_push_url"]
            self.html_url = response["html_url"]
            self.created_at = response["created_at"]
            self.updated_at = response["updated_at"]
            self.description = response["description"]
            self.comments = response["comments"]
            self.commits_url = response["comments_url"]
            self.files = [GistFile.from_json(content) for filename, content in response["files"].items()]
        except KeyError:
            raise GistApiInvalidResponse('Response syntax has been changed')

    @classmethod
    def from_json(cls, response):
        return cls(response)
