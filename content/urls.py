from django.urls import path
from content.views import UploadFeed, Profile, Main, UploadReply, ToggleLike, ToggleBookmark, delete_reply

urlpatterns = [
    path('upload/', UploadFeed.as_view()),
    path('reply/', UploadReply.as_view()),
    path('like/', ToggleLike.as_view()),
    path('bookmark/', ToggleBookmark.as_view()),
    path('profile/', Profile.as_view()),
    path('main/', Main.as_view(), name='main'),
    
    path('delete/<int:id>/', delete_reply, name='delete'),
]

