4가 http통신에러 (통신규약..)
Ex)

200: 성공적으로 접근했다는 것임

302:redirect 성공

400: 접근을 했는데 리소스가 없음
403: 인가되지 않은 접근
404: url이 이상함

5쪽 server에러



Oauth: 원래는 로그인기능이 없었음



Swing_test/settings.py 에
ALLOWED_HOSTS = [<주소>]
프로젝트 / 실행URL과 포트/ 실행URL과 포트에 등록된 8000번



MUDDLEWARE: 실행과정 중에서 중간작용을 해주는 친구들

- Csrf: 통신중 악의적인 접근을 막기 위해 csrf토큰을 생성해주는 친구인데, 종종 오류를 일으킴

TEMPLATES = []

- DIRS: [BASE_DIR/여기]



AUTH_USER_MODEL = 'oath.User' << 여기
기본에있던 유저모델이 아니라 우리가 생성해서 할거기때문에
우리가 만들어서 사용함



AUTH_PASSWORD_VALIDATORS

- 기본적으로 설정 되어있어서 건들 필요 없음



LANGUAGE_CODE = 'en-us
'TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
5개



토큰원리!

구글클라우드 - 구글에서 개발자들을 위해 제공(Azure과 비슷)
Oauth를 할때 어디에서 할 것이며, 누구까지 테스트 할 수 있게 해주는지.. API서비스를 만들어놈



ouath/settings.py의 #OAuth Setting

GOOGLE_REDIRECT_URI는
구글 클라우드/사용자 인증 정보 / 승인된 URL정보에 
승인된 URL과
GOOGLE_REDIRECT_URI = 'https://swing-tst.run.goorm.io/login/google/callback'
와 

구글클라우드/사용자 인증 정보 / 클라이언트 ID 에
있는 아이디랑 무조건 똑같아야함

구글클라우드/ OAuth 동의 화면 / 민감하지 않은 범위 / .email과 .profile 
구글클라우드/ OAuth 동의 화면 / 민감한 범위 / .datastore
에 있는 정보와
ouath/settings.py 
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/userinfo.email ' + 'https://www.googleapis.com/auth/userinfo.profile ' + 'https://www.googleapis.com/auth/datastore' 가 같아야함
GOOGLE_API_URI = 'https://www.googleapis.com/oauth2/v2'
ouath/views.py 의 주소확인



API

임시로 저장해서 토큰을 갖고있는 유저인지



1. 특정 계정으로 로그인 시도를 할 때 id를 통해서 코드를 생성하고 



Ouath/models.py
class User은 기존 장고의 User을 상속받는데, 기존 장고는
User(필드설정이 다되어있음) > abstract user(기초적인 필드설정만 되어있음) >abstract base user (인증설정만 되어있음, 다른필드는x, 우리는 로그인할때 학번으로 인증받기위해 이걸로 상속받음)



