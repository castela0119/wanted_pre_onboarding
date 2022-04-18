# wanted_pre_onboarding
프리온보딩 - Backend 과정 선발과제입니다.

## 1. 가상환경 설치 및 실행
```shell
# virtualvenv 설치
> pip3 install virtualenv

# 가상환경을 위한 디렉토리
> python3 -m virtualenv [디렉토리명]

# 가상환경 활성화
> source [디렉토리명]/bin/activate

# 가상환경 비활성화
> deactivate
```

## 2. 모델 생성 및 서버 실행
```shell
# 마이그레이션을 생성하는 명령어
> python3 manage.py makemigrations

# 마이그레이션을 적용하는 명령어
> python3 manage.py migrate

# 서버 실행
> python manage.py runserver
```

## 3. 엔드포인트 설계
| 기능 | method | url |
|------|---|---|
| 전체 상품 조회 | GET | http://127.0.0.1:8000 |
| 특정 상품  | POST | http://127.0.0.1:8000 |

