import re


class UnicodeChars:
    PILCROW: str = "\u00b6"
    MATH_LEFT_DOUBLE_ANGLE: str = "\u27ea"
    MATH_RIGHT_DOUBLE_ANGLE: str = "\u27eb"
    MATH_LEFT_ANGLE_BRACKET: str = "\u27e8"
    MATH_RIGHT_ANGLE_BRACKET: str = "\u27e9"


class StringOperation:
    def perform(self, text) -> str:
        return text


class BracketStrategy(StringOperation):
    _left_bracket = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE
    _right_bracket = UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE
    _inside_brackets = [
        UnicodeChars.MATH_LEFT_ANGLE_BRACKET,
        UnicodeChars.MATH_RIGHT_ANGLE_BRACKET]

    @property
    def left_bracket(self):
        return self._left_bracket

    @left_bracket.setter
    def left_bracket(self, char: str):
        self._left_bracket = char

    @property
    def right_bracket(self):
        return self._right_bracket

    @right_bracket.setter
    def right_bracket(self, char: str):
        self._right_bracket = char

    def perform(self, text: str) -> str:
        def add_brackets(match_obj):
            left, right = self._inside_brackets
            return left + match_obj.group() + right
        text = re.sub(r"{\w*}", add_brackets, text)
        return f"{self._left_bracket}{text}{self._right_bracket}"


class PaddingStrategy(StringOperation):
    _pad_char = UnicodeChars.PILCROW

    @property
    def pad_char(self):
        return self._pad_char

    @pad_char.setter
    def pad_char(self, char: str):
        self.pad_char = char

    def perform(self, text: str) -> str:
        expansion = int(len(text) / 3)
        padding = self.pad_char * expansion
        return padding + text + padding


def bracket_decorate(method):
    def func_wrapper(self, text: str):
        text = method(self, text)
        if self._bracket_strategy:
            return self._bracket_strategy.perform(text)
        else:
            return text
    return func_wrapper


def pad_decorate(method):
    def func_wrapper(self, text: str):
        text = method(self, text)
        if self._pad_text:
            return self._padding_strategy.perform(text)
        else:
            return text
    return func_wrapper


class Localizer:
    def __init__(self, bracket_strategy: StringOperation = None,
                 padding_strategy: StringOperation = None):
        self._pad_text = False

        if bracket_strategy:
            self._bracket_strategy = bracket_strategy
        else:
            self._bracket_strategy = BracketStrategy()

        if padding_strategy:
            self._padding_strategy = padding_strategy
        else:
            self._padding_strategy = PaddingStrategy()

    @property
    def pad_text(self):
        return self._pad_text

    @pad_text.setter
    def pad_text(self, flag: bool):
        self._pad_text = flag

    @bracket_decorate
    @pad_decorate
    def localize(self, text: str):
        return text
