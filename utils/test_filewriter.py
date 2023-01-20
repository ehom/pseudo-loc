import unittest
from filewriter import FileWriter
from filewriter import JsonFileWriter
from filewriter import PropertiesFileWriter
from filewriter import NullFileWriter


class FileReaderTest(unittest.TestCase):
    def test_json_filewriter(self):
        filename = "../test_files/test.json"
        writer = FileWriter.get(filename)
        self.assertEqual(type(writer), type(JsonFileWriter(filename)))

    def test_null_filewriter(self):
        filename = "../test_files/test.j"
        writer = FileWriter.get(filename)
        self.assertEqual(type(writer), type(NullFileWriter(filename)))

    def test_properties_filewriter(self):
        filename = "../test_files/test.properties"
        writer = FileWriter.get(filename)
        self.assertEqual(type(writer), type(PropertiesFileWriter(filename)))


if __name__ == '__main__':
    unittest.main()
