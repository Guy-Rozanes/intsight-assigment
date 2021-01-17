class BaseGistApi(object):

    def __init__(self, access_token):
        if access_token:
            self._headers = {'accept': 'application/vnd.github.v3+json',
                             "Authorization": f'token {access_token}'}
        else:
            self._headers = {'accept': 'application/vnd.github.v3+json'}
