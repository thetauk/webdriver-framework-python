import logging
import sys

class LogManager:
  @staticmethod
  def setupLogging():
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    return logger