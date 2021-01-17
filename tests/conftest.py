from gist.api.conf.conf import ACCESS_TOKEN
from gist.api.gists_client import GistClient


def pytest_sessionfinish(session, exitstatus):
    client = GistClient(ACCESS_TOKEN)
    gists_result = client.gists_action.get_gists_list()
    for gist in gists_result.content:
        client.gists_action.delete_a_gist_by_gist_id(gist.id)
