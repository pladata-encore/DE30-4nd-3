# 모듈 디렉토리
이 디렉토리는 데이터 분석에 쓰일 데이터 수집 스레드 실행을 위한 필수 모듈을 담고 있습니다. 아래는 내용과 사용 방법에 대한 개요입니다.

## 디렉토리 구조
module/  
├── __init__.py  
├── ~~__main__.py~~  
├── ApiCrawling.py  
├── getAPIToJson.py  
├── getAPIToJson_miramar.py  
├── PostJsonToAPI.py  
├── PUBGAnalyzer.py  
├── thread_collectData.py
└── README.md  

## 개요

- `__init__.py`: 이 파일은 디렉터리를 패키지로 처리해야 함을 나타냅니다.
- ~~`__main__.py`: 응용 프로그램을 실행하기 위한 메인 스크립트입니다. 모듈을 실행하기 위한 진입점 역할을 합니다.~~
- `ApiCrawling.py`: 다른 모듈들을 하나로 취합해서 실행하며, 특정 이벤트 발생 전까지 계속 실행시키는 무한루프 역할을 합니다.
- `getAPIToJson.py`: 다양한 API 데이터를 받아오고, 받아온 API에서 특정 데이터들을 뽑아내는 역할을 합니다.
- `getAPIToJson_miramar.py`: `Miramar`맵의 API데이터를 받아오고 받아온 API에서 특정 데이터들을 뽑아내는 역할을 합니다.
- `PostJsonToAPI.py`: 분석을 위해 전처리된 데이터들을 DB의 형식에 맞게 API로 POST하는 역할을 합니다.
- `PUBGAnalyzer.py`: 받아온 데이터에서 분석에 필요한 값들을 추출하고, 분석을 위해 전처리를 수행하는 역할을 합니다.
- `README.md`: 해당 디렉터리의 목적, 구조, 주요 파일 설명, 사용법 등을 적은 MarkDown 파일입니다.
- `thread_collectData.py`: Flask 백엔드 서버에 스레드 형태로 본 크롤러를 실행시키기 위해 __main__.py 파일을 약간의 수정을 거쳐 run.py 코드에서 호출될 파일입니다.

## 사용방법

- 스레드 형태로 데이터 수집기를 실행하려면 ``thread_collectData.py`` 파일에 필요한 파라미터를 넣습니다.
- ``modules.thread_collectData.start_background_task``를 호출합니다.


- 특정 모듈 실행
  - 필요에 따라 특정 모듈을 개별적으로 실행할 수도 있습니다. 예를 들어 다음과 같습니다:
    ```bash
    python -m module.PostJsonToAPI.py
    ```

- 종속성 스크립트를 실행하기 전에 필요한 종속성을 설치해야 합니다. 다음을 사용하여 이 작업을 수행할 수 있습니다:
    ```bash
    pip install requests
    ```