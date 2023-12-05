import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('/home/taher/Python101/logging/ad.log', mode='w', encoding='utf-8')
handler.setLevel(logging.DEBUG)

Newformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(Newformat)
logger.addHandler(handler)

logger.debug('Hi Sir !!')