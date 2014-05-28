__author__ = 'Ashkan'


import sys
import logging


logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger("KBDegree")     # pylint: disable=C0103

logger.setLevel(logging.DEBUG)
