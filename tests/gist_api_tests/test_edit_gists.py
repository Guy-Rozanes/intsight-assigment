import pytest

from gist.entities.gists_file import GistFile


@pytest.mark.sanity
@pytest.mark.functionality
def test_edit_gist_description(create_gist_with_deletion):
    gist_client, gist = create_gist_with_deletion
    result = gist_client.gists_action.edit_a_gist_by_gist_id(gist.id, description='new_description')
    assert result.status_code == 200
    assert result.content.description == 'new_description'


@pytest.mark.functionality
def test_edit_gist_files(create_gist_with_deletion):
    gist_client, gist = create_gist_with_deletion
    last_file = gist.files[0].filename
    result = gist_client.gists_action.edit_a_gist_by_gist_id(gist.id, files=GistFile('new.txt', 'edit txt'))
    assert result.status_code == 200
    file_names = {file.filename for file in result.content.files}
    assert file_names == {'new.txt', last_file}


@pytest.mark.functionality
def test_edit_non_existing_gist(create_authorized_gists_client_instance):
    client = create_authorized_gists_client_instance
    result = client.gists_action.edit_a_gist_by_gist_id('non-existing', description='new')
    assert result.status_code == 404
    assert result.error.message == 'Not Found'


@pytest.mark.functionality
def test_edit_empty_description(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    result = client.gists_action.edit_a_gist_by_gist_id(gist.id, description='')
    assert result.status_code == 200
    assert result.content.description == ''
