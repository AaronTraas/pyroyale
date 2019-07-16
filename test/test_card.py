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
from pyroyale.models.card import Card
from pyroyale.rest import ApiException


class TestCard(unittest.TestCase):
    """Card unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = Card()
        pass

    def testConstructorInitializers(self):
        model = Card(
            name='name',
            id='id',
            max_level='max_level',
            icon_urls='icon_urls'
        )

        assert model.id=='id'
        assert model.name=='name'
        assert model.max_level=='max_level'
        assert model.icon_urls=='icon_urls'

    def testToDict(self):
        model = Card(
            id=123,
            name='name',
            icon_urls=Card(name='name')
        )

        modelDict = model.to_dict()

        assert modelDict['id']==123
        assert modelDict['name']=='name'
        assert modelDict['icon_urls']['name']=='name'

    def testToString(self):
        model = Card('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = Card('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = Card('A')
        model_a2 = Card('A')
        model_b  = Card('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()