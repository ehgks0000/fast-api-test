# 설정

* 패키지 매니저 설치
> 
`curl -sSL https://install.python-poetry.org | python3 -`    
[참고](https://python-poetry.org/docs/)

* 의존성 추가
>
`poetry add 모듈이름`

* 환경변수
>
export PYTHONPATH="/home/kim/projects/fast-test/app"    
export PYTHONPATH=$(pwd)/app

* 설치
>
poetry install // 의존성 설치

# 실행 방법

* 로컬 가상환경 venv
>
$ `. .venv/bin/activate`    //가상환경 실행         

$ `poetry install` // 의존성 설치

$ `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`

$ deactivate // 가상환경 종료


* 도커 컨테이너

> 
$ docker compose up --build // 도커 컨테이너 실행

