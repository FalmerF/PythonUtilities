import os
import re
import codecs
from os import walk

directory = input("Enter full directory: ")
fileFormat = input("Enter file format: ")
searchText = input("Enter searching text: ")
replaceText = input("Enter replace text: ")

def main(directory: str, fileFormat: str, searchText: str, replaceText: str):
	print('Search started!\n\n')

	for (dirPath, dirNames, fileNames) in walk(directory):
		num = 0
		while num < len(fileNames):
			fileName = fileNames[num]

			file = codecs.open(f'{dirPath}/{fileName}', 'r', encoding='utf8')
			if fileName.endswith(fileFormat):
				content = file.read()
				match = re.search(searchText, content)
				if match is not None:
					content = content.replace(searchText, replaceText)
					file = codecs.open(f'{dirPath}/{fileName}', 'w', encoding='utf8')
					file.write(content)
					file.close()
					print(f'Modified {dirPath}/{fileName}'.replace(f'{directory}\\', ''))
			num += 1

	print('\n\nReplaceing finished!\n')
	nextSearch(directory, fileFormat)
	

def nextSearch(directory: str, fileFormat: str):
	print('1. Continue with different text')
	print('2. Continue searching in a different path\n')

	searchText = ''
	result = input("Choose your option: ")
	if result == '1':
		print('\nContinue with different text\n')
		searchText = input("Enter searching text: ")
		replaceText = input("Enter replace text: ")
		main(directory, fileFormat, searchText, replaceText)
	elif result == '2':
		print('\nContinue searching in a different path\n')
		directory = input("Enter full directory: ")
		fileFormat = input("Enter file format: ")
		searchText = input("Enter searching text: ")
		replaceText = input("Enter replace text: ")
		main(directory, fileFormat, searchText, replaceText)
	else:
		print('\nIncorrect unswer\n\n')
		nextSearch(directory, fileFormat)

main(directory, fileFormat, searchText, replaceText)