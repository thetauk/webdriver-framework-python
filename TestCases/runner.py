import unittest
from unittest import TextTestRunner

from tauk.config import TaukConfig
from tauk.listeners.unittest_listener import TaukListener
from tauk.tauk_webdriver import Tauk

from Resources.DataConfig import DataConfig

if __name__ == '__main__':
  Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN, project_id=DataConfig.TAUK_PROJECT_ID))
  loader = unittest.TestLoader()
  suite = loader.discover("./", pattern = "test*.py")
  alltests = unittest.TestSuite((suite))
  unittest.TextTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  #punittest.main(testRunner=TextTestRunner(resultclass=TaukListener))