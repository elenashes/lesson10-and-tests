import app
import sys
import unittest
from pathlib import Path
import os


BASENAME = 'lesson18-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ArchitectureTestCase(SkyproTestCase):
    pass

if __name__ == "__main__":
    unittest.main()