from django.urls import re_path
from techCare.userApp import views as vw


urlpatterns = [
    re_path(r'^my_account/(?P<_id>\d+)/', vw.my_account, name="my_account"),
    re_path(r'^edit_account/(?P<_id>\d+)/', vw.edit_account, name="edit_account"),
    # re_path(r'^deactivate_profile/(?P<user_id>\d+)/', vw.deactivateProfile, name="deactivate_profile"),
]