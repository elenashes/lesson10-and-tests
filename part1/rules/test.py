import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup


BASENAME = 'lesson10-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class WelcomeTestCase(SkyproTestCase):
    def setUp(self):
        file = open("rules.html", 'r')
        soup = BeautifulSoup(file)
        breakpoint()
        pass

    def test_one(self):
        pass

if __name__ == "__main__":
    unittest.main()