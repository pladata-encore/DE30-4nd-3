import datetime
from datetime import datetime

class PubgAnalyzer:
    def __init__(self, data):
        self.data = data
        self.initial_player_names = self.get_all_player_names()
        self.phase_changes = self.get_phase_changes()
        self.victim_times = self.get_victim_times()
        self.coordinate_list = []
    
    def get_all_player_names(self):
        player_names = set()
        for entry in self.data:
            try:
                name = entry['character']['name']
                player_names.add(name)
            except KeyError:
                pass
        return list(player_names)
    
    def get_phase_changes(self):
        phase_changes = []
        for entry in self.data:
            try:
                if entry['_T'] == 'LogPhaseChange' and int(entry['common']['isGame']) == entry['common']['isGame']:
                    phase_changes.append([entry['phase'], entry['_D']])
            except KeyError:
                pass
        return phase_changes
    
    def get_victim_times(self):
        victim_times = []
        for entry in self.data:
            try:
                if entry['_T'] == "LogPlayerKillV2":
                    victim_times.append([entry['victim']['name'], entry['_D']])
            except KeyError:
                pass
        return victim_times
    
    def calculate_geometric_center(self):
        for phase, phase_time_str in self.phase_changes:
            phase_time = datetime.strptime(phase_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            alive_players = self.filter_alive_players(phase_time)
            x, y = self.calculate_center_for_phase(alive_players, phase_time)
            self.coordinate_list.append([x, y])
            # print(f"{phase}페이즈 기하학적 중심 {(x, y)}")
        return self.coordinate_list
    
    def filter_alive_players(self, phase_time):
        alive_players = self.initial_player_names[:]
        victim_datetime_list = [
            (name, datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ'))
            for name, dt in self.victim_times
        ]
        for name, death_time in victim_datetime_list:
            if death_time < phase_time:
                alive_players.remove(name)
        return alive_players
    
    def calculate_center_for_phase(self, alive_players, phase_time):
        x_sum, y_sum = 0, 0
        count = 0
        for player in alive_players:
            closest_time = self.find_closest_log_time(player, phase_time)
            for entry in self.data:
                try:
                    if 'character' in entry and entry['character']['name'] == player and entry['_D'] == closest_time:
                        x_sum += entry['character']['location']['x']
                        y_sum += entry['character']['location']['y']
                        count += 1
                except KeyError:
                    pass
        if count > 0:
            x = x_sum / count
            y = y_sum / count
        else:
            x, y = 0, 0
        return x, y
    
    def find_closest_log_time(self, player, phase_time):
        log_times = [
            entry['_D']
            for entry in self.data
            if 'character' in entry and entry['character']['name'] == player
        ]
        closest_time = None
        min_diff = float('inf')
        for ts in log_times:
            current_time = datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S.%fZ')
            time_diff = abs((current_time - phase_time).total_seconds())
            if time_diff < min_diff:
                min_diff = time_diff
                closest_time = ts
        return closest_time
    
    def get_gas_positions(self):
        gas_list = []
        for entry in self.data:
            try:
                if entry['gameState']['poisonGasWarningRadius'] != 0:
                    position = entry['gameState']['poisonGasWarningPosition']
                    radius = entry['gameState']['poisonGasWarningRadius']
                    if [position, radius] not in gas_list:
                        gas_list.append([position, radius])
            except KeyError:
                pass
        return gas_list
    
    def print_gas_positions(self):
        gas_list = self.get_gas_positions()
        gas_coords_list = []
        for count, gas in enumerate(gas_list, start=1):
            # print(f"{count}페이즈 실제 자기장 중심 ({gas[0]['x']},{gas[0]['y']})")
            gas_coords_list.append([gas[0]['x'],gas[0]['y']])
        return gas_coords_list