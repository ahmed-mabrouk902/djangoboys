from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from knox import views as knox_views
urlpatterns = [
    # path('api/login/h', views.index, name='index'),
    # path('', views.index, name='index'),
    path('index', views.index, name=''),
    path('index2', views.index2, name='index2'),
    path('', views.index1, name=''),

    path('sign_up', views.sign_up, name='sign_up'),
    path('signin', views.sign_in, name='signin'),
    path('logout', views.log_out, name='logout'),
    # path('accounts/profile/', views.finishpass, name='accounts/profile/'),

    path('upload', views.upload, name='upload'),
    path('delete', views.delete, name='delete'),
    path('deleteCustGrp', views.deleteCustGrp, name='deleteCustGrp'),
    path('groups', views.groups, name='groups'),
    path('uploadcap', views.uploadcap, name='uploadcap'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('Jgroup', views.Jgroup, name='Jgroup'),

    path('comment', views.post_comment, name='post_comment'),
    path('like-cap', views.like_cap, name='like-cap'),
    path('form', views.form, name='form'),
    path('settings', views.settings, name='settings')
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]

# to locate files of media
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
