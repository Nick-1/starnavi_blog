# starnavi_social_network

**To start a project:**
1. cd starnavi_blog
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py runserver


**API urls:**
###### api/v1/user/registration/
- POST registration user

###### api/v1/user/login/
- POST login (JWT)

###### api/v1/posts/
- GET all posts
- POST create post

###### api/v1/posts/{{post_id}}
- GET one post

###### api/v1/posts/{{post_id}}
- PATCH change post
- DELETE remove post

###### api/v1/like/
- POST like

###### api/v1/like/{{post_id}
- DELETE unlike

###### api/v1/likescount/?date_from=**{{date}}**&date_to=**{{date}}** ex: 2020-7-10
- GET count and date of current user likes

###### api/v1/user/{{user_id}}/actions/
- GET gel user actions (login and last action time)

**Postman collection:**
[**Postman collection:**](https://www.getpostman.com/collections/f48922350938724534c3)



