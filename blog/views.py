from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from django.shortcuts import render, redirect
# from .form import SignUpForm
from django.utils.timezone import now
# Create your views here.
from re import S
from tkinter import E
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from .emails import *
from .serializer import *
from django.contrib.auth import authenticate


from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer

# to add users to database
from django.contrib.auth.models import User, auth
# for error msg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost, FollowersCount, form_request, Postcaption, commentpost, CustomGroup, joingroup
from django.http import HttpResponse, HttpResponseRedirect
from .form import form1
######
from django.core.mail import send_mail
from django.conf import settings
######
from itertools import chain
from random import shuffle
import datetime


@login_required(login_url='signin')
def index1(request):

    user_objects = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_objects)

    user_following_list = [user_profile]

    feed = []

    user_following = FollowersCount.objects.filter(
        follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
        feed_caps = Postcaption.objects.filter(user=usernames)
        feed.append(feed_caps)

    feed_cap = list(chain(*feed))

    for j in range(len(feed_cap)+1):  # tri organised posts by time creation
        for i in range(len(feed_cap)-j-1):
            if (feed_cap[i].created_at > feed_cap[i+1].created_at):
                aux = feed_cap[i]
                feed_cap[i] = feed_cap[i+1]
                feed_cap[i+1] = aux

    # ------------------------
    feedid = []
    for i in range(len(feed_cap)):
        feedid.append(feed_cap[i].id)

    feedids = [str(uuid) for uuid in feedid]
    for i in range(len(feedids)):
        feed_cap[i].id = feedids[i]
    # ------------------------COMMENTS
    comments = list(chain(commentpost.objects.all()))

    for j in range(len(comments)+1):  # tri organised posts by time creation
        for i in range(len(comments)-j-1):
            if (comments[i].created_at < comments[i+1].created_at):
                aux = comments[i]
                comments[i] = comments[i+1]
                comments[i+1] = aux

    feedC = []
    for i in range(len(comments)):
        feedC.append(comments[i].post_id)
    feedCM = [str(uuid) for uuid in feedC]
    # ------------------------LIKES
    like_filter = list(chain(LikePost.objects.all()))

    # ------------------------

    # user suggestions start
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(
        all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)

    final_suggestions_lsit = [x for x in list(
        new_suggestions_list) if x not in list(current_user)]
    shuffle(final_suggestions_lsit)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_lsit:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    # ------------------------------------------------------
    final_F_list = []
    new_F_list = [x for x in list(all_users) if (
        x in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_lsit = [x for x in list(
        new_F_list) if x not in list(current_user)]
    shuffle(final_F_list)
    username_profile_F = []
    username_profile_list_F = []

    for users in final_suggestions_lsit:
        username_profile_F.append(users.id)

    for ids in username_profile_F:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list_F.append(profile_lists)
    username_profile_list_F = list(chain(*username_profile_list_F))

    # ------------------------
    content = {
        'like_filter': like_filter,
        'following': username_profile_list_F,
        'user_profile': user_profile,
        'feedCM': feedCM,
        'comment': comments,
        'posts': feed_cap,
        # limité par 4
        'suggestions_username_profile_list': suggestions_username_profile_list[:4],
    }
    return render(request, 'blog/index1.html', content)


@login_required(login_url='signin')
def index2(request):

    user_objects = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_objects)

    user_following_list = [user_profile]
    feed = []

    user_following = FollowersCount.objects.filter(
        follower=request.user.username)
    user_following_list = Profile.objects.all()

    for usernames in user_following_list:
        feed_lists = CustomGroup.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_lists = CustomGroup.objects.filter(user=usernames)
    feed_cap = list(chain(*feed))

    for j in range(len(feed_cap)+1):
        for i in range(len(feed_cap)-j-1):
            if (feed_cap[i].created_at > feed_cap[i+1].created_at):
                aux = feed_cap[i]
                feed_cap[i] = feed_cap[i+1]
                feed_cap[i+1] = aux

    # ------------------------
    feedid = []
    for i in range(len(feed_cap)):
        feedid.append(feed_cap[i].id)

    feedids = [str(uuid) for uuid in feedid]
    for i in range(len(feedids)):
        feed_cap[i].id = feedids[i]

    # ------------------------
    comments = list(chain(commentpost.objects.all()))
    for j in range(len(comments)+1):
        for i in range(len(comments)-j-1):
            if (comments[i].created_at < comments[i+1].created_at):
                aux = comments[i]
                comments[i] = comments[i+1]
                comments[i+1] = aux
    feedC = []
    for i in range(len(comments)):
        feedC.append(comments[i].post_id)
    feedCM = [str(uuid) for uuid in feedC]

    # ------------------------
    join_filter = joingroup.objects.all()

    # ------------------------
    # user suggestions start
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    new_suggestions_list = [x for x in list(
        all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_lsit = [x for x in list(
        new_suggestions_list) if x not in list(current_user)]
    shuffle(final_suggestions_lsit)
    username_profile = []
    username_profile_list = []

    for users in final_suggestions_lsit:
        username_profile.append(users.id)
    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)
    suggestions_username_profile_list = list(chain(*username_profile_list))

    # ------------------------------------------------------
    final_F_list = []
    new_F_list = [x for x in list(all_users) if (
        x in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_lsit = [x for x in list(
        new_F_list) if x not in list(current_user)]
    shuffle(final_F_list)
    username_profile_F = []
    username_profile_list_F = []

    for users in final_suggestions_lsit:
        username_profile_F.append(users.id)
    for ids in username_profile_F:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list_F.append(profile_lists)
    username_profile_list_F = list(chain(*username_profile_list_F))

    # ------------------------
    content = {
        'join_group': join_filter,
        'following': username_profile_list_F,
        'user_profile': user_profile,
        'feedCM': feedCM,
        'comment': comments,
        'posts': feed_cap,
        'suggestions_username_profile_list': suggestions_username_profile_list[:4],
    }
    return render(request, 'blog/index2.html', content)


@login_required(login_url='signin')
def groups(request):

    if request.method == 'POST':
        user = request.user.username
        if request.FILES.get('image_upload1') != None:
            image = request.FILES.get('image_upload1')
        else:
            image = " "

        description = request.POST['description']
        name = request.POST['name']
        starts_at = request.POST['startat']
        finish_at = request.POST['finishat']
        Activity = request.POST['Activity']
        Location = request.POST['Location']
        if starts_at < str(datetime.datetime.today()):
            messages.error(request, 'date Invalide')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif starts_at > finish_at:
            messages.error(request, 'date Invalide')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            new_post = CustomGroup.objects.create(
                user=user, name=name, starts_at=starts_at, location=Location, finish_at=finish_at, activity=Activity, image=image, caption=description)
            new_post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def Jgroup(request):
    username = request.user.username
    id = request.GET.get('post_id')

    post = CustomGroup.objects.get(id=id)

    join_filter = joingroup.objects.filter(
        post_id=id, username=username).first()

    if join_filter == None:
        new_join = joingroup.objects.create(post_id=id, username=username)
        new_join.save()

        post.teammates = post.teammates+1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        join_filter.delete()
        post.teammates = post.teammates-1
        post.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    id = request.GET.get('post_id')

    post = Post.objects.get(id=id)

    like_filter = LikePost.objects.filter(
        post_id=id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=id, username=username)
        new_like.save()

        post.no_of_likes = post.no_of_likes+1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def post_comment(request):
    id = request.GET.get('post_id')
    username = request.user.username
    comments = request.POST['comment']

    new_com = commentpost.objects.create(
        auther=username, post_id=id, com=comments)
    new_com.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def delete(request):
    username = request.user.username
    id = request.GET.get('post_id')

    posts = Post.objects.filter(user=username)
    postid = []
    for i in range(len(posts)):
        postid.append(posts[i].id)
    postid = [str(uuid) for uuid in postid]
    if id in postid:
        Post.objects.filter(id=id).delete()
    else:
        Postcaption.objects.filter(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def deleteCustGrp(request):
    username = request.user.username
    id = request.GET.get('id')
    bousts = CustomGroup.objects.filter(user=username)
    postid = []
    for i in range(len(bousts)):
        postid.append(bousts[i].id)
    postid = [str(uuid) for uuid in postid]
    if id in postid:
        CustomGroup.objects.filter(id=id).delete()
    else:
        CustomGroup.objects.filter(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='signin')
def like_cap(request):
    username = request.user.username
    id = request.GET.get('post_id')

    post = Postcaption.objects.get(id=id)

    like_filter = LikePost.objects.filter(
        post_id=id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=id, username=username)
        new_like.save()

        post.no_of_likes = post.no_of_likes+1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_caption = Postcaption.objects.filter(user=pk)
    user_post_length = len(user_posts)+len(user_caption)

    like_filter = LikePost.objects.all()

    feed = []
    feed.append(user_posts)
    feed.append(user_caption)
    feed_cap = list(chain(*feed))
    for i in range(len(feed_cap)):
        for j in range(len(feed_cap)-i-1):
            if (feed_cap[i].created_at > feed_cap[i+1].created_at):
                aux = feed_cap[i]
                feed_cap[i] = feed_cap[i+1]
                feed_cap[i+1] = aux
    # -------------------------------------------
    feedid = []
    for i in range(len(feed_cap)):
        feedid.append(feed_cap[i].id)

    feedids = [str(uuid) for uuid in feedid]
    for i in range(len(feedids)):
        feed_cap[i].id = feedids[i]
    # ------------------------
    comments = list(chain(commentpost.objects.all()))
    for j in range(len(comments)+1):
        for i in range(len(comments)-j-1):
            if (comments[i].created_at < comments[i+1].created_at):
                aux = comments[i]
                comments[i] = comments[i+1]
                comments[i+1] = aux
    feedC = []
    for i in range(len(comments)):
        feedC.append(comments[i].post_id)
    feedCM = [str(uuid) for uuid in feedC]

    follower1 = request.user.username
    user1 = pk

    if FollowersCount.objects.filter(follower=follower1, user=user1).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))
    context = {
        'like_filter': like_filter,
        'comment': comments,
        'feedCM': feedCM,
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': feed_cap,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'blog/profile.html', context)


def index(request,):
    if request.method == 'POST':
        from_email = request.POST['email']
        name = request.POST['name']
        sub = request.POST['subjects']
        message = request.POST['message']
        send_mail(
            sub,  # title
            name+" send a message using his email "+from_email + \
            " to tell you ' "+message+"'",  # message
            from_email,  # sender
            ['AquaTide322@gmail.com'],  # reciver
            fail_silently=False
        )
    return render(request, 'blog/index.html', {})


# def finishpass(request):
#     u = User.objects.get(username=)
#     user_profile = Profile.objects.get(user=u)
#     if request.method == 'POST':
#         u.set_password()
#         u.save()
#     return render(request, 'blog/finishpass.html', {user_profile: "user_profile"})


@login_required(login_url='signin')
def log_out(request):
    auth.logout(request)
    return redirect('/index')


@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower1 = request.POST['follower']
        user1 = request.POST['user']
        if FollowersCount.objects.filter(follower=follower1, user=user1).first():
            delete_follower = FollowersCount.objects.get(
                follower=follower1, user=user1)
            delete_follower.delete()
            return redirect('/profile/'+user1)
        else:
            new_follower = FollowersCount.objects.create(
                follower=follower1, user=user1)
            new_follower.save()
            return redirect('/profile/'+user1)
    else:
        return redirect('/')


@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []
        for users in username_object:
            username_profile.append(users.id)
        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'blog/search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:

        return redirect('/')

    return HttpResponse('<h1>Upload View </h1>')


@login_required(login_url='signin')
def uploadcap(request):
    if request.method == 'POST':
        user = request.user.username
        caption = request.POST['caption']

        new_cap = Postcaption.objects.create(user=user, caption=caption)
        new_cap.save()
        return redirect('/')
    else:

        return redirect('/')

    return HttpResponse('<h1>Upload View </h1>')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    # 2:03:10 accolades data binding frontend to backend
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('settings')

    return render(request, 'blog/setting.html', {'user_profile': user_profile})


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                # .error or .info gives the information in the database
                messages.error(request, 'Email taken')
                return redirect('sign_up')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('sign_up')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                # log in and redirect to setting page
                user_login = auth.authenticate(
                    username=username, email=email, password=password)
                auth.login(request, user_login)

                # create profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.error(request, 'Password not matched')
            return redirect('sign_up')
    else:
        return render(request, 'blog/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.error(request, 'Credentials Invalid')
            return redirect('signin')
    return render(request, 'blog/sign_in.html', {})


def form(request):
    if request.method == 'POST':
        form = form1(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/index")

    return render(request, 'blog/form.html', {'form': form1})

##################################################################


# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })


# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

# class LoginAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data=data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 password = serializer.data['password']

#                 user = authenticate(email=email, password=password)

#                 if user is None:

#                     return Response({
#                         'status': 400,
#                         'message': 'invalid password mf'
#                         'data': {}
#                     })

#                 refresh = RefreshToken.for_user(user)

#                 return {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 }

#             return Response({
#                 'status': 400,
#                 'message': 'something went wrong mf'
#                 'data': serializer.errors
#             })

#         except Exception as e:
#             print(e)
