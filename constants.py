API_URL = 'api/v1/'
USER_LOGIN_URL = API_URL + 'token/'
USER_URL = API_URL + 'user/'
USER_REGISTRATION_URL = USER_URL + 'registration/'
POSTS_URL = API_URL + 'posts/'
LIKE_URL = API_URL + 'like/'
LIKE_COUNT_URL = API_URL + 'likecount/'


def get_user_actions_url(user_id):
    return f'{USER_URL}/{user_id}/actions/'
