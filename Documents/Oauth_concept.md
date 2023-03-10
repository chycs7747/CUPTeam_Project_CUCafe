#### OAuth의 4가지 유형

1. 리소스 소유자

   보호된 리소스에 대한 액세스 권한을 부여 가능함.  
   사람의 경우엔 end-user이라고 부른다.

2. 리소스 서버

   허용할 수 있는 보호된 리소스를 호스팅하는 서버이다.  
   엑세스 토큰을 사용하여 보호된 리소스 요청에 응답한다.

3. 고객  

   리소스 소유자를 '대신하여' 권한을 부여하여 보호된 리소스 요청을 수행하는 응용 프로그램이다.   
   "클라이언트"라는 용어는 특정 구현 특성(예: 애플리케이션이 서버, 데스크톱 또는 다른 장치에서 실행되는지 여부)을 의미하지 않는다.  

4. 서버가 성공한 후 클라이언트에 액세스 토큰을 발급한다.
   리소스 소유자 인증 및 권한 부여.

인가 서버와 리소스 서버 간의 상호 작용은 이 규격의 범위를 벗어납니다. 인가 서버는 리소스 서버와 동일한 서버이거나 별도의 엔티티일 수 있다.
단일 권한 부여 서버는 여러 리소스 서버에서 허용하는 액세스 토큰을 발급할 수 있습니다.

![스크린샷 2023-01-09 오후 3.12.45](/Users/yunho/Library/Application Support/typora-user-images/스크린샷 2023-01-09 오후 3.12.45.png)



순서

고객이 리소스 소유자에게 Authorization(인가) 요청을 보내면, 리소스 소유자는 클라이언트에게 Authorization Grant(인가 수여증)을 준다. 이 수여증으로 인가 서버에 요청을 보내면, 수여증이 유효한지 서버가 확인하고 유효하면 엑세스 토큰을 준다.  

이 Authorization Grant에는 4가지 증명서를 갖고 있다.

1.  <strong>Authorization code</strong>
2. Implicit 
3. resource owner password credentials
4. client credentials

고객은 이 엑세스 토큰을 통해 리소스 서버에 접근해서 보호된 리소스를 얻는다.



Authorization Grant 요소 설명

