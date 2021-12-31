API endpoints
=============

Basic
-----

- /rest-auth/login/ (POST)

    - username
    - email
    - password

    Returns Token key

- /rest-auth/logout/ (POST)

    .. note:: ``ACCOUNT_LOGOUT_ON_GET = True`` to allow logout using GET - this is the exact same configuration from allauth. NOT recommended, see: http://django-allauth.readthedocs.io/en/latest/views.html#logout


- /rest-auth/password/change/ (POST)

    - new_password1
    - new_password2
    - old_password

    .. note:: ``OLD_PASSWORD_FIELD_ENABLED = True`` to use old_password.
    .. note:: ``LOGOUT_ON_PASSWORD_CHANGE = False`` to keep the user logged in after password change

- /rest-auth/user/ (GET, PUT, PATCH)

    - username
    - first_name
    - last_name

    Returns pk, username, email, first_name, last_name


Registration
------------

- /rest-auth/registration/ (POST)

    - username
    - password1
    - password2
    - email



Creation of shortened links
---------------------------

- /create/ (POST)

    - original_link
    - shortened_link (you will get shortened link after you give original link)

Link list
---------

- / (GET)

    - you will get your shortened links if you logged in and created shortened links.