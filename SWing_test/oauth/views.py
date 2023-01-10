from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from SWing_test import settings
import requests
from .models import User, UserManager

#Create your views here.

#for display Login & success view
class HtmlView:
    def index(request):
        return render(request, 'oauth/index.html')

    def success(request):
        return render(request, 'oauth/success.html')
    
def login(request, context):
    print('login process')
    #if request.method == 'POST':
    id = context.get('id')
    password = context.get('password', None)
    user = auth_authenticate(id=None, password = None) #auth_authenticate는 Import해서 사용. 해당 id, password를 갖고있는지 확인
    if settings.TMP_USER_TOKEN == context.get('email')+'_'+context.get('token'):
        print("token check success")
        if user is not None:#### 순서 변경 필요    
            auth_login(request, user)
            print('login success')
        else:
            print('user is None')
            signup(request,context)
    else:
        print('비정상적 접근')
    #else:
    #    print('POST방식 아님')
    return
    
def signup(request, context):
    print('sign up process')
    id = context.get('id', None)
    email = context.get('email', None)
    name = context.get('name', None)
    print(id)
    print(email)
    print(name)
    if id is not None:
        if email is not None:
            if name is not None:
                user = User.objects.create_user(id, email, name)
                print('create user success')
                login(request, context)
            else:
                print('name is none')
        else:
            print('email is none')
    else:
        print('id is none')
    return

#for use Google Oauth authentication, get code by client_id first and get token by code, client_id, client_secret.
class OauthLogin:
    def google_login(request): #구글 로그인->코드받아옴->redirect로인해 google_callback실행
        print('login')
        client_id = settings.GOOGLE_ID
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        scope = settings.GOOGLE_SCOPE
        return redirect(f'{settings.GOOGLE_LOGIN_URI}/auth?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}')

    def google_callback(request):
        print('callback')
        client_id = settings.GOOGLE_ID
        client_secret = settings.GOOGLE_SECRET
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        code = request.GET.get('code', None) #잘못된게 아니면 get방식으로 code를 받아옴. 실패시 None을 반환
        if code is not None:
            result = requests.post(
                f"https://oauth2.googleapis.com/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&grant_type=authorization_code",
                headers={"Accept": "application/json"}, #grant_type=authorization_code == 토큰
            )
            result_json = result.json() # json양식으로 받아옴
            error = result_json.get("error", None) #에러가 없으면 None반환 (토큰이 잘 반환되었는지)
            if error is not None:
                return redirect('http://127.0.0.1:8000/')
            else:
                print('pass')
                access_token = result_json.get('access_token')
                profile_request = requests.get(
                    f'{settings.GOOGLE_API_URI}/userinfo?alt=json&access_token={access_token}',
                    headers={
                        'Authorization': f'token {access_token}',
                        'Accept': 'application/json',
                    },
                )
                
                ####
                profile_json = profile_request.json()
                user_email = ProcessingUserData.get_email(profile_json) # = profile_json.get('email')
                user_name = ProcessingUserData.get_name(profile_json)
                
                settings.TMP_USER_TOKEN = user_email+'_'+access_token
                
                print(profile_json)
                print(user_email)
                print(ProcessingUserData.email_parsing(user_email))
                context = { 
                    'id': ProcessingUserData.email_parsing(user_email)[0],
                    'email': user_email,
                    'name': user_name,
                    'token': access_token,
                }
                if(ProcessingUserData.check_dankook_mail(user_email) == True):
                    print('it is dankook mail')
                    login(request, context)
                else:
                    print('it is not dankook mail')
                ####
                                
                ##render? templete 호출  redirect? url 호출 but cotext 전달 불가 해결해야됨
                return redirect('http://127.0.0.1:8000/success', context)
        else:
            return redirect('http://127.0.0.1:8000/')

class ProcessingUserData:
    def get_email(user_profile):
        return user_profile.get('email', None)
        
    def get_name(user_profile):
        return user_profile.get('name', None)
    
    def email_parsing(user_email):
        return user_email.split('@')
    
    def check_dankook_mail(user_email):
        if(ProcessingUserData.email_parsing(user_email)[1] == 'dankook.ac.kr'):
            return True
        else:
            return False
    
