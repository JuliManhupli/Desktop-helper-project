import os
import py7zr
import shutil
from string import ascii_letters, digits
from styles import stylize


TRANSLITERATION = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
                'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
                'ы': 'y', 'ь': '', 'э': 'e', 'є': 'ye', 'ё': 'yo', 'ю': 'yu', 'я': 'ya', 'Ё': 'Yo','Є': 'Ye', 'Ї': 'Yi', 'А': 'A', 'Б': 'B',
                'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'І': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L',
                'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
                'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
                }


CATEGORIES = {'archives': ('zip', 'gz', 'tar', '7z'),
                'audio': ('mp3', 'ogg', 'wav', 'amr', 'flac'),
                'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'odt'),
                'images': ('jpeg', 'png', 'jpg', 'svg', 'webp'),
                'video': ('avi', 'mp4', 'mov', 'mkv'),
                'other': ()
                }

class NormalizeName:
    """Class for normalizing file names."""

    @staticmethod
    def get_normal_name(file_name: str) -> str:
        """Normalize a file name by transliterating and replacing invalid characters."""

        correct_characters = ascii_letters + digits + '_'
        file_name, extension = os.path.splitext(file_name)
        file_name = ''.join([char if char in correct_characters else TRANSLITERATION[char]
                            if char in TRANSLITERATION else '_'
                            for char in file_name])

        while '__' in file_name:
            file_name = file_name.replace('__', '_')

        return file_name + extension

    @staticmethod
    def check_name_conflict(folder_path: str, name: str) -> str:
        """Check for name conflicts and resolve by appending counter."""

        files = os.listdir(folder_path)

        if name not in files:
            return name

        filename, extension = os.path.splitext(name)
        counter = 1
        new_file_name = f"{filename}_{counter}{extension}"

        while new_file_name in files:
            counter += 1
            new_file_name = f"{filename}_{counter}{extension}"

        return new_file_name

    @classmethod
    def rename(cls, full_file_path: str) -> str:
        """Rename a file by normalizing name and resolving conflicts."""

        file_name = os.path.basename(full_file_path)
        file_path = os.path.dirname(full_file_path)

        new_file_name = cls.get_normal_name(file_name)

        if new_file_name == file_name:
            return  stylize('The name ', 'yellow') + file_name + stylize(' does not need correction.', 'yellow')

        new_file_name = cls.check_name_conflict(file_path, new_file_name)

        new_full_file_path = os.path.join(file_path, new_file_name)

        os.rename(full_file_path, new_full_file_path)

        return file_name + stylize(' was changed to ', 'green') + new_file_name + stylize(' successfully.', 'green')


class UnpackArchive:
    """Class for extracting archive files."""

    def __init__(self, archive_path: str) -> None:
        """Initialize with archive path and destination folder."""

        self.archive_path = archive_path
        self.destination_folder_path = os.path.dirname(archive_path)

    def extract(self) -> str:
        """Extract archive contents to destination folder."""

        if not os.path.exists(self.archive_path):
            return stylize('Archive ', 'red') + self.archive_path + stylize(' does not exist.', 'red')
        if not os.path.exists(self.destination_folder_path):
            return stylize('Folder ', 'red') + self.destination_folder_path + stylize(' does not exist.', 'red')

        extension = os.path.splitext(self.archive_path)[1][1:]

        message = stylize('archive ', 'green') + self.archive_path + stylize(' was extracted successfully.', 'green')

        if extension == '7z':
            with py7zr.SevenZipFile(self.archive_path, mode='r') as z:
                z.extractall(path=self.destination_folder_path)
        elif extension in CATEGORIES['archives']:
            shutil.unpack_archive(self.archive_path, self.destination_folder_path)
        else:
            message = stylize("I can't work with such files", 'red')

        return message


