# Last_project

### before work 

git branch '(back/front)_기능' 으로 branch 생성

- 새로 나온 branch 에서 commit 이 밀렸을 때
1. branch --set-upstream-to=origin/master '위에 설정한 이름'
2. git pull 

-> master 브랜치와 같은 상태에 놓임.

- 새로운 branch 에서 push 

1. git push --set-upstream origin '새로운 branch 이름'
2. git switch master
3. git merge '새로운 branch 이름'
4. git push

-> master 브랜치와 같은 상태에 놓임.

- commit -m '한글로 작성, 말머리 [수정/추가...] 등 적절하게 사용 이후, 간략하게 설명'

2023/11/16
------------------

보안해야 할 점 (은미):
1. 찾는 지역에 해당 은행이 없을 경우에 '해당 은행이 없습니다' 메세지 출력 _ KakaoMap.vue
2. CSS

할 일 (휘원):
1. 게시글/댓글 작성자만 수정, 삭제 기능 추가 DetailView.vue 
2. 환율 api 기능 추가

2023/11/20
------------------
npm install bootstrap bootstrap-vue-3
npm install -D sass

할 일
- 은미:
1. app.vue main3.png 구성
2. sign-up, longin css
3. a태그 링크 연결 (app.vue)

- 휘원 :
1. 프로필 페이지 구현
