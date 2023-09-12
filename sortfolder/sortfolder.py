from .classes import SortFolder, NormalizeName, UnpackArchive
import os
from styles import stylize


def sort_folder_run():
    while True:

        print(
            'Enter the path to the folder in which you want to organize or enter "Back" to return to the previous menu:')
        path = input('>>> ')

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(stylize('Folder ', 'red') + path + stylize(' does not exist.', 'red'))
            continue

        sort = SortFolder(path)
        print(sort.run())
        break


def normalize_name():
    while True:

        print(
            'Enter the path of the file or folder for which you want to normalize the name or enter "Back" to return to the previous menu:')
        path = input('>>> ')

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(path + stylize(' does not exist.', 'red'))
            continue

        normalize = NormalizeName()
        print(normalize.rename(path))
        break


def unpack_archive():
    while True:

        print('Enter the path to the archive you want to unpack or enter "Back" to return to the previous menu:')
        path = input('>>> ')

        if path.lower() in ('back', "exit", "close", 'quit', 'q', '0'):
            break

        if not os.path.exists(path):
            print(path + stylize(' does not exist.', 'red'))
            continue

        unpac = UnpackArchive(path)
        print(unpac.extract())
        break


handler = {
    '1': sort_folder_run,
    '2': normalize_name,
    '3': unpack_archive,
}


def start():
    print(stylize("\nWelcome to the Sortfolder!", 'white', 'bold'))

    while True:
        print(stylize('Select a command:', 'white'))
        print('1 - Sort folder')
        print('2 - File or folder name normalization')
        print('3 - Unpack an archive')
        print('4 - Return to the main menu')
        command = input('>>> ')
        if command == '4':
            break
        elif command in handler:
            handler[command]()
        else:
            print(stylize("The command is incorrect", 'red'))
