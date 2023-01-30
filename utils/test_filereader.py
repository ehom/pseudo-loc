import unittest
import filereader as fr


class FileReaderTest(unittest.TestCase):
    def test_json_filereader(self):
        filename = "../test_files/test.json"
        reader = fr.FileReader.get(filename)
        self.assertEqual(type(reader), type(fr.JsonFileReader(filename)))

    def test_null_filereader(self):
        filename = "../test_files/test.j"
        reader = fr.FileReader.get(filename)
        self.assertEqual(type(reader), type(fr.NullFileReader(filename)))

    def test_properties_filereader(self):
        filename = "../test_files/test.properties"
        reader = fr.FileReader.get(filename)
        self.assertEqual(type(reader), type(fr.PropertiesFileReader(filename)))


if __name__ == '__main__':
    unittest.main()
