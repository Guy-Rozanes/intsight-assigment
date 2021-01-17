import requests

from http_client.entities.http_method import Method
from http_client.entities.http_response import HttpResponse


def _verify_params(params):
    if not params:
        return {}
    else:
        return params


def _verify_headers(headers):
    if not headers:
        return {}
    else:
        return headers


class HttpClient(object):

    def send_request(self, url, method, body=None, data=None, params=None, headers=None):
        params = _verify_params(params)
        headers = _verify_headers(headers)

        result = None
        if method == Method.GET:
            result = requests.get(url, params=params, headers=headers)

        elif method == Method.POST:
            result = self._post_method(url, body, data, params, headers)

        elif method == Method.PUT:
            result = self._put_method(url=url, body=body, data=data, params=params, headers=headers)

        elif method == Method.DELETE:
            result = self._delete_method(url=url, body=body, data=data, params=params, headers=headers)

        elif method == Method.PATCH:
            result = self._patch_method(url=url, body=body, data=data, params=params, headers=headers)

        return HttpResponse(result)

    def _post_method(self, url, body=None, data=None, params=None, headers=None):
        if data:
            return requests.post(url=url, data=data, params=params, headers=headers)
        elif body:
            return requests.post(url=url, json=body, params=params, headers=headers)

    def _put_method(self, url, body, data, params, headers):
        if data:
            return requests.put(url=url, data=data, params=params, headers=headers)
        elif body:
            return requests.put(url=url, json=body, params=params, headers=headers)
        else:
            return requests.put(url=url, params=params, headers=headers)

    def _delete_method(self, url, data, body, params, headers):
        if data:
            return requests.delete(url=url, data=data, params=params, headers=headers)
        elif body:
            return requests.delete(url=url, json=body, params=params, headers=headers)
        else:
            return requests.delete(url=url, params=params, headers=headers)

    def _patch_method(self, url, data, body, params, headers):
        if data:
            return requests.patch(url=url, data=data, params=params, headers=headers)
        elif body:
            return requests.patch(url=url, json=body, params=params, headers=headers)
