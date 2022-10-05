from django.urls import path
from content.views import UploadFeed, Profile, Main, UploadReply, ToggleLike, ToggleBookmark, delete_feed, delete_reply, update_feed, delete_reply
#1번 방식
from content import views

urlpatterns = [
    
    path('upload/', UploadFeed.as_view()),
    path('reply/', UploadReply.as_view()),
    path('like/', ToggleLike.as_view()),
    path('bookmark/', ToggleBookmark.as_view()),
    path('profile/', Profile.as_view()),

    path('main/', Main.as_view(), name='main'),
    path('<int:id>/delete/', delete_feed), # 게시글 삭제
    path('<int:id>/update/', update_feed), # 게시글 수정
    # 1번 방식
    path('<int:pk>', views.detail, name='detail'),
    # 2번 방식
    # path('<int:pk>', Main.detail),
   
    path('delete/<int:id>/', delete_reply, name='delete'),
    
]
