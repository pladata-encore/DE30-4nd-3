# Flask Backend Server

## 📄 개발 환경

* Python version : 3.9.10
* OS : Windows 11
* IDE : pycharm 
* Packages:
  * Flask == 3.0.3
  * Flask-SQLAlchemy == 3.1.1
  * SQLAlchemy==2.0.31
  * PyMySQL == 1.1.1
  * pip == 24.1
  * setuptools==70.1.0



## 📄 Directory Tree
### Project Tree
```
app
 ┣ blueprints
 ┃      ┣ whitezoneAnalysis
 ┃      ┃       ┣ models.py
 ┃      ┃       ┣ views.py
 ┃      ┃       ┗ __init__.py
 ┃      ┗ __init__.py
 ┣ config.py
 ┣ extensions.py
 ┗ __init__.py
```

## 📄 Database Scheme
### Phase1~8
| Column Name            | Data Type   | Constraints |                 
|------------------------|-------------|-------------|
| match_id               | VARCHAR(50) | PK          |                 
| user_geometry_center_x | REAL        | NN          |
| user_geometry_center_y | REAL        | NN          |                 
| white_zone_center_x    | REAL        | NN          |                 
| white_zone_center_y    | REAL        | NN          |                 
* `match_id`
  * 배틀그라운드 각 매치당 아이디
* `user_geometry_center_x`
  * 플레이어들의 기하학적 중심의 x좌표
* `user_geometry_center_y`
  * 플레이어들의 기하학적 중심의 y좌표
* `white_zone_center_x` 
  * 세이프티 존 발생지점 중심의 x좌표
* `white_zone_center_x`
  * 세이프티 존 발생지점 중심의 y좌표
## 📄 API Documentation


## 📍 Endpoint


### /whitezoneAnalysis/
* /phases/ : (GET) 모든 phase 데이터를 반환
* /phase/{int:phase_number} : (GET) 특정 phase 데이터를 반환
* /phase/{int:phase_number}/{int:data_number} : (GET) 특정 phase 데이터를 랜덤하게 섞어서 지정된 수만큼 반환
* /insert/phase : (POST) 새로운 phase 데이터를 삽입


## 📍 API Specification


### /whitezoneAnalysis/phases
* Request
  * Method : `GET`
* Response
  * Status : `200`
    * Body
      ```python
        {
            "Phase1": [
                {
                  "match_id": "id1",
                  "user_geometry_center_x": 0.0,
                  "user_geometry_center_y": 0.0,
                  "white_zone_center_x": 0.0,
                  "white_zone_center_y": 0.0
                }
             ],
            "Phase2": [
                {
                  "match_id": "id2",
                  "user_geometry_center_x": 1.0,
                  "user_geometry_center_y": 1.0,
                  "white_zone_center_x": 1.0,
                  "white_zone_center_y": 1.0
                }
             ],
            "Phase3": [
                {
                  "match_id": "id3",
                  "user_geometry_center_x": 3.0,
                  "user_geometry_center_y": 3.0,
                  "white_zone_center_x": 3.0,
                  "white_zone_center_y": 3.0
                }
             ],
            "Phase4": [
                {
                  "match_id": "id1",
                  "user_geometry_center_x": 4.0,
                  "user_geometry_center_y": 4.0,
                  "white_zone_center_x": 4.0,
                  "white_zone_center_y": 4.0
                }
             ],
            "Phase5": [
                {
                  "match_id": "id5",
                  "user_geometry_center_x": 5.0,
                  "user_geometry_center_y": 5.0,
                  "white_zone_center_x": 5.0,
                  "white_zone_center_y": 5.0
                }
             ],
            "Phase6": [
                {
                  "match_id": "id6",
                  "user_geometry_center_x": 6.0,
                  "user_geometry_center_y": 6.0,
                  "white_zone_center_x": 6.0,
                  "white_zone_center_y": 6.0
                }
             ],
            "Phase7": [
                {
                  "match_id": "id7",
                  "user_geometry_center_x": 7.0,
                  "user_geometry_center_y": 7.0,
                  "white_zone_center_x": 7.0,
                  "white_zone_center_y": 7.0
                }
             ],
            "Phase8": [
                {
                  "match_id": "id8",
                  "user_geometry_center_x": 8.0,
                  "user_geometry_center_y": 8.0,
                  "white_zone_center_x": 8.0,
                  "white_zone_center_y": 8.0
                }
             ],
        }
      ```

### /whitezoneAnalysis/phase/{int: phase_number}
* Request
  * Method : `GET`
* Response
  * Status : `200`
    * Body
      ```python
        {
            "Phase1": [
                {
                  "match_id": "id1",
                  "user_geometry_center_x": 0.0,
                  "user_geometry_center_y": 0.0,
                  "white_zone_center_x": 0.0,
                  "white_zone_center_y": 0.0
                }
             ]          
        }
      ```

### /whitezoneAnalysis/phase/{int: phase_number}/{int: data_number}
* Request
  * Method: `GET`
* Response
  * Status : `200`
    * Body
      ```python
        {
          "Phase2": [
          {
            "match_id": "random_id_1",
            "user_geometry_center_x": 0.0,
            "user_geometry_center_y": 0.0,
            "white_zone_center_x": 0.0,
            "white_zone_center_y": 0.0
          },
          {
            "match_id": "random_id_2",
            "user_geometry_center_x": 1.0,
            "user_geometry_center_y": 1.0,
            "white_zone_center_x": 1.0,
            "white_zone_center_y": 1.0
          },
          {
            "match_id": "random_id_3",
            "user_geometry_center_x": 2.0,
            "user_geometry_center_y": 2.0,
            "white_zone_center_x": 2.0,
           "white_zone_center_y": 2.0
          }
        ]
      }
      ```
* Error Response
  * Status : `413`
    * Body
      ```python
      {
        "error": "Payload Too Large Error",
        "message": "Input data counts exceeds the number of records in the database."
      }
      ```

### /whitezoneAnalysis/insert/phase

* Request
  * Method : `POST`
    * Body :
      ```python
        {
          "table": "phase1",
          "data": {
            "match_id": "some_id",
            "user_geometry_center_x": 0.0,
            "user_geometry_center_y": 0.0,
            "white_zone_center_x": 0.0,
            "white_zone_center_y": 0.0
          }
        }
      ``` 
* Response
  * Status : `200`
 
* Error Response
  * Status : `400`
    * 요청 형식이 JSON이 아닌 경우
    * Body
      ```python
        {
          "error": "Bad Request Error",
          "message" : "Request body must be JSON"
        }
      ```
    
  * Status : `400`
    * body의 JSON에 'table','data' 필드가 존재하지 않은 경우 
    * Body
      ```python
      {
        "error": "Bad Request Error",
        "message" : "Request must include 'table' and 'data'"
      }
      ```
  * Status : `400`
    * 'data'의 하위 필드가 없는 경우 
    * Body
      ```python
      {
        "error": "Bad Request Error",
        "message" : "Missing Data Fields"
      }
      ```
  * Status : `404`
    * 'Table' 명이 유효하지 않은 경우 
    * Body
      ```python
      {
        "error": "Not Found Error",
        "message": "Invalid table name"
      }
      ```