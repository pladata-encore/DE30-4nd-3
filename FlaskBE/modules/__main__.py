from ApiCrawling import APICrawling
from getAPIToJson_miramar import getApiToJson

# 인스턴스 설정
platform = 'steam'
playerName = 'WL_sir'
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwOTczZWUxMC0wOTZlLTAxM2QtY2NlNi0zMmFkODc5M2Q4OGIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNzE4MDM0MTc4LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImhlaGViYWxzc2EifQ.ADpdC0UInjTkDeVJXNjtZvMf4rNQAyrzQqWuPGvuteE'

GA = getApiToJson(platform,playerName,api_key)
matchID_list = GA.getMatchIdList()
for i in range(len(matchID_list)):
    getMap = GA.getMapNameFromTelemetryJson(matchID_list[i])
    if getMap == "Miramar":
        print("miramar")
        APICrawling(platform, playerName, api_key)
    else:
        continue