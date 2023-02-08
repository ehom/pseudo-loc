#!/usr/bin/env python3

import json
import pathlib
from jproperties import Properties


class FileWriter:
    def __init__(self, filename):
        self._filename = filename

    @staticmethod
    def get(filename):
        registry = {
            '.json': JsonFileWriter,
            '.properties': PropertiesFileWriter
        }
        file_extension = pathlib.Path(filename).suffix
        if file_extension in registry:
            return registry[file_extension](filename)
        else:
            return NullFileWriter(filename)


class JsonFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, dict_obj):
        # print("JsonFileWriter write")
        json_obj_str = json.dumps(dict_obj, indent=4, ensure_ascii=False)

        with open(self._filename, 'w', encoding="utf-8") as outputHandle:
            outputHandle.write(json_obj_str)


class PropertiesFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, dict_obj):
        properties = Properties()
        for key, value in dict_obj.items():
            properties[key] = value['message']

        with open(self._filename, "wb") as f:
            properties.store(f)


class NullFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, dict_obj):
        pass
