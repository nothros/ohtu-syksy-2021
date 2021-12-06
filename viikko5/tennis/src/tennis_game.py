class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0

    def get_name(self):
        return self.player_name

    def won(self):
        self.player_score+=1
    
    def get_score(self):
        return self.player_score

class ScoreBoard:
    def __init__(self, player1_name, player2_name) -> None:
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.score_string = ["Love", "Fifteen", "Thirty", "Forty"]
    
    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.won()
        else:
            self.player2.won()

    def score_strings(self, score):
        return f"{self.score_string[score]}"

    def score_to_string(self):
        score_player1 = self.player1.get_score()
        score_player2 = self.player2.get_score()
        return self.score_string[score_player1]+"-"+self.score_string[score_player2]

    def tie_to_string(self):
        score = self.player1.get_score()
        if  score > 3:
            return "Deuce"
        return self.score_strings(score)+"-All"

    def win_to_string(self):
        return "Win for "+self.get_leader()

    def tie(self):
        return self.player1.get_score() == self.player2.get_score()

    def get_leader(self):
        winner = None
        if self.player1.get_score() > self.player2.get_score():
            winner = self.player1.get_name()
        else:
            winner = self.player2.get_name()
        return winner

    def winner(self):
        winner = None
        if max(self.player1.get_score(), self.player2.get_score()) > 3:
            winner=self.get_leader()
        return winner

    def both_over_thirty(self):
        return self.player1.get_score() >= 3 and self.player2.get_score() >= 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scoreboard = ScoreBoard(player1_name, player2_name)
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        self.scoreboard.won_point(player_name)

    def get_score(self):
        score = ""
        if self.scoreboard.tie():
            score = self.scoreboard.tie_to_string()

        elif self.scoreboard.winner():
            score = self.scoreboard.win_to_string()

        elif not self.scoreboard.both_over_thirty():
            score = self.scoreboard.score_to_string()
        
        else:
            score = "Advantage"+self.scoreboard.get_leader()

        return score
