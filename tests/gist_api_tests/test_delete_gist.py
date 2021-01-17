import pytest


@pytest.mark.sanity
@pytest.mark.functionality
def test_delete_a_gist(create_gist):
    client, gist_entry = create_gist
    result = client.gists_action.delete_a_gist_by_gist_id(gist_entry.id)
    assert result.status_code == 204
    all_gists = client.gists_action.get_gists_list().content
    all_ids = [gist.id for gist in all_gists]
    assert gist_entry.id not in all_ids


@pytest.mark.functionality
def test_delete_non_existing_gist(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    result = gist_client.gists_action.delete_a_gist_by_gist_id('non-existing')
    assert result.status_code == 404


@pytest.mark.functionality
def test_delete_public_gist(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    result = gist_client.gists_action.get_gists_list(public=True)
    public_gist_id = result.content[0].id

    deletion_result = gist_client.gists_action.delete_a_gist_by_gist_id(public_gist_id)
    assert deletion_result.status_code == 404
    assert deletion_result.error.message == 'Not Found'
