import re


class UnicodeChars:
    PILCROW: str = "\u00b6"
    MATH_LEFT_DOUBLE_ANGLE: str = "\u27ea"
    MATH_RIGHT_DOUBLE_ANGLE: str = "\u27eb"
    LEFT_CORNER_BRACKET: str = "\u300C"
    RIGHT_CORNER_BRACKET: str = "\u300D"


class StringOperation:
    def perform(self, text):
        pass


class BracketStrategy(StringOperation):
    def __init__(self):
        self._left_bracket = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE
        self._right_bracket = UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE
        self._left_inside_bracket = UnicodeChars.LEFT_CORNER_BRACKET
        self._right_inside_bracket = UnicodeChars.RIGHT_CORNER_BRACKET

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
            return self._left_inside_bracket + \
                match_obj.group() + \
                self._right_inside_bracket
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


class Localizer:
    def __init__(self, bracket_strategy: StringOperation = None,
                 padding_strategy: StringOperation = None):

        self._pad_text = False

        if bracket_strategy is None:
            self._bracket_strategy = BracketStrategy()
        else:
            self._bracket_strategy = bracket_strategy

        if padding_strategy is None:
            self._padding_strategy = PaddingStrategy()
        else:
            self._padding_strategy = padding_strategy

    @property
    def pad_text(self):
        return self._pad_text

    @pad_text.setter
    def pad_text(self, flag=True):
        self._pad_text = flag

    def localize(self, text: str):
        if self.pad_text is True:
            text = self._padding_strategy.perform(text)
        return self._bracket_strategy.perform(text)

    class Builder:
        def __init__(self):
            self._padding_strategy: StringOperation = PaddingStrategy()
            self._bracket_strategy: StringOperation = BracketStrategy()

        @property
        def padding_strategy(self):
            return self._padding_strategy

        @padding_strategy.setter
        def padding_strategy(self, padding_strategy: StringOperation):
            self._padding_strategy = padding_strategy
            return self

        @property
        def bracket_strategy(self):
            return self._bracket_strategy

        @bracket_strategy.setter
        def bracket_strategy(self, bracket_strategy: StringOperation):
            self._bracket_strategy = bracket_strategy
            return self

        def build(self):
            return Localizer(padding_strategy=self._padding_strategy,
                             bracket_strategy=self._bracket_strategy)
