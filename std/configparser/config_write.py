# Configuration file parser
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['gosber.org'] = {}
config['gosber.org']['User'] = 'hg'
config['g8gg.server.com'] = {}
topsecret = config['g8gg.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
