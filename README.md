# wanted_pre_onboarding
프리온보딩 - Backend 과정 선발과제입니다.

## 1. 가상환경 설치 및 실행
```shell
# virtualvenv 설치
> sudo pip install virtualenv

# 가상환경을 위한 디렉토리
> python3 -m virtualenv [디렉토리명]

# 또는
> virtualenv -p python3 [디렉토리명]

# 가상환경 활성화
> source [디렉토리명]/bin/activate

# django 프레임워크 설치
> pip3 install django

# 가상환경 비활성화
> deactivate

# 패키지 목록 출력
> pip freeze

# 패키지 목록을 requirements.txt에 저장
> pip freeze > requirements.txt
```

## 2. 모델 생성 및 서버 실행
```shell
# 마이그레이션을 생성하는 명령어
> python3 manage.py makemigrations

# 마이그레이션을 적용하는 명령어
> python3 manage.py migrate

# 서버 실행
> python3 manage.py runserver
```

## 3. 엔드포인트 설계
| 기능 | method | url | 비고 |
|------|---|---| --- |
| 상품 등록 | POST | http://127.0.0.1:8000/products/ | - |
| 특정 상품 수정  | POST | http://127.0.0.1:8000/products/<int:product_id> | 필드에 맞게 작성하면 수정됩니다. |
| 특정 상품 신청하기  | POST | http://127.0.0.1:8000/products/<int:product_id>/apply | 로그인된 user를 가져와 applicants로 추가합니다. |
| 검색으로 상품 조회  | GET | http://127.0.0.1:8000/products?search=테니스 | title 또는 description 에 해당 단어를 검색해서 찾습니다. |
| 전체 상품 조회  | GET | http://127.0.0.1:8000/products | - |
| 특정 상품에 펀딩하기  | POST | http://127.0.0.1:8000/products/<int:product_id>/funding | 상품에 정해진 once_funding(1회펀딩액)만큼 펀딩됩니다. |
| 정렬으로 상품 조회 | POST | http://127.0.0.1:8000/products?ordering=total_funding | id 또는 total_funding(총 펀딩금액)으로 정렬됩니다. |


