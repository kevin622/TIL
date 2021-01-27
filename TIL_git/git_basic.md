# Git 사용법

## 개념 정리

- `git` : 버전 관리 시스템

- `branch` : 깃에서 프로젝트 진행 시 마스터에서 분리된 일의 진행을 위해 만드는 폴더의 다른 버전. 이후 폐기를 하든 마스터와 병합을 한다.

- `master` : 깃 폴더의 중심이자 뼈대.

- `HEAD` : 깃 사용자의 위치. 특정 브랜치 혹은 마스터 중 하나이다.





## 명령어 정리

### 깃 직접 관리

- `$ git init` :  현재 경로에 *.git* 폴더 생성. 이후 해당 폴더 깃으로 관리 가능
- `$ git add .` : 변경 사항 스테이징
- `$ git commit -m <message>` : 스테이징 된 사항을 커밋. 변경사항이 직접 적용이 되는 최소단위
- `$ git remote add <리포 주소> ` : 깃 폴더를 깃허브/깃랩의 리포에 연결
- `$ git push origin <branch name>` : 특정 브랜치의 커밋 내용을 리포에 적용
- `$ git log` : 커밋 로그 출력
- `$ git reflog` : 브랜치 이동까지 포함한 모든 로그 출력

### 브랜치 관리

- `$ git branch` : 현재 생성되어있는 모든 브랜치 출력
- `$ git branch <branch name>` : 새로운 브랜치 생성
  - `$ git branch -d <branch name>` : (이미 병합이 된) 브랜치 삭제
  - `$ git branch -D <branch name>` : 브랜치 강제 삭제. 병합이 되지 않은 브랜치를 삭제할 때 사용
- `$ git switch <branch name> ` : 특정 브랜치로 이동. `$ git checkout <branch name> ` 을 사용할 수도 있다.
  - `$ git switch -c <branch name>` : 새로운 브랜치를 생성하고 이동
- `$ git merge <branch name>` : 특정 브랜치를 현재 위치와 병합