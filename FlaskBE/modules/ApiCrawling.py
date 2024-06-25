import time
import random
from modules.getAPIToJson_miramar import getApiToJson
from modules.PUBGAnalyzer import PubgAnalyzer
from modules.PostJsonToAPI import PostJsonToApi

count = 1
def APICrawling(platform, playerName, api_key):
    global count
    # DFS용도로 사용할 스택에 플레이어들의 이름을 담기
    player_stack = [playerName]

    # 반복문에 사용될 논리 스위치
    bool_switch = True

    # 반복문 시작
    while player_stack and bool_switch:
        current_player = player_stack.pop()
        print(current_player)
        try:
            GA = getApiToJson(platform, current_player, api_key)
            matchID_list = GA.getMatchIdList()
            if not matchID_list:
                continue
            # 리스트에서 매치 아이디 랜덤 초이스
            random_matchID = random.choice(matchID_list)
            print(random_matchID)

            # 뽑은 매치 아이디에서 텔레메트리 추출
            ga_tele = GA.getTelemetryJsonFromMatchId(random_matchID)

            # 클래스 생성하고 PubgAnalyzer(분석모듈) 실행
            analyzer = PubgAnalyzer(ga_tele)
            player_coordinate_list = analyzer.calculate_geometric_center()
            mag_coords_list = analyzer.print_gas_positions()
            phase_count = 1

            # PostJsonToApi(적재모듈)을 실행해서 분석된 데이터를 DB에 API Post 방식으로 적재  
            for x, y in zip(mag_coords_list, player_coordinate_list):
                # 9페이즈는 없으므로 패스
                if phase_count == 9:
                    break
                Poster = PostJsonToApi(url="http://127.0.0.1:5000", endPoint="/whitezoneAnalysis/insert/phase", phaseNum=phase_count, matchId=random_matchID, user_x=y[0], user_y=y[1], real_x=x[0], real_y=x[1])
                Poster.postData()
                phase_count += 1
            count += 1

            # 은닉 리스트는 분석기에서 추출된 플레이어 이름들의 리스트
            secret_list = analyzer.initial_player_names
            random.shuffle(secret_list)
            player_stack.extend(secret_list)
        except Exception as e:
            print(f"Error processing player {current_player}: {e}")

        # API 요청 과부하 방지를 위한 타이머
        for i in range(1, 8):
            print(i, end="\t")
            time.sleep(1)

        # 맵 이름이 miramar인 것들만 실행
        GA = getApiToJson(platform,playerName,api_key)
        matchID_list = GA.getMatchIdList()
        for i in range(len(matchID_list)):
            getMap = GA.getMapNameFromTelemetryJson(matchID_list[i])
            if getMap == "Miramar":
                bool_switch = True
            else:
                bool_switch = False