class SortFolder:
    """Class for sorting files into categories."""

    def __init__(self, path) -> None:
        """Initialize with base folder path."""
        self.BASE_FOLDER = path



    def create_categories(self) -> None:
        """
        Create category folders if they don't exist.

        This function iterates over the defined categories and checks if each category folder
        exists in the BASE_FOLDER. If a category folder doesn't exist, it creates the folder.
        """

        for folder_name in CATEGORIES:
            folder_path = os.path.join(self.BASE_FOLDER, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)



    @staticmethod
    def normalize(file_name: str) -> str:
        """
        Normalize the file name by removing illegal characters and applying transliteration.

        This function takes a file name as input and normalizes it by  replacing characters
        that are not in the set of allowed characters (ascii letters, digits, and underscore).
        It also applies transliteration to replace any non-ASCII characters with their
        corresponding ASCII equivalents.

        Args:
            file_name (str): The file name to normalize.

        Returns:
            str: The normalized file name."""

        correct_characters = ascii_letters + digits + '_'
        file_name, extension = os.path.splitext(file_name)
        file_name = ''.join([char if char in correct_characters else TRANSLITERATION[char]
                            if char in TRANSLITERATION else '_'
                            for char in file_name])

        return file_name + extension


    @staticmethod
    def check_name_conflict(folder_path: str, name: str) -> str:
        """
        Check if a file name conflicts with existing files in a folder and resolves the conflict.

        This function checks if the given name conflicts with any existing files in the specified
        folder. If there is a conflict, it appends a counter to the name to make it unique.

        Args:
            folder_path (str): The path to the folder.
            name (str): The file name to check for conflicts.

        Returns:
            str: The resolved file name without conflicts.
        """

        files = os.listdir(folder_path)

        if name not in files:
            return name

        filename, extension = os.path.splitext(name)
        counter = 1
        new_filename = f"{filename}_{counter}{extension}"

        while new_filename in files:
            counter += 1
            new_filename = f"{filename}_{counter}{extension}"

        return new_filename

    @classmethod
    def rename_file(cls, destination_folder: str, full_file_path: str) -> str:
        """
        Rename a file and resolve naming conflicts.

        This function renames the file at the given full file path by normalizing the file name.
        If the new file name conflicts with existing files in either the source folder or the
        destination folder, it resolves the conflicts.

        Args:
            destination_folder (str): The path to the destination folder.
            full_file_path (str): The full path to the file.

        Returns:
            str: The new full file path of the renamed file.
        """

        file_name = os.path.basename(full_file_path)
        file_path = os.path.dirname(full_file_path)

        new_file_name = cls.normalize(file_name)

        if new_file_name != file_name:
            new_file_name = cls.check_name_conflict(file_path, new_file_name)
        new_file_name = cls.check_name_conflict(destination_folder, new_file_name)

        new_full_file_path = os.path.join(file_path, new_file_name)

        os.rename(full_file_path, new_full_file_path)

        return new_full_file_path


    @classmethod
    def move_file(cls, file_path: str, destination_folder: str) -> None:
        """
        Move a file to the specified destination folder.

        This function moves the file at the given file path to the specified destination folder.
        It calls the `rename_file` function to ensure the file is renamed and conflicts are resolved
        before moving it.

        Args:
            file_path (str): The path to the file to be moved.
            destination_folder (str): The path to the destination folder.

        Returns:
            None
        """

        new_full_file_path = cls.rename_file(destination_folder, file_path)
        shutil.move(new_full_file_path, destination_folder)


    def get_category_path(self, file_name: str) -> str:
        """
        Get the category path for a file based on its extension.

        This function determines the category path for a file based on its extension. It compares
        the extension with the extensions defined in the CATEGORIES dictionary. If a match is found,
        it returns the corresponding category path.

        Args:
            file_name (str): The name of the file.

        Returns:
            str: The path to the category folder if the file belongs to a category, None otherwise.

        """

        extension = os.path.splitext(file_name)[1].lower()[1:]
        if extension:

            for category, extensions in CATEGORIES.items():
                if extension in extensions:
                    category_path = os.path.join(self.BASE_FOLDER, category)

                    return category_path

        return os.path.join(self.BASE_FOLDER, 'other')


    def move_files(self) -> None:
        """
        Move files to their respective category folders.

        This function traverses the files and folders within the BASE_FOLDER.
        Files that match the extensions specified in the CATEGORIES dictionary are moved to their
        corresponding category folders using the move_file function.
        Files with unknown extensions are renamed using the rename_file function.
        """

        for root, dirs, files in os.walk(self.BASE_FOLDER):
            if os.path.basename(root) in CATEGORIES:
                continue
            for file in files:
                category_path = self.get_category_path(file)
                self.move_file(os.path.join(root, file), category_path)



    def unpack_archives(self) -> None:
        """
        Unpack archive files within the 'archives' folder.

        This function extracts files from archive files located within the 'archives' folder
        of the BASE_FOLDER. It supports multiple archive formats such as zip, gz, tar, and 7z.
        Extracted files are placed in the 'archives' folder and the original archive files are deleted.
        """

        folder_path = os.path.join(self.BASE_FOLDER, 'archives')
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.splitext(file)[1][1:] in CATEGORIES['archives']:

                if os.path.splitext(file)[1][1:] == '7z':
                    with py7zr.SevenZipFile(file_path, mode='r') as z:
                        z.extractall(path=folder_path)
                else:
                    shutil.unpack_archive(file_path, folder_path)

                os.remove(file_path)


    def delete_empty_folders(self) -> None:
        """
        Delete empty folders within the BASE_FOLDER.

        This function traverses the files and folders within the BASE_FOLDER in reverse order.
        Empty folders (excluding category folders) are deleted recursively.
        """

        for root, dirs, files in os.walk(self.BASE_FOLDER, topdown=False):

            for directory in dirs:
                path = os.path.join(root, directory)

                if os.path.basename(path) in CATEGORIES:
                            continue

                if not os.listdir(path):
                    os.rmdir(path)


    def run(self) -> None:
        """
        Perform the disassembly process.

        This function is the main entry point for the disassembly process.
        It calls various functions to create categories, move files, unpack archives,
        and delete empty folders.
        """

        self.create_categories()
        self.move_files()
        self.unpack_archives()
        self.delete_empty_folders()

        return stylize("Sorting folder ", 'green') + self.BASE_FOLDER + stylize(" completed.", 'green')
