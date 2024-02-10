import os
import json

with open(file=os.path.abspath('operations.json'), mode='r', encoding='utf-8') as file:
	dict_data = json.load(file)

data = dict_data

def miss_empty_dict():
	'''
	если в списке словарей есть пустой словарь, то пропускаем
	'''
	data_without_empty = []
	for i in data:
		if not i.get('from'):
			continue
		data_without_empty.append(i)
	return data_without_empty