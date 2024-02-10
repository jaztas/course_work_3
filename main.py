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


def get_executed():
	'''
	получает список всех EXECUTED операций
	'''
	executed_operations = [i for i in miss_empty_dict() if i and i['state'] == 'EXECUTED']
	return executed_operations


def get_data_for_sort(x):
	'''
	функция принимает то, по чему в дальнейшем будет сортироваться ф-ия sorted()
	'''
	return x['date']


def sorted_operations():
	'''
	сортирует по дате от настоящего к прошлому
	'''
	operations_list = sorted(get_executed(), key=get_data_for_sort, reverse=True)
	return operations_list