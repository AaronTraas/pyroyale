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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConstructorInitializers(self):
        model = TournamentDetail(
            items='items',
            started_time='started_time',
            members_list='members_list'
        )

        assert model.items=='items'
        assert model.started_time=='started_time'
        assert model.members_list=='members_list'

    def testToDict(self):
        model = TournamentDetail(
            started_time=123,
            members_list=[TournamentDetail(items='items')]
        )

        modelDict = model.to_dict()

        assert modelDict['started_time']==123
        assert modelDict['members_list'][0]['items']=='items'

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
