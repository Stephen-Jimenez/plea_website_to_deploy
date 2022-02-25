from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bio', views.bio),
    path('shows/', views.shows),
    path('login_reg', views.login_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_comment', views.add_comment),
    path('media', views.media),
    path('rsvp/<int:user_id>/<int:show_id>', views.rsvp),
    path('rsvps/<int:show_id>', views.rsvps),
    path('edit/<int:user_id>', views.edit_page),
    path('edit_info/<int:user_id>', views.edit_info),
    path('delete_comment/<int:comment_id>/<int:user_id>', views.delete_comment),
]