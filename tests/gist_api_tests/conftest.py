import pytest
from gist.api.conf.conf import ACCESS_TOKEN
from gist.api.gists_client import GistClient
from gist.entities.gists_file import GistFile


@pytest.fixture(scope='module')
def create_authorized_gists_client_instance():
    return GistClient(ACCESS_TOKEN)


@pytest.fixture(scope="module")
def create_unauthorized_gists_client_instance():
    return GistClient()


@pytest.fixture
def create_gist(create_authorized_gists_client_instance):
    gist_file_example = GistFile(file_name='test.txt', content='abcdefg')
    client = create_authorized_gists_client_instance
    result = client.gists_action.create_a_gist(gist_file_example)

    return client, result.content


@pytest.fixture
def create_gist_with_deletion(create_authorized_gists_client_instance, request):
    gist_file_example = GistFile(file_name='test.txt', content='abcdefg')
    client = create_authorized_gists_client_instance
    result = client.gists_action.create_a_gist(gist_file_example)

    def clean_gist():
        client.gists_action.delete_a_gist_by_gist_id(result.content.id)

    request.addfinalizer(clean_gist)

    return client, result.content
