# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
from unittest.mock import patch

import pyroyale
from pyroyale.api.players_api import PlayersApi  # noqa: E501
from pyroyale.rest import ApiException
from pyroyale.exceptions import ApiTypeError

class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = PlayersApi()  # noqa: E501

    @patch('urllib3.PoolManager.request')
    def test_get_player(self, mock_get):

        mock_get.return_value.status=200
        mock_get.return_value.data = """
            {
              "tag": "#9ULGLRCL",
              "name": "AaronTraas",
              "expLevel": 13,
              "trophies": 5378,
              "bestTrophies": 5628,
              "wins": 7669,
              "losses": 7622,
              "battleCount": 21279,
              "threeCrownWins": 2368,
              "challengeCardsWon": 3398,
              "challengeMaxWins": 10,
              "tournamentCardsWon": 0,
              "tournamentBattleCount": 128,
              "role": "leader",
              "donations": 90,
              "donationsReceived": 80,
              "totalDonations": 147283,
              "warDayWins": 113,
              "clanCardsCollected": 180742,
              "clan": {
                "tag": "#JY8YVV",
                "name": "Agrassar",
                "badgeId": 16000010
              },
              "arena": {
                "id": 54000016,
                "name": "Master II"
              },
              "leagueStatistics": {
                "previousSeason": {
                  "id": "2019-06",
                  "trophies": 5577,
                  "bestTrophies": 5598
                }
              },
              "badges": [
                {
                  "name": "ClanWarWins",
                  "level": 3,
                  "maxLevel": 3,
                  "progress": 113
                }
              ],
              "achievements": [
                {
                  "name": "Team Player",
                  "stars": 3,
                  "value": 6,
                  "target": 1,
                  "info": "Join a Clan"
                }
              ],
              "cards": [
                {
                  "name": "Minions",
                  "id": 26000005,
                  "level": 11,
                  "maxLevel": 13,
                  "count": 7000,
                  "iconUrls": {
                    "medium": "https://api-assets.clashroyale.com/cards/300/yHGpoEnmUWPGV_hBbhn-Kk-Bs838OjGzWzJJlQpQKQA.png"
                  }
                }
              ],
              "currentFavouriteCard": {
                "name": "Elite Barbarians",
                "id": 26000043,
                "maxLevel": 13,
                "iconUrls": {
                  "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
                }
              },
              "starPoints": 1565
            }
        """.encode('utf-8')

        player = self.api.get_player('#9ULGLRCL')
        assert player.tag == '#9ULGLRCL'
        assert player.name == 'AaronTraas'
        assert player.exp_level == 13
        assert player.trophies == 5378
        assert player.best_trophies == 5628
        assert player.wins == 7669
        assert player.losses == 7622
        assert player.battle_count == 21279
        assert player.three_crown_wins == 2368
        assert player.challenge_cards_won == 3398
        assert player.challenge_max_wins == 10
        assert player.tournament_cards_won == 0
        assert player.tournament_battle_count >= 128
        assert player.role == 'leader'
        assert player.donations == 90
        assert player.donations_received == 80
        assert player.total_donations == 147283
        assert player.war_day_wins == 113
        assert player.clan_cards_collected == 180742
        assert player.clan.tag == '#JY8YVV'
        assert player.clan.name == 'Agrassar'
        assert player.clan.badge_id == 16000010
        assert player.arena.id == 54000016
        assert player.arena.name == 'Master II'
        assert player.league_statistics.previous_season.trophies == 5577
        assert player.league_statistics.previous_season.best_trophies == 5598
        assert player.badges[0].name == 'ClanWarWins'
        assert player.badges[0].level == 3
        assert player.badges[0].max_level == 3
        assert player.badges[0].progress == 113
        assert player.achievements[0].name == 'Team Player'
        assert player.achievements[0].stars == 3
        assert player.achievements[0].value == 6
        assert player.achievements[0].target == 1
        assert player.achievements[0].info == 'Join a Clan'
        assert player.cards[0].name == 'Minions'
        assert player.cards[0].id == 26000005
        assert player.cards[0].level == 11
        assert player.cards[0].max_level == 13
        assert player.cards[0].count == 7000
        assert player.cards[0].icon_urls.medium.startswith('https://')
        assert player.current_favourite_card.name == 'Elite Barbarians'
        assert player.current_favourite_card.id == 26000043
        assert player.current_favourite_card.max_level == 13
        assert player.current_favourite_card.icon_urls.medium.startswith('https://')
        assert player.star_points == 1565


    @patch('urllib3.PoolManager.request')
    def test_get_player_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            model = self.api.get_player('#9ULGLRCL')
            assert False

        except ApiException as e:
            print("Exception when calling PlayersApi->get_player: %s\n" % e)
            assert True

    def test_get_player_param(self):
        try:
            cardList = self.api.get_player('#9ULGLRCL', garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

    @patch('urllib3.PoolManager.request')
    def test_get_player_battles(self, mock_get):

        mock_get.return_value.status=200
        mock_get.return_value.data = """
            [
              {
                "type": "clanWarWarDay",
                "battleTime": "20190722T211817.000Z",
                "isLadderTournament": false,
                "arena": {
                  "id": 54000033,
                  "name": "Fisherman's Float"
                },
                "gameMode": {
                  "id": 72000066,
                  "name": "Showdown_Ladder"
                },
                "deckSelection": "collection",
                "team": [
                  {
                    "tag": "#9ULGLRCL",
                    "name": "AaronTraas",
                    "startingTrophies": 5378,
                    "crowns": 0,
                    "kingTowerHitPoints": 4824,
                    "princessTowersHitPoints": [
                      2731
                    ],
                    "clan": {
                      "tag": "#JY8YVV",
                      "name": "Agrassar",
                      "badgeId": 16000010
                    },
                    "cards": [
                      {
                        "name": "Elite Barbarians",
                        "id": 26000043,
                        "level": 13,
                        "maxLevel": 13,
                        "iconUrls": {
                          "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
                        }
                      }
                    ]
                  }
                ],
                "opponent": [
                  {
                    "tag": "#VCQ0GR8R",
                    "name": "Gmain",
                    "startingTrophies": 5527,
                    "crowns": 1,
                    "kingTowerHitPoints": 4824,
                    "princessTowersHitPoints": [
                      3052,
                      2416
                    ],
                    "clan": {
                      "tag": "#JVRQ9YV",
                      "name": "ZOO CLOWNS",
                      "badgeId": 16000136
                    },
                    "cards": [
                      {
                        "name": "Elite Barbarians",
                        "id": 26000043,
                        "level": 13,
                        "maxLevel": 13,
                        "iconUrls": {
                          "medium": "https://api-assets.clashroyale.com/cards/300/C88C5JH_F3lLZj6K-tLcMo5DPjrFmvzIb1R2M6xCfTE.png"
                        }
                      }
                    ]
                  }
                ]
              }
            ]
        """.encode('utf-8')

        warlog = self.api.get_player_battles('#9ULGLRCL')

        war = warlog[0]
        assert war.type == 'clanWarWarDay'
        assert war.battle_time == "20190722T211817.000Z"
        assert war.is_ladder_tournament == False
        assert war.arena.id == 54000033
        assert war.arena.name == "Fisherman's Float"
        assert war.game_mode.id == 72000066
        assert war.game_mode.name == "Showdown_Ladder"
        assert war.deck_selection == "collection"

        assert war.team[0].tag == "#9ULGLRCL"
        assert war.team[0].name == "AaronTraas"
        assert war.team[0].starting_trophies == 5378
        assert war.team[0].crowns == 0
        assert war.team[0].king_tower_hit_points == 4824
        assert war.team[0].princess_towers_hit_points[0] == 2731
        assert war.team[0].clan.tag == "#JY8YVV"
        assert war.team[0].clan.name == "Agrassar"
        assert war.team[0].clan.badge_id == 16000010
        assert war.team[0].cards[0].name == 'Elite Barbarians'
        assert war.team[0].cards[0].id == 26000043
        assert war.team[0].cards[0].level == 13
        assert war.team[0].cards[0].max_level == 13
        assert war.team[0].cards[0].icon_urls.medium.startswith('https://')

        assert war.opponent[0].tag == '#VCQ0GR8R'
        assert war.opponent[0].name == 'Gmain'
        assert war.opponent[0].starting_trophies == 5527
        assert war.opponent[0].crowns == 1
        assert war.opponent[0].king_tower_hit_points == 4824
        assert war.opponent[0].princess_towers_hit_points[0] == 3052
        assert war.opponent[0].princess_towers_hit_points[1] == 2416
        assert war.opponent[0].clan.tag == "#JVRQ9YV"
        assert war.opponent[0].clan.name == "ZOO CLOWNS"
        assert war.opponent[0].clan.badge_id == 16000136
        assert war.opponent[0].cards[0].name == 'Elite Barbarians'
        assert war.opponent[0].cards[0].id == 26000043
        assert war.opponent[0].cards[0].level == 13
        assert war.opponent[0].cards[0].max_level == 13
        assert war.opponent[0].cards[0].icon_urls.medium.startswith('https://')


    @patch('urllib3.PoolManager.request')
    def test_get_player_battles_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            model = self.api.get_player_battles('#9ULGLRCL')
            assert False

        except ApiException as e:
            print("Exception when calling PlayersApi->get_player_battles: %s\n" % e)
            assert True

    def test_get_player_battles_bad_param(self):
        try:
            cardList = self.api.get_player_battles('#9ULGLRCL', garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

    @patch('urllib3.PoolManager.request')
    def test_get_player_upcoming_chests(self, mock_get):

        mock_get.return_value.status=200
        mock_get.return_value.data = """
            {
              "items": [
                {
                  "index": 0,
                  "name": "Giant Chest"
                },
                {
                  "index": 1,
                  "name": "Silver Chest"
                }
              ]
            }
        """.encode('utf-8')

        chests = self.api.get_player_upcoming_chests('#9ULGLRCL').items

        assert len(chests) == 2
        assert chests[0].index == 0
        assert chests[0].name == 'Giant Chest'
        assert chests[1].index == 1
        assert chests[1].name == 'Silver Chest'

    @patch('urllib3.PoolManager.request')
    def test_get_player_fail(self, mock_get):

        mock_get.return_value.status=500

        try:
            model = self.api.get_player_upcoming_chests('#9ULGLRCL')
            assert False

        except ApiException as e:
            print("Exception when calling PlayersApi->get_player_upcoming_chests: %s\n" % e)
            assert True

    def test_get_player_upcoming_chests_bad_param(self):
        try:
            cardList = self.api.get_player_upcoming_chests('#9ULGLRCL', garbage='garbage')
            assert False

        except ApiTypeError as e:
            assert True

if __name__ == '__main__':
    unittest.main()
