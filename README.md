# 💻 GDSC 국민대 지부의 외부 홍보용 웹사이트 README

아래의 모든 ReadMe 는 다음의 노션 페이지 (인수인계서, 개발 wiki) 에 담긴 내용이니 다음 링크로 읽어보셔도 됩니다.

https://jinjae.notion.site/8f37ae9627d649ed9c70547efc1f5c99?pvs=4

-----

### ⌛️ 개발시 고려사항 및 작동 구조

* 해당 웹사이트에는 1)멤버별 정보 2) 깃허브 활동 정보를 담아 단체가 활성화 되어 있는 상태를 보여주는 것을 목표하였습니다.

  하지만 별도의 서버를 운영하면서 이를 구현하는 것에는 다음과 같은 애로사항이 있다고 판단하였습니다.

  1) 해당 웹사이트는 보여주는 용도이며 유저와의 상호작용이 존재하지 않아, 서버를 돌리는 것이 오버스팩이라고 판단.
  2) 서버를 돌리기 위해 클라우드 사용시 인수인계시에 결제(카드를 등록해서 사용하므로) 정보가 까다로울 것으로 판단.
   
* 따라서 깃허브 액션을 통해 api 를 사용하여 정보를 가져오고, 이를 깃허브 레포지토리 내에 저장하는 형식으로 같은 기능을 구현하였습니다.

-----

### 🏭 깃허브 레포지토리 구조

**A : 프론트엔드 react 빌드 및 보존을 위한 레포지토리**

- [https://github.com/Google-DSC-Kookmin/2023-02-WebPage-Project](https://github.com/Google-DSC-Kookmin/Project-Front)
- A 의 Github actions 은 빌드된 리액트 정적 파일을 B의 별도 브랜치로 저장합니다.

**B : (현재 레포지토리) 웹사이트와 관련된 정적 파일 코드(html,css,js) 및 멤버 정보, 멤버 활동 정보가 담긴 레포.**

- https://github.com/Google-DSC-Kookmin/Google-DSC-Kookmin.github.io

B 에는 Github actions work flow 가 두 가지 있습니다.

- B - **[main.yml](https://github.com/Google-DSC-Kookmin/Google-DSC-Kookmin.github.io/blob/master/.github/workflows/main.yml)** :  Github Pages 는 해당 레포지토리를 호스팅해줍니다.
- B - **[memberDataUpdate.yml](https://github.com/Google-DSC-Kookmin/Google-DSC-Kookmin.github.io/blob/master/.github/workflows/memberDataUpdate.yml) :내부 노션 멤버 데이터베이스에 접근하고,
- Notion API 를 통해 등록된 모든 멤버들의 속성값(이름, 깃허브 주소..)을 불러와 data/Members.json 에 저장합니다.**


-----

## 👓 해당 웹사이트가 데이터를 긁어오고, 업데이트, 호스팅하는 작동 플로우.

- Github Pages 에서는 정적인 페이지(html, css, javascript) 소스만 업로드 되어야 합니다.
    
    따라서, react 로 개발하는 방식을 채택하기 위해서, 다음과 같이 이루어집니다.
    
    1) react 로 로컬에서 개발
    
    2) 새로운 branch를 생성하여, github에 upload
    
    3) Pull requests 요청 및 main branch에 merge
    
    4) A 레포에 달린 github actions 이 돌면서, B 레포에 정적 파일(html,css,js)를 제공
    
    이때 B 레포에 별도의 브랜치가 생성되어 새로운 코드들을 포함하고 있음.
    
    5) B 레포의 새롭게 생성된 브랜치의 내용들을 Main 브랜치에 push / merge
    
    6) B 레포의 main push 를 actions 가 감지하고 새롭게 웹사이트 호스팅.


-----

## ✅ 수정하고 싶은 사안에 따라서 적절한 방식을 선택.

  **1) 웹사이트 내부의 특정 정보(데이터)를 수정하고 싶은 경우**

    B 레포의 data 폴더를 수정.

  **2) 웹사이트 내부 디자인의 일부(특정 수치 조정) 수정하고 싶은 경우**

    A 레포를 clone 하여 작업한 뒤, A레포에 branch로 푸쉬 및 Pull Request 생성

  **3) 웹사이트 전체 구성 또는 디자인의 큰 변화가 필요할 시**

    A 레포를 clone 하여 작업한 뒤, A레포에 branch로 푸쉬 및 Pull Request 생성

      → 어떠한 경우라도 B레포의 정적파일을 수정하는 경우, 다음 업데이트에서 해당내용은 누락됩니다.

-----
## 🧑‍🤝‍🧑 참여자 
- 이동국 김세현 이세영 이정안 이혁규 정일형
- https://www.notion.so/jinjae/gdsc-3f83ee1f75944c9b8e9a91637fee9473?pvs=4
