
class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        filtered_players=[p for p in self._players if p.nationality == nationality]
        filtered_players.sort(key=lambda x: x.points, reverse=True)
        return filtered_players

