class Player:
    def __init__(self, name, nationality, team, assists, goals):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.assists = assists
        self.goals = goals

    @property
    def points(self):
        return self.assists+self.goals

    def __str__(self):
        return f"{self.name:20}{self.team} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.points):>2}"