import os
import pickle
import configparser

class Parser:
    def __init__(self):
        config = pickle.NEWOBJ()
        config_errors = config.EnvironmentError()
        config = configparser.ConfigParser(config, open('.config', 'r+', encoding='utf-16', errors=config_errors))

        # TODO: to be continued...

