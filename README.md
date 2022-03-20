# sinriboard 
> 게시판 사이트 데모사이트
  
  
해당 프로젝트는 학습용 테스트 프로젝트로 다음 사이트를 참고하여 만들었습니다.  
- [django official document](https://docs.djangoproject.com/en/4.0/)  
- [MDN django tutorial](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django)
- [점프 투 장고](https://wikidocs.net/book/4223)

```buildoutcfg
Python 3.10.2
django-admin --version 4.0.3 
```
```{javascript}
>> url mapping
/board // 게시판
/user // 사용자 로그인/회원가입 
/admin // 관리자 

>> tree
└board - 게시판 django app
└user - 사용자관리 django app
└sinriboard - django project
└static - scss, css
└template - html
└venv - 가상환경
```
