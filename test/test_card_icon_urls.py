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
from pyroyale.models.card_icon_urls import CardIconUrls  # noqa: E501
from pyroyale.rest import ApiException


class TestCardIconUrls(unittest.TestCase):
    """CardIconUrls unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = CardIconUrls()
        pass

    def testConstructorInitializers(self):
        model = CardIconUrls(
            medium='medium'
        )

        assert model.medium=='medium'

    def testToDict(self):
        model = CardIconUrls(
            medium='medium'
        )
        modelDict = model.to_dict()
        assert modelDict['medium']=='medium'

        model = CardIconUrls(
            medium=123
        )
        modelDict = model.to_dict()
        assert modelDict['medium']==123

        model = CardIconUrls(
            medium={'foo': 'bar'}
        )
        modelDict = model.to_dict()
        assert modelDict['medium']['foo']=='bar'

        model = CardIconUrls(
            medium=CardIconUrls(medium='medium')
        )
        modelDict = model.to_dict()
        assert modelDict['medium']['medium']=='medium'

        model = CardIconUrls(
            medium=[CardIconUrls(medium='medium')]
        )
        modelDict = model.to_dict()
        assert modelDict['medium'][0]['medium']=='medium'

    def testToString(self):
        model = CardIconUrls('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = CardIconUrls('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = CardIconUrls('A')
        model_a2 = CardIconUrls('A')
        model_b  = CardIconUrls('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
