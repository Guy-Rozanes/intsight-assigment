from gist.api.gists_actions import GistsActions


class GistClient(object):

    def __init__(self, access_token=None):
        self.gists_action = GistsActions(access_token)

