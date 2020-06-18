import os
import sys
import yaml
from yaml import SafeLoader, parser, scanner

this_folder = os.path.dirname(os.path.abspath(__file__))
yaml_file = 'test_yaml.yaml'

file_path = '{}/{}'.format(this_folder,yaml_file)

try:
    with open(file_path, 'r') as f:
        my_file_str = f.read()
except IOError as e:
    sys.exit(str(e))
try:
    cfg = yaml.load(my_file_str, Loader=SafeLoader)
except (parser.ParserError, scanner.ScannerError) as e:
    sys.exit(str(e))

food_whitelist = cfg['food_whitelist']
food_blacklist = cfg['food_blacklist']
print(food_whitelist)
print(food_blacklist)
print(type(food_whitelist))
print(type(food_blacklist))