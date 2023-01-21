#google_api
from django.shortcuts import render, redirect
from config import settings

#import service
from . import views_service

#board.urls.py
from board import urls #for google callback's redirect url (예정)

# Create your views here.

class OauthLogin:
    def google_login(request): #구글 로그인->코드받아옴->redirect로인해 google_callback실행
        '''
        Authorization Server에 client_id, response_type, redirect_url, scope 등을 넘겨주어 google_callback을 실행
        '''
        client_id = settings.GOOGLE_CLIENT_ID
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        scope = settings.GOOGLE_SCOPE

        #required: response_type, client_id, state? / optional: redirect_url, scope, access_type, prompt
        return redirect(f'{settings.GOOGLE_ENDPOINT}?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}&access_type=offline&prompt=select_account')

    def google_callback(request):
        code = request.GET.get('code') #get authorization_code(Use as approval permissions for resource servers) -> for Authorization Code Grant Flow
        print("code: ",code)
        #액세스 토큰은 API에서 읽고 유효성을 검사하기 위한 것
        #하단의 엑세스 토큰을 발급받고,
        access_token = views_service.Service.google_get_access_token(code) #code를 이용ㅇ해서 access token을 받아옴 / views_service.py의 class Service 이용
        #이를 userDB 혹은 tokenApp을 만들어 따로 보관하고 해당 엑세스 토큰의 주인이 누군지만 엮어놓는다면, 추후 이를 이용해 구글 api를 이용할 수 있다.
        #현재, 따로 저장을 해두지 않은 관계로 엑세스 토큰 이용 방식을 하단의 google_get_uer_info를 google_callback함수에 넣어서 보여주기 위해 적어 보았다.
        user_data = views_service.Service.google_get_user_info(access_token=access_token)
        profile_data = {
            'username': user_data['email'],
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', ''),
            'nickname': user_data.get('nickname', ''),
            'name': user_data.get('name', ''),
            'image': user_data.get('picture', None),
            'path': "google",
        }
        
        return redirect('http://127.0.0.1:8000/cafe/board') #board의 네임스페이스를 사용하는 법을 알게 되면 url별칭으로 바꿀 예정이다.
        

        
        

