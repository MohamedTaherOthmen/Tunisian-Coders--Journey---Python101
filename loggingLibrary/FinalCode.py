# after two nights of hard learning I've master almost all logging's Labrary functions
import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler('/home/taher/Python101/loggingLibrary/Logs/finallog.log')
Format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.setLevel(logging.DEBUG)
handler.setLevel(logging.INFO)
handler.setFormatter(Format)
logger.addHandler(handler)

logger.debug('This The Debug Message')
logger.info('This The Info Message')
logger.warning('This The Warning Message')
logger.error('This The Error Message')
