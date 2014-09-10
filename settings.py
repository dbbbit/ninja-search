import logging
from logging.handlers import RotatingFileHandler

#: logging config
LOGGING_PATH = '/var/log/ninja-search/search_error.log'

handler = RotatingFileHandler(LOGGING_PATH, maxBytes=1000000)
handler.setLevel(logging.INFO)

#: debug?
DEBUG = False
