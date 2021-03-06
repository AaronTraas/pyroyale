# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.tournament_detail import TournamentDetail  # noqa: E501
from pyroyale.rest import ApiException


class TestTournamentDetailDetail(unittest.TestCase):
    """TournamentDetailDetail unit test stubs"""

    def testDefaults(self):
        model = TournamentDetail()
        assert True

    def testConstructorInitializers(self):
        model = TournamentDetail(
            tag='tag',
            name='name',
            type='type',
            status='status',
            level_cap='level_cap',
            first_place_card_prize='first_place_card_prize',
            creator_tag='creator_tag',
            description='description',
            capacity='capacity',
            max_capacity='max_capacity',
            preparation_duration='preparation_duration',
            duration='duration',
            created_time='created_time',
            game_mode='game_mode',
            started_time='started_time',
            members_list='members_list'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.type=='type'
        assert model.status=='status'
        assert model.level_cap=='level_cap'
        assert model.first_place_card_prize=='first_place_card_prize'
        assert model.creator_tag=='creator_tag'
        assert model.description=='description'
        assert model.capacity=='capacity'
        assert model.max_capacity=='max_capacity'
        assert model.preparation_duration=='preparation_duration'
        assert model.duration=='duration'
        assert model.created_time=='created_time'
        assert model.game_mode=='game_mode'
        assert model.started_time=='started_time'
        assert model.members_list=='members_list'

    def testToDict(self):
        model = TournamentDetail(
            tag={'foo':'bar'},
            started_time=TournamentDetail(name=123),
            members_list=[TournamentDetail(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['started_time']['name']==123
        assert modelDict['members_list'][0]['name']=='name'

    def testToString(self):
        model = TournamentDetail('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = TournamentDetail('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = TournamentDetail('A')
        model_a2 = TournamentDetail('A')
        model_b  = TournamentDetail('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
