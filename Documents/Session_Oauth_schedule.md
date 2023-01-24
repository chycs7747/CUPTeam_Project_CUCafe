회의내용



## Oauth2.0

1. Token - GitHub, Google 모두 가능
2. 인증은 토큰으로 유지는 세션으로
3. User모델은 세션파트쪽이랑 동일하게 다시 수정할 예정
4. settings.py에 설정한 설정값 들로 코드 구현해서 1/20일에 확인 할 예정



##Session

1. 세션에 로그인 정보 저장
   - request를 이용해서 user 모델의 email 저장
2. 로그인 시 세션에 저장된 이메일과 다를시 로그인 창으로 되돌아감.
3. 세션이 만료되었을 시 이용하는 Session Refresh까지 1/20에 구현할 예정 