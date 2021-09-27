import os
import re
import codecs
from os import walk

directory = input("Enter full directory: ")
fileFormat = input("Enter file format: ")
searchText = input("Enter searching text: ")

def main(directory: str, fileFormat: str, searchText: str):
	print('Search started!\n\n')

	for (dirPath, dirNames, fileNames) in walk(directory):
		num = 0
		while num < len(fileNames):
			fileName = fileNames[num]

			file = codecs.open(f'{dirPath}/{fileName}', 'r', encoding='utf8')
			if fileName.endswith(fileFormat):
				match = re.search(searchText, file.read())
				if match is not None:
					print(f'{dirPath}/{fileName}'.replace(f'{directory}\\', ''))
			num += 1

	print('\n\nSearch finished!\n')
	nextSearch(directory, fileFormat, searchText)
	

def nextSearch(directory: str, fileFormat: str, searchText: str):
	print('1. Continue with different text')
	print('2. Continue searching in a different path\n')

	result = input("Choose your option: ")
	if result == '1':
		print('\nContinue with different text\n')
		searchText = input("Enter searching text: ")
		main(directory, fileFormat, searchText)
	elif result == '2':
		print('\nContinue searching in a different path\n')
		directory = input("Enter full directory: ")
		fileFormat = input("Enter file format: ")
		searchText = input("Enter searching text: ")
		main(directory, fileFormat, searchText)
	else:
		print('\nIncorrect unswer\n\n')
		nextSearch(directory, fileFormat, searchText)

main(directory, fileFormat, searchText)