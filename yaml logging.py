
"""
version: 1
disable_existing_loggers: True
formatters:
    standard:
        format: '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
handlers:
    file_handler:
        class: logging.FileHandler
        level: INFO
        formatter: standard
        filename: data/file.log
loggers:
    "__main__":
        level: INFO
        handlers: ['file_handler']
        propagate: no




Above is a simple YAML config file that has the three most essential components in every logging configuration, which are

Formatters — The logging output format. In the above case, we have the time, the script name, the log level and the message.
Handlers — which specify how, where, and frequency of the logging output, the log level to start storing from, file path, message format etc.
Loggers — helps to aggregate all the handlers specified earlier.


Typically if using File config or Dict config format, all you need to do is add the config file name as an argument to logging.config.dictConfig() or logging.config.fileConfig()(depending on if you use a file or Dict format) and you are good to go. But since you are using YAML, you first need to read the config file using a YAML reader and then add it to logging.config.dictConfig() like this


#assuming the log config file name is log.yml
with open('log.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

#read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


A complete sample code looks like this (assume the script name is called helper_code.py).

import logging
import logging.config
import yaml

# read tjhe yaml file
with open('log.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
# read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


"""