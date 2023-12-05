import logging

logger = logging.getLogger('Tahoura')

# Enter Logging lvl :
loglevel = str(input('Select Logging level = '))
# The getattr() function returns the value of the specified attribute from the specified object.
# Isn't in the structure gives a none integer output
num_lvl = getattr(logging, loglevel.upper(), None)
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
if not isinstance(num_lvl, int):
    raise ValueError('Invalid log level : %s' % loglevel)

# By Default logging output prompted in Terminal
# Sometimes you want your logging output to be printed in a spific log file :
# log messages that are equal or higher than level 2 (DEBUG) will be prompted
# We can customize log messages by adding date, time, name, levelname
logging.basicConfig(
    filename='/home/taher/Python101/loggingLibrary/Logs/logs.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt = '%m/%d/%Y %I:%M:%S %p',
    filemode = 'w',
    level=num_lvl
)

#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

