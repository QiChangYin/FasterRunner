from rest_framework.response import Response
from rest_framework.views import APIView
from fastuser.common import response
from fastuser import models
from fastuser import serializers
import logging
# Create your views here.
from fastuser.common.token import generate_token
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger('FastRunner')


class Test1View(APIView):


    """
    注册:{
        "user": "demo"
        "password": "1321"
        "email": "1@1.com"
    }
    """

    def post(self, request):

        # try:
        #     username = request.data["username"]
        #     password = request.data["password"]
        #     email = request.data["email"]
        # except KeyError:
        #     return Response(response.KEY_MISS)
        #
        # if models.UserInfo.objects.filter(username=username).first():
        #     return Response(response.REGISTER_USERNAME_EXIST)
        #
        # if models.UserInfo.objects.filter(email=email).first():
        #     return Response(response.REGISTER_EMAIL_EXIST)
        #
        # request.data["password"] = make_password(password)
        #
        # serializer = serializers.UserInfoSerializer(data=request.data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        return Response(response.REGISTER_SUCCESS)
        # else:
        #     return Response(response.SYSTEM_ERROR)


class Test2View(APIView):


    """
    注册:{
        "user": "demo"
        "password": "1321"
        "email": "1@1.com"
    }
    """

    def post(self, request):

        # try:
        #     username = request.data["username"]
        #     password = request.data["password"]
        #     email = request.data["email"]
        # except KeyError:
        #     return Response(response.KEY_MISS)
        #
        # if models.UserInfo.objects.filter(username=username).first():
        #     return Response(response.REGISTER_USERNAME_EXIST)
        #
        # if models.UserInfo.objects.filter(email=email).first():
        #     return Response(response.REGISTER_EMAIL_EXIST)
        #
        # request.data["password"] = make_password(password)
        #
        # serializer = serializers.UserInfoSerializer(data=request.data)
        #
        # if serializer.is_valid():
        #     serializer.save()
        return Response(response.REGISTER_SUCCESS)
        # else:
        #     return Response(response.SYSTEM_ERROR)

