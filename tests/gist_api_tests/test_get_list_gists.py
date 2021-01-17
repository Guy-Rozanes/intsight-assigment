import datetime

import pytest


@pytest.mark.sanity
@pytest.mark.functionality
def test_get_my_gists(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    result = client.gists_action.get_gists_list()
    assert result.status_code == 200
    assert result.content[0].id == gist.id


@pytest.mark.functionality
def test_get_all_public_gists(create_authorized_gists_client_instance):
    client = create_authorized_gists_client_instance
    result = client.gists_action.get_gists_list(public=True)
    assert result.status_code == 200


@pytest.mark.functionality
def test_get_my_gists_from_specific_page(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    result = client.gists_action.get_gists_list(page=1)
    assert result.status_code == 200
    assert result.content[0].id == gist.id


@pytest.mark.functionality
def test_get_my_gists_from_non_existing_page(create_authorized_gists_client_instance):
    client = create_authorized_gists_client_instance
    result = client.gists_action.get_gists_list(page=100)
    assert result.status_code == 200
    assert result.content == []


@pytest.mark.functionality
def test_get_gist_from_specific_date(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    result = client.gists_action.get_gists_list(since=yesterday.isoformat())
    assert result.status_code == 200
    assert result.content[0].id == gist.id


@pytest.mark.functionality
def test_get_gist_from_specific_date_tomorrow(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    yesterday = datetime.datetime.now() + datetime.timedelta(days=1)
    result = client.gists_action.get_gists_list(since=yesterday.isoformat())
    assert result.status_code == 200
    assert result.content == []


@pytest.mark.functionality
def test_get_gist_from_specific_per_page(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    result = client.gists_action.get_gists_list(per_page=100)
    assert result.status_code == 200
    assert result.content[0].id == gist.id


@pytest.mark.functionality
def test_get_gist_combine_all_query_parameters(create_gist_with_deletion):
    client, gist = create_gist_with_deletion
    yesterday = datetime.datetime.now() + datetime.timedelta(days=1)
    result = client.gists_action.get_gists_list(page=1, per_page=5, since=yesterday.isoformat())
    assert result.status_code == 200
    assert result.content == []
