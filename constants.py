API_URL = 'api/v1/'
USER_LOGIN_URL = API_URL + 'token/'
USER_URL = API_URL + 'user/'
USER_REGISTRATION_URL = USER_URL + 'registration/'
POST_ROUT = 'posts'
LIKE_ROUT = 'like'
LIKES_COUNT_ROUT = 'likescount'
ACTIONS_URL = 'actions'
POSTS_URL = f'{API_URL}{POST_ROUT}/'
LIKE_URL = f'{API_URL}{LIKE_ROUT}/'
LIKE_COUNT_URL = f'{API_URL}{LIKES_COUNT_ROUT}/'


def get_user_actions_url(user_id):
    return f'/{USER_URL}{user_id}/{ACTIONS_URL}/'
