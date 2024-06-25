import requests

# 분석모듈로 분석된 데이터를 DB에 API로 전송하여 적재하는 모듈
class PostJsonToApi:
    def __init__(self, url, endPoint, phaseNum, matchId, user_x, user_y, real_x, real_y):
        self.url = url
        self.endPoint = endPoint
        self.phaseNum = phaseNum
        self.matchId = matchId
        self.user_x = user_x
        self.user_y = user_y
        self.real_x = real_x
        self.real_y = real_y
        self.body = {
            "table": f"phase{self.phaseNum}",
            "data": {
                "match_id": str(self.matchId),
                "user_geometry_center_x": float(self.user_x),   
                "user_geometry_center_y": float(self.user_y),
                "white_zone_center_x": float(self.real_x),
                "white_zone_center_y": float(self.real_y)
            }
        }
    
    # 디버깅용 프린트, POST 요청으로 데이터를 전송
    def postData(self):
        headers = {'Content-Type': 'application/json'}
        url = self.url + self.endPoint
        response = requests.post(url, json=self.body, headers=headers)
        print(f"매치 아이디 : {self.matchId}")
        print(f"페이즈 남바 : {self.phaseNum}")
        print(f"바디 : {self.body}")
        if response.status_code == 200:
            print(f"Response content: {response.content}")
        elif response.status_code == 404:
            print(f"Response content: {response.content}")
        else:
            print(f"Unexpected status code: {response.status_code}")
            print(f"Response content: {response.content}")