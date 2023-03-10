리눅스

필요 배경지식

1. 두꺼운 책을 보면 보통 앞쪽에 유닉스 시스템부터해서 ~ 역사가 나오는데, 이런 배경지식 부분부터 잘 봐두기



리눅스란 무엇인가?

- Computer Operating System(OS)와 같은 것

OS란 무엇인가?

- 시스템 소프트웨어 - 컴퓨터 하드웨어, 소프트웨어 자원을 관리





[기존의 세션 방식]

- 사용자가 로그인을 했었다는 기록을 세션으로써 서버가 기억함. 쉽게말해, 로그인을 할 때 표를 발급받는데 (authentication), 표를 반 찢어서 사용자 서버가 갖고있다가 다시 그 사용자가 로그인할 때 서로의 찢어진 표를 보고 인가를 해줌(authorization)

단점: 서버가 여러개면 1번서버에서 인증한 표가 3번서버에서 인증이 되지 않음. 그렇다고 서버용 세션 데이터베이스를 만들어 관리하면 속도가 느려지고, 이 속도를 해결한 데이터베이스를 만든다 해도 서로가 얽혀있어서 데이터베이스에 문제가 생기면 큰일이 날 수 있음.

이를 해결한 방식

-> JWT 토큰 방식..!

JWT 토큰 방식

- 세 부분으로 나뉘어져 있음.
  - Header
  - Payload
  - Verify Signature
- 위와 같은 정보를 클레임이라고 한다.
- 위의 정보를 로그인 시 서버에 보내면, 서버가 요청마다 일일이 데이터베이스에서 확인해야할 양이 줄어든다.
- 특별한 암호화가 아니라 Base64로 인코딩한 것이므로, 사용자가 자바스크립트같은걸로 디코딩해서 볼 수 있는 것 아닌가?
- 그렇지 않다. Header부분에는 타입("typ")가 반드시 "JWT"여야 하고, 알고리즘("alg")는 3번 서명 값을 만드는데 사용된다. 이 때 사용되는 알고리즘이 Hmac sha 256등의 방식.
- 1번 헤더와 2번 페이로드, 그리고 "서버에 감쳐놓은 비밀 값"을 암호화 알고리즘에 넣고 돌리면 3번 서명 값이 나옴. (해쉬함수의 단방향성)

하지만.. 역시 세션에 비교했을 때 JWT도 단점이 존재

단점: JWT는 불가능하지만, 세션은 Stateful해서, 모든 사용자들의 상태를 기억하고 있다는건 구현하기 부담되고 고려사항도 많지만, 이게 된다면 기억하는 대상의 상태들을 언제든 제어할 수 있다는 의미 즉, 세션 방식으로는 한 기기에서만 로그인 가능한 서비스를 만드는 경우 PC에서 로그인한 상태의 어떤 사용자가 핸드폰에서 또 로그인하면 PC에서는 로그아웃되도록 기존 세션을 종료하는게 가능하다.

다시말해, 세션 방식에서는 책상에 올려둔 표를 버리면 되는데, JWT에서는 이것이 불가능하다. 왜냐하면 이미 줘버린 토큰을 뺏어 버릴 수 없고, 그 토큰의 발급 내역이나 정보를 서버가 어디에 기록해서 추적하고 있지 않으므로 통제가 불가능. 그렇다고 상태를 어디에다 기록해두면 세션과 큰 차이가 없고, 공격자가 이 토큰을 탈취해버리면 막을 방법도 존재하지 않는다.

->JWT만으로 인가를 주는 서비스는 많지 않음

이를 보완하기 위해 여러 방법이 있지만, 한계점이 존재한다.

예를들어, access토큰과 refresh토큰을 만든다. access토큰은 인가를 위한 토큰이고, refresh토큰은 access토큰을 갱신해주기 위한 토큰으로, 만료기간을 길게 잡는다. 이렇게하면 access토큰이 로그인 중에 탈취당해도 공격자는 이 토큰을 오래 사용하지 못한다. 그리고 탈취당했을 때 refresh토큰을 지워버리면 갱신도 하지 못한다.
하지만, 역시나 짧은 시간동안은 공격자가 access토큰을 사용 가능하다는 점이 한계점이라고 할 수 있겠다.

Written by Choi
