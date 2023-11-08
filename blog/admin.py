from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, form_request, commentpost, Postcaption,CustomGroup,Likecap,joingroup

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(form_request)
admin.site.register(commentpost)
admin.site.register(Postcaption)
admin.site.register(CustomGroup)
admin.site.register(Likecap)
admin.site.register(joingroup)


