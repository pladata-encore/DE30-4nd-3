import requests
import json

class getApiToJson:
    # 초기 설정 플랫폼명, 닉네임, 개인 API 키, 베이스URL, 헤더 
    def __init__(self, platform, playerName, apikey):
        self.platform = platform
        self.playerName = playerName
        self.apikey = apikey
        self.id_search_by_nickname_url = f"https://api.pubg.com/shards/{self.platform}/players?filter[playerNames]="
        self.apis_header = {
            "Authorization": f"Bearer {self.apikey}",
            "Accept": "application/vnd.api+json"
        }
        self.telemetry_header = {
            "Accept": "application/vnd.api+json",
            "Accept-Encoding": "gzip"
        }
        self.id_response = requests.get(self.id_search_by_nickname_url + self.playerName, headers=self.apis_header)
    # 플레이어 ID 추출
    def getPlayerId(self):
        playerId = self.id_response.json()['data'][0]['links']['self'].split("/")[-1]
        return f"playerid : {playerId}"
    
    # 플레이어의 매치ID를 리스트로 반환
    def getMatchIdList(self):
        match_datas = self.id_response.json()['data'][0]['relationships']['matches']['data']
        match_data_lists = [match['id'] for match in match_datas]
        print(f"검색된 matchId 수 : {len(match_data_lists)}")
        return match_data_lists
    
    # 매치ID 리스트를 기반으로 각각의 요소에 대응하는 텔레메트리 URL 추출해서 리스트로 반환
    def getTelemetryURLFromList(self, match_data_lists):
        match_search_by_matchId_url = f"https://api.pubg.com/shards/{self.platform}/matches/"
        telemetryURLList = []
        for match_IDs in match_data_lists:
            match_data = requests.get(match_search_by_matchId_url + match_IDs, headers=self.apis_header,params=self.params)
            telemetryId = match_data.json()['data']['relationships']['assets']['data'][0]['id']
            print(f"matchId : {match_IDs}\ntelemetryId : {telemetryId}")
            for included_item in match_data.json()['included']:
                if included_item['type'] == 'asset':
                    telemetry_url = included_item['attributes']['URL']
                    telemetryURLList.append(telemetry_url)
                    print(telemetry_url, "\n")
        return telemetryURLList
    
    # 텔레메트리 URL로부터 텔레메트리 Json을 반환
    def getTelemtryJsonFromTelemetryURL(self, telemetry_url):
        telemetry_response = requests.get(telemetry_url, headers=self.telemetry_header)
        return telemetry_response.json()
    
    # 매치 ID 하나로 텔레메트리 Json을 반환
    def getTelemetryJsonFromMatchId(self, matchId):
        self.matchId = matchId
        match_search_by_matchId_url = f"https://api.pubg.com/shards/{self.platform}/matches/"
        match_data = requests.get(match_search_by_matchId_url + self.matchId, headers=self.apis_header)
        for included_item in match_data.json()['included']:
            if included_item['type'] == 'asset':
                self.telemetryURL = included_item['attributes']['URL']
        # print(f"matchId : {self.matchId}\ntelemetryURL : {self.telemetryURL}\n")
        telemetry_response = requests.get(self.telemetryURL, headers=self.telemetry_header)
        return telemetry_response.json()
    
    # 받아온 텔레메트리 데이터를 원하는 형식으로 저장
    def saveJsonFile(self, JsonResponse, fileName, filetype):
        filetype = "." + f"filetype"
        self.fileName = fileName + filetype
        with open(self.fileName, 'w') as json_file:
            json.dump(JsonResponse, json_file, indent=4)
    
    # 엔드포인트별로 다른 API 데이터를 반환하는 함수
    def getOtherApiToJson(self, endPoints):
        url = f"https://api.pubg.com/shards/{self.platform}"
        r = requests.get(url + endPoints, headers=self.apis_header)
        return r.json()
    
    # 매치 ID에 대응하는 텔레메트리를 찾고 맵 이름을 추출하여 반환
    def getMapNameFromTelemetryJson(self,matchId):
        self.data = self.getTelemetryJsonFromMatchId(matchId)
        for i in range(len(self.data)):
            try:
                if self.data[i]['mapName'] == "Desert_Main":
                    return "Miramar"
                elif self.data[i]['mapName'] == "Erangel_Main":
                    return "Erangel"
                elif self.data[i]['mapName'] == "Savage_Main":
                    return "Sanhok"
                elif self.data[i]['mapName'] == "Neon_Main":
                    return "Deston"
                elif self.data[i]['mapName'] == "Tiger_Main":
                    return "Taego"
                elif self.data[i]['mapName'] == "DihorOtok_Main":
                    return "Karakin"
                elif self.data[i]['mapName'] == "Baltic_Main":
                    return "Vikendi"
                else:
                    return self.data[i]['mapName']
            except:
                pass