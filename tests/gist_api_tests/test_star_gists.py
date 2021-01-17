import pytest


@pytest.mark.sanity
@pytest.mark.functionality
def test_star_a_gist(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    result = client.gists_action.star_a_gist_by_gist_id(gist.id)
    assert result.status_code == 204
    all_starred_gists = client.gists_action.get_all_starred_gists()
    assert all_starred_gists.content[0].id == gist.id


@pytest.mark.functionality
def test_star_non_existing_gist(create_authorized_gists_client_instance):
    client = create_authorized_gists_client_instance
    result = client.gists_action.star_a_gist_by_gist_id('non-existing')

    assert result.status_code == 404
    assert result.error.message == 'Not Found'


@pytest.mark.functionality
def test_star_gist_that_already_starred(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    client.gists_action.star_a_gist_by_gist_id(gist.id)
    result = client.gists_action.star_a_gist_by_gist_id(gist.id)
    assert result.status_code == 204

    all_starred_gists = client.gists_action.get_all_starred_gists()
    assert all_starred_gists.content[0].id == gist.id
