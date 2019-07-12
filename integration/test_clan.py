import unittest

import config

import pyroyale
from pyroyale.rest import ApiException

configuration = config.getConfiguration()

class TestClansApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pyroyale.ClansApi(pyroyale.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_clan_agrassar(self):
        try:
            clan = self.api.get_clan('#JY8YVV')
            assert clan.clan_war_trophies > 0
            for member in clan.member_list:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'AaronTraas'
                    assert member.exp_level >= 13
                    assert member.trophies >= 4000
                    assert member.arena.id >= 54000000
                    assert member.role.lower() in ['leader', 'coleader', 'elder', 'member']
                    assert member.clan_rank in range(1,50)
                    assert member.previous_clan_rank in range(1,50)
                    assert member.donations >= 0
                    assert member.donations_received >= 0
                    assert member.clan_chest_points >= 0

        except ApiException as e:
            print("Exception when calling CardsClan->get_clan: %s\n" % e)
            assert False


    def test_clan_agrassar_members(self):
        try:
            members = self.api.get_clan_members('#JY8YVV')
            for member in members.items:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'AaronTraas'
                    assert member.exp_level >= 13
                    assert member.trophies >= 4000
                    assert member.arena.id >= 54000000
                    assert member.role.lower() in ['leader', 'coleader', 'elder', 'member']
                    assert member.clan_rank in range(1,50)
                    assert member.previous_clan_rank in range(1,50)
                    assert member.donations >= 0
                    assert member.donations_received >= 0
                    assert member.clan_chest_points >= 0

        except ApiException as e:
            print("Exception when calling CardsClan->get_clan_members: %s\n" % e)
            assert False

    def test_clan_agrassar_warlog(self):
        try:
            warlog = self.api.get_clan_war_log('#JY8YVV')
            assert len(warlog.items) in range(0,11)
            for war in warlog.items:
                assert war.season_id > 0
                assert len(war.participants) in range(1,50)
                assert len(war.standings) in range(1,50)
                for standing in war.standings:
                    if standing.clan.tag == '#JY8YVV':
                        assert standing.clan.name.lower() == 'agrassar'
                    assert standing.clan.badge_id > 0
                    assert standing.clan.clan_score >= 0
                    assert standing.clan.participants in range(1,50)
                    assert standing.clan.battles_played in range(0,50)
                    assert standing.clan.wins >= 0
                    assert standing.clan.crowns >= 0

        except ApiException as e:
            print("Exception when calling CardsClan->get_clan_members: %s\n" % e)
            assert False

    def test_clan_agrassar_current_war(self):
        try:
            war = self.api.get_current_war('#JY8YVV')
            assert war.state in ['notInWar','collectionDay','warDay']

        except ApiException as e:
            print("Exception when calling CardsClan->get_clan_members: %s\n" % e)
            assert False

    def test_clan_search_agrassar(self):
        try:
            clans = self.api.search_clans(name='agrassar')
            assert len(clans.items) >= 1
            found = False
            for clan in clans.items:
                if clan.tag == '#JY8YVV':
                    assert clan.name == 'Agrassar'
                    found = True
            assert found

        except ApiException as e:
            print("Exception when calling CardsClan->get_clan_members: %s\n" % e)
            assert False

