import threading


def background_task():
    from modules.getAPIToJson_miramar import getApiToJson
    from modules.ApiCrawling import APICrawling
    print("Background task has started...")

    # 인스턴스 설정
    platform = 'PLATFORM'
    playerName = 'PLAYER_NAME'
    api_key = 'YOUR_API_KEY'

    GA = getApiToJson(platform, playerName, api_key)
    matchID_list = GA.getMatchIdList()
    for i in range(len(matchID_list)):
        getMap = GA.getMapNameFromTelemetryJson(matchID_list[i])
        if getMap == "Miramar":
            print("miramar")
            APICrawling(platform, playerName, api_key)
        else:
            continue


def start_background_task():
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()
