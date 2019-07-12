import unittest

import config

import pyroyale
from pyroyale.rest import ApiException

configuration = config.getConfiguration()

class TestPlayersApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pyroyale.PlayersApi(pyroyale.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_player_AaronTraas(self):
        try:
            player = self.api.get_player('#9ULGLRCL')
            assert player.tag == '#9ULGLRCL'
            assert player.name == 'AaronTraas'
            assert player.exp_level >= 13
            assert player.trophies >= 4000
            assert player.best_trophies >= 4000
            assert player.wins >= 7000
            assert player.losses >= 7000
            assert player.battle_count >= 20000
            assert player.three_crown_wins >= 2000
            assert player.challenge_cards_won >= 2000
            assert player.challenge_max_wins >= 10
            assert player.tournament_cards_won >= 0
            assert player.tournament_battle_count >= 100
            assert player.role.lower() in ['leader', 'coleader', 'elder', 'member']
            assert player.donations >= 0
            assert player.donations_received >= 0
            assert player.total_donations >= 100000
            assert player.war_day_wins >= 100
            assert player.clan_cards_collected >= 100000
            assert player.clan.tag == '#JY8YVV'
            assert player.clan.name == 'Agrassar'
            assert player.clan.badge_id >= 16000000
            assert player.arena.id >= 54000000
            assert player.league_statistics.current_season.trophies > 4000
            assert player.league_statistics.current_season.best_trophies > 4000
            assert player.league_statistics.previous_season.trophies > 4000
            assert player.league_statistics.previous_season.best_trophies > 4000
            assert player.league_statistics.best_season.trophies > 4000
            assert len(player.badges) > 5
            assert len(player.achievements) > 5
            assert len(player.cards) > 50
            assert len(player.current_favourite_card.name) > 2
            assert player.current_favourite_card.id >= 26000000
            assert player.current_favourite_card.max_level > 4
            assert player.current_favourite_card.icon_urls.medium.startswith('https://')
            assert player.star_points >= 0

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player(): %s\n" % e)
            assert False

    def test_player_AaronTraas_upcoming_chests(self):
        try:
            chests = self.api.get_player_upcoming_chests('#9ULGLRCL').items

            assert len(chests) > 10
            assert chests[0].index >= 0
            assert len(chests[0].name) >= 2
            assert chests[0].name.lower().endswith('chest')

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player_upcoming_chests(): %s\n" % e)
            assert False

    def test_player_AaronTraas_battle_log(self):
        try:
            battles = self.api.get_player_battles('#9ULGLRCL')

            assert len(battles) >= 1

            battle = battles[0]

            assert battle.type in ['PvP', 'clanWarWarDay', 'clanWarCollectionDay', 'challenge']
            assert len(battle.team) >= 1
            assert len(battle.opponent) >= 1
            assert battle.game_mode.id >= 72000000
            assert len(battle.game_mode.name) >= 2

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player_battles(): %s\n" % e)
            assert False

