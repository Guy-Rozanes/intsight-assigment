import pytest


@pytest.mark.sanity
@pytest.mark.functionality
def test_latest_revision(create_gist_with_deletion):
    gist_client, gist = create_gist_with_deletion
    result = gist_client.gists_action.get_latest_revision_of_gist_by_gist_id(gist.id)
    assert result.status_code == 200
    assert result.content.id == gist.id


@pytest.mark.functionality
def test_latest_revision_for_non_existing_gist(create_authorized_gists_client_instance):
    gist_client = create_authorized_gists_client_instance
    result = gist_client.gists_action.get_latest_revision_of_gist_by_gist_id(gist_client, custom_sha='not_exist')
    assert result.status_code == 404
    assert result.error.message == 'Not Found'


@pytest.mark.functionality
def test_latest_revision_for_non_existing_sha(create_gist_with_deletion):
    gist_client, gist = create_gist_with_deletion
    custom_sha = 'not_exist'
    result = gist_client.gists_action.get_latest_revision_of_gist_by_gist_id(gist.id, custom_sha=custom_sha)

    assert result.status_code == 422
    assert result.error.message == f'No commit found for SHA: {custom_sha}'