1. Authorization Code

   Authorization Code는 클라이언트와 리소스 소유자가 Authorization Server과 중개를 통해 발급한다.(처음에 클라이언트에게 권한 부여 요청, 리소스 소유자가 서버에게 authorization grant를 받아서 클라이언트에게 줌. 중개 없이 둘 사이에서 주는 같은 것보다 선호됨(Resource Owner Password Credentials방식을 뜻하는 것으로 보임.) 직접 리소스 소유자가 클라이언트에게 이 코드를 주지 않는 이유는, 리소스 소유자가 인가를 받기 위해 뭔가 행동을 하는 것은 오로지  authorization server사이에서만 이루어지기 때문이다. (리소스 소유자의 보호된 리소스 권한 접근 증명서(credentials)는 클라이언트와 공유하지 않음.) 

   이 Authorization code는 몇가지 이점을 클라이언트에게 제공한다. 주내용: 대리인을 거치지 않고, authorization server에게 access token을 요청할 수 있다. (보안 이점도 있다고 함)

2. Implicit

   authorization code flow를 단순화 시킴 (authorization code를 통해 access token)을 요청하지 않고 authorization server엑게 바로 access token을 받음 (redirect url로 code대신 token을 받는 격)

   

3. Resource Owner Password Credentials

   implicit 방식과 다르게 리소스 소유자에게 직접 Resource Owner Password Credentials을 요청하고 이를 이용해 authorization server에게 직접적으로 access token을 요청한다.

4. Client Credentials Grant Type

   개인 클라우드 저장소와 같이 리소스의 소유자가 클라이언트와 같은 경우일 때 주로 사용. Client Credentials를 통해 직접적으로 보호된 자원에 요청할 수 있다.

   

Refresh Token

- Access토큰 갱신을 위해 사용. Access토큰보다 갱신 기간이 길어야 함.
- 문자열로 리소스 소유자에게 클라이언트가 authorization grant를 받았다는 것을 증명함
- 엑세스 토큰을 재발급 받을때 Optional Refresh Token을 받을 수도 있음



mac token vs bearer token

- Bearer 토큰의 일종인 access토큰은 보호된 리소스 요청을 수행하는데 필요한 정보를 담고 있으므로, 이 토큰 유형에 대한 이해가 없으면 절대로 사용해서는 안된다.
- 이럴 때 mac token을 사용, but 맥 토큰도 단점이 존재. Bearer token의 강점이 mac token의 약점이고 역도 성립



[Access Token]



Access Token Request

```
grant_type
         REQUIRED.  Value MUST be set to "password".

   username
         REQUIRED.  The resource owner username.

   password
         REQUIRED.  The resource owner password.

   scope
         OPTIONAL.
```



Access Token Response



1. Authorization Code Grant

   [Authorization Request]

   ```
   1) response_type
            REQUIRED.  Value MUST be set to "code".
   
   2) client_id
            REQUIRED.  The client identifier as described in Section 2.2.
   
   3) redirect_uri
            OPTIONAL.  As described in Section 3.1.2.
            
   4) scope
            OPTIONAL.  The scope of the access request as described by
            Section 3.3.
   
   5) state
            RECOMMENDED.  An opaque value used by the client to maintain state between the request and callback.  The authorization server includes this value when redirecting the user-agent back to the client. The parameter SHOULD be used for preventing cross-site request forgery as described in Section 10.12.
   ```

   [Authorization Response]

   ```
   code
            REQUIRED.  The authorization code generated by the authorization server.  The authorization code MUST expire shortly after it is issued to mitigate the risk of leaks. A maximum authorization code lifetime of 10 minutes is RECOMMENDED. The client MUST NOT use the authorization code more than once.  If an authorization code is used more than once, the authorization server MUST deny the request and SHOULD revoke (when possible) all tokens previously issued based on that authorization code.  The authorization code is bound to the client identifier and redirection URI.
   
   state
            REQUIRED if the "state" parameter was present in the client authorization request.  The exact value received from the client.
   ```

​		[Error Response]

​		

```
error
         REQUIRED.  A single ASCII [USASCII] error code from the
         following:

         invalid_request
               The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.
               
				unauthorized_client
               The client is not authorized to request an authorization code using this method.

         access_denied
               The resource owner or authorization server denied the request.

         unsupported_response_type
               The authorization server does not support obtaining an authorization code using this method.

         invalid_scope
               The requested scope is invalid, unknown, or malformed.

         server_error
               The authorization server encountered an unexpected condition that prevented it from fulfilling the request. (This error code is needed because a 500 Internal Server Error HTTP status code cannot be returned to the client via an HTTP redirect.)

         temporarily_unavailable
               The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  (This error code is needed because a 503
 Service Unavailable HTTP status code cannot be returned to the client via an HTTP redirect.)
Values for the "error" parameter MUST NOT include characters outside the set %x20-21 / %x23-5B / %x5D-7E.

   			error_description
         OPTIONAL.  Human-readable ASCII [USASCII] text providing additional information, used to assist the client developer in understanding the error that occurred. Values for the "error_description" parameter MUST NOT include characters outside the set %x20-21 / %x23-5B / %x5D-7E.

   			error_uri
         OPTIONAL.  A URI identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error. Values for the "error_uri" parameter MUST conform to the
 URI-reference syntax and thus MUST NOT include characters outside the set %x21 / %x23-5B / %x5D-7E.
	 			state
         REQUIRED if a "state" parameter was present in the client authorization request.  The exact value received from the client.

```



2. implicit Grant

[Response]

```
access_token
         REQUIRED.  The access token issued by the authorization server.

   token_type
         REQUIRED.  The type of the token issued as described in Section 7.1.  Value is case insensitive.

   expires_in
         RECOMMENDED.  The lifetime in seconds of the access token. For example, the value "3600" denotes that the access token will] expire in one hour from the time the response was generated.
 If omitted, the authorization server SHOULD provide the expiration time via other means or document the default value.

   scope
         OPTIONAL, if identical to the scope requested by the client; otherwise, REQUIRED.  The scope of the access token as described by Section 3.3.

   state
         REQUIRED if the "state" parameter was present in the client authorization request.  The exact value received from the client.
```

- The authorization server MUST NOT issue a refresh token.

3. Resource Owner Password Credentials Grant flow

[Response]

```
An example successful response:

     HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
       "example_parameter":"example_value"
     }
```

4. Client Credentials Grant flow

[Response]

```
HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "example_parameter":"example_value"
     }
```

- A refresh token SHOULD NOT be included



더 자세한

Response, Request, Error은 하단의 링크를 참고

https://datatracker.ietf.org/doc/html/rfc6749#section-4