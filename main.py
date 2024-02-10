import os
import json

with open(file=os.path.abspath('operations.json'), mode='r', encoding='utf-8') as file:
	dict_data = json.load(file)

data = dict_data