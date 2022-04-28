# site

My website

## todo

dropdown on click

blog:
  blog post ideas:
    filter?
    tag?

  add view
    comment crud
    maybe oauth?

  maybe?
    crud?
    image?

## ideas

message text box like stackoverflow
notification

Avatar URL: {{ user.socialaccount_set.all.0.get_avatar_url }}
UID: {{ user.socialaccount_set.all.0.uid }}
Date Joined: {{ user.socialaccount_set.all.0.date_joined}}
Last Login: {{ user.socialaccount_set.all.0.last_login}}
Full Name: {{ user.socialaccount_set.all.0.extra_data.name }}
