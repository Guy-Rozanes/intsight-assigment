import pytest

from gist.entities.gists_file import GistFile
from tests.gist_api_tests.test_utils import get_all_user_gist_ids


@pytest.mark.sanity
@pytest.mark.functionality
def test_create_a_gist(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    result = gist_client.gists_action.create_a_gist(GistFile('abcd.txt', 'abcd'))

    assert result.status_code == 201
    assert result.content.files[0].filename == 'abcd.txt'

    assert result.content.id in get_all_user_gist_ids(gist_client)


@pytest.mark.functionality
def test_create_a_gist_with_empty_filename_will_generate_name(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    gist_file = GistFile('', 'abcd')
    result = gist_client.gists_action.create_a_gist(gist_file)
    assert result.status_code == 201
    assert result.content.files[0].filename != gist_file


@pytest.mark.functionality
def test_create_a_gist_with_same_filename(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    gist_file = GistFile('new.txt', 'abcd')
    gist_client.gists_action.create_a_gist(gist_file)
    result = gist_client.gists_action.create_a_gist(gist_file)

    assert result.status_code == 201
    assert result.content.files[0].filename == gist_file.get_file_name()


@pytest.mark.functionality
def test_create_a_gist_without_specify_files_will_throw_error(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    gist_file = GistFile('new.txt', 'abcd')
    gist_client.gists_action.create_a_gist(gist_file)
    result = gist_client.gists_action.create_a_gist(file=None)

    assert result.status_code == 422
    assert 'Invalid request' in result.error.message


@pytest.mark.functionality
@pytest.mark.parametrize('file_format', ['.txt', '.wav', '.bat'])
def test_create_a_gist_with_different_formats(create_authorized_gists_client_instance, file_format):
    gist_client = create_authorized_gists_client_instance
    gist_file = GistFile(f'new{file_format}', 'abcd')

    result = gist_client.gists_action.create_a_gist(gist_file)

    assert result.status_code == 201, result.content
    assert result.content.files[0].filename == gist_file.get_file_name()
