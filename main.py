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


def five_last_operations(data):
	count = 0
	for i in sorted_operations():
		if not i.get('from'):
			continue
		elif count == 5:
			break
		count += 1
		print(f"{i['date'][:10].replace('-', '.')} {i['description']}")
		print(
			f"{i['from'].split()[0]} {i['from'].split()[1][:4]} {i['from'].split()[1][4:6]}** **** {i['from'].split()[-1][8:12]} -> Счет **{i['to'][-4:]}")
		print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
		print()


if __name__ == "__main__":
	five_last_operations(data)