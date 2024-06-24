import time
import random
from getAPIToJson import getApiToJson
from PUBGAnalyzer import PubgAnalyzer
from PostJsonToAPI import PostJsonToApi

count = 1
def APICrawling(platform, playerName, api_key):
    global count
    player_stack = [playerName]
    while player_stack:
        current_player = player_stack.pop()
        print(current_player)
        try:
            GA = getApiToJson(platform, current_player, api_key)
            matchID_list = GA.getMatchIdList()
            if not matchID_list:
                continue
            random_matchID = random.choice(matchID_list)
            print(random_matchID)
            ga_tele = GA.getTelemetryJsonFromMatchId(random_matchID)
            analyzer = PubgAnalyzer(ga_tele)
            player_coordinate_list = analyzer.calculate_geometric_center()
            mag_coords_list = analyzer.print_gas_positions()
            phase_count = 1
            for x, y in zip(mag_coords_list, player_coordinate_list):
                if phase_count == 9:
                    break
                Poster = PostJsonToApi(url="http://192.168.0.79:5000", endPoint="/whitezoneAnalysis/insert/phase", phaseNum=phase_count, matchId=random_matchID, user_x=y[0], user_y=y[1], real_x=x[0], real_y=x[1])
                Poster.postData()
                phase_count += 1
            count += 1
            secret_list = analyzer.initial_player_names
            random.shuffle(secret_list)
            player_stack.extend(secret_list)
        except Exception as e:
            print(f"Error processing player {current_player}: {e}")
        for i in range(1, 8):
            print(i, end="\t")
            time.sleep(1)