import unittest

import config

import pyroyale
from pyroyale.rest import ApiException

configuration = config.getConfiguration()

class TestLocationsApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pyroyale.LocationsApi(pyroyale.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

