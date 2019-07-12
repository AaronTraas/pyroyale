from __future__ import absolute_import

import pyroyale
from pyroyale._version import __version__
import unittest

def testVersion():
    assert len(__version__) >= 5

