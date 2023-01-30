import unittest
from pseudo_loc.lib.localizer import Localizer
from pseudo_loc.lib.localizer import UnicodeChars


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.localizer = Localizer()

    def test_default_localizer(self):
        localized = self.localizer.localize("abc")
        localized = localized.encode('utf-8')
        expected = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE + \
            "abc" + \
            UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE
        expected = expected.encode('utf-8')

        self.assertEqual(localized, expected)

    def test_localizer_with_padding(self):
        self.localizer.pad_text = True
        localized = self.localizer.localize("abc")
        localized = localized.encode('utf-8')
        expected = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE + \
            UnicodeChars.PILCROW + \
            "abc" + UnicodeChars.PILCROW + \
            UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE
        expected = expected.encode('utf-8')

        self.assertEqual(localized, expected)

    def test_empty_string(self):
        localized = self.localizer.localize("")
        localized = localized.encode('utf-8')
        expected = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE + UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE
        expected = expected.encode('utf-8')

        self.assertEqual(localized, expected)


if __name__ == '__main__':
    unittest.main()
