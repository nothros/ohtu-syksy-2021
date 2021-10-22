import unittest
from player import Player
from player_reader import PlayerReader
from statistics import Statistics


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class testStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_haku_palauttaa_pelaajan(self):
        player=self.statistics.search("Semenko")

        self.assertEqual(player.name, "Semenko")

    def test_haku_palauttaa_none(self):
        none_player=self.statistics.search("Pelaaja")

        self.assertEqual(none_player, None)
    
    def test_haku_palauttaa_none(self):
        none_player=self.statistics.search("Pelaaja")

        self.assertEqual(none_player, None)

    def test_team_palauttaa_oikeat(self):
        team = self.statistics.team("EDM")

        self.assertEqual(len(team), 3)   
    
    def test_top_scorers_palauttaa_oikeat(self):
        players = self.statistics.top_scorers(1)

        self.assertEqual(players[0].name, "Gretzky")   
