import json

from gist.api.base_gist_api import BaseGistApi
from gist.api.conf.conf import GISTS_HOST
from gist.api.exceptions.exceptions import GistGeneralFunctionalityError, GistApiInvalidResponse
from gist.api.response_entities.gist_custom_response import GistCustomResponse
from gist.api.response_entities.models import Models
from http_client.http_client import HttpClient
from http_client.entities.http_method import Method


class GistsActions(BaseGistApi):
    BASE_URL = GISTS_HOST + "/gists"

    def __init__(self, access_token):
        super().__init__(access_token)
        self._http_client = HttpClient()

    def get_gists_list(self, public=False, since=None, per_page=None, page=None):
        headers = self._headers
        params = {}
        if public:
            headers = {}
        if page:
            params['page'] = page

        if per_page:
            params['per_page'] = per_page

        if since:
            params['since'] = since

        result = self._http_client.send_request(self.BASE_URL, Method.GET, headers=headers, params=params)
        return GistCustomResponse(result, Models.GIST)

    def create_a_gist(self, file, description=None, public=None):
        file = file.to_json() if file else None
        data_content = {'files': file}
        if description:
            data_content['description'] = description
        if public is not None:
            data_content['public'] = public
        result = self._http_client.send_request(self.BASE_URL, Method.POST,
                                                data=json.dumps(data_content),
                                                headers=self._headers)
        return GistCustomResponse(result, Models.GIST)

    def delete_a_gist_by_gist_id(self, gist_id):
        delete_url = f'{self.BASE_URL}/{gist_id}'
        result = self._http_client.send_request(delete_url, Method.DELETE, headers=self._headers)
        return GistCustomResponse(result, None)

    def edit_a_gist_by_gist_id(self, gist_id, description=None, files=None):
        body = {}
        if files:
            body['files'] = files.to_json()

        if description is not None:
            body['description'] = description

        edit_url = f'{self.BASE_URL}/{gist_id}'
        result = self._http_client.send_request(edit_url, Method.PATCH, headers=self._headers, data=json.dumps(body))

        return GistCustomResponse(result, Models.GIST)

    def star_a_gist_by_gist_id(self, gist_id):
        star_url = f'{self.BASE_URL}/{gist_id}/star'
        result = self._http_client.send_request(star_url, Method.PUT, headers=self._headers)
        return GistCustomResponse(result, None)

    def get_all_starred_gists(self):
        star_url = f'{self.BASE_URL}/starred'
        result = self._http_client.send_request(star_url, Method.GET, headers=self._headers)
        return GistCustomResponse(result, Models.GIST)

    def get_latest_commit_sha_by_gist_id(self, gist_id):
        all_commits_url = f'{self.BASE_URL}/{gist_id}/commits'
        result = self._http_client.send_request(all_commits_url, Method.GET, headers=self._headers)
        try:
            latest_sha = result.content[0]['version']
        except KeyError:
            if result.status_code == 404:
                raise GistGeneralFunctionalityError('Gist is not exist please enter existing gist id')

            raise GistApiInvalidResponse('Commits response has been changed, version key is not exist')
        return latest_sha

    def get_latest_revision_of_gist_by_gist_id(self, gist_id, custom_sha=None):
        sha = ""
        if not custom_sha:
            sha = self.get_latest_commit_sha_by_gist_id(gist_id)
            if not sha:
                raise GistGeneralFunctionalityError('There is not a commits of this specific gist')
        else:
            sha = custom_sha
        revision_url = f'{self.BASE_URL}/{gist_id}/{sha}'
        result = self._http_client.send_request(revision_url, Method.GET, headers=self._headers)
        return GistCustomResponse(result, Models.GIST)
