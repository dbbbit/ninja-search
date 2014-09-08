import logging
from logging.handlers import RotatingFileHandler

#: logging config

LOGGING_PATH = '/tmp/ninja-search.log'

handler = RotatingFileHandler(LOGGING_PATH, maxBytes=1000000)
handler.setLevel(logging.INFO)
