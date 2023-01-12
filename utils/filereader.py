import json
import pathlib
from jproperties import Properties


class FileReader:
    def __init__(self, filename):
        self._filename = filename
        print("FileReader:", filename)

    def read(self) -> dict:
        print("FileReader read")
        return {}

    @property
    def filename(self):
        return self._filename

    @staticmethod
    def get(filename):
        table = {
            '.json': JsonFileReader,
            '.properties': PropertiesFileReader
        }
        file_extension = pathlib.Path(filename).suffix
        if file_extension in table:
            return table[file_extension](filename)
        else:
            return NullFileReader(filename)


class JsonFileReader(FileReader):
    def __init__(self, filename):
        print("JsonFileReader")
        super().__init__(filename)
        print("JsonFileReader:", self.filename)

    def read(self) -> dict:
        print("Json FileReader perform:", self._filename)

        with open(self._filename) as f:
            content = json.load(f)
        return content


class PropertiesFileReader(FileReader):
    def __init__(self, filename):
        print("PropertiesReader")
        super().__init__(filename)

    def read(self) -> dict:
        content = {}
        with open(self._filename, "rb") as f:
            properties = Properties()
            properties.load(f)
            for item in properties.items():
                message_id, message = item[0], item[1][0]
                content[message_id] = {
                    "message": message
                }
        return content


class NullFileReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def read(self):
        raise FileNotFoundError
