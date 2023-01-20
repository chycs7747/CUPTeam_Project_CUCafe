from django.shortcuts import render
from SWing_test import settings

# Create your views here.

class OauthLogin:
    def google_login(request): #구글 로그인->코드받아옴->redirect로인해 google_callback실행
        print('login')
        client_id = settings.GOOGLE_ID
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        scope = settings.GOOGLE_SCOPE
        return redirect(f'{settings.GOOGLE_LOGIN_URI}/auth?client_id={client_id}&