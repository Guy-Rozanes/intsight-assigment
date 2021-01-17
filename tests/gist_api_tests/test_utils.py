def get_all_user_gist_ids(gist_client):
    all_gists = gist_client.gists_action.get_gists_list().content
    return [gist.id for gist in all_gists]
