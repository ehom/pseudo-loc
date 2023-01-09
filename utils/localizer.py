class UnicodeChars:
    PILCROW: str = "\u00b6"
    MATH_LEFT_DOUBLE_ANGLE: str = "\u27ea"
    MATH_RIGHT_DOUBLE_ANGLE: str = "\u27eb"


class BracketStrategy:
    _left_bracket = UnicodeChars.MATH_LEFT_DOUBLE_ANGLE
    _right_bracket = UnicodeChars.MATH_RIGHT_DOUBLE_ANGLE

    @property
    def left_bracket(self):
        return self._left_bracket

    @left_bracket.setter
    def left_bracket(self, char):
        char: str
        self._left_bracket = char

    @property
    def right_bracket(self):
        return self._right_bracket

    @right_bracket.setter
    def right_bracket(self, char):
        char: str
        self._right_bracket = char

    def perform(self, text) -> str:
        text: str
        return self._left_bracket + text + self._right_bracket


class PaddingStrategy:
    _pad_char = UnicodeChars.PILCROW

    @property
    def pad_char(self):
        return self._pad_char

    @pad_char.setter
    def pad_char(self, char):
        self.pad_char = char

    def perform(self, text):
        expansion = int(len(text) / 3)
        padding = self.pad_char * expansion
        return padding + text + padding


class Localizer:
    def __init__(self, bracket_strategy=BracketStrategy(), padding_strategy=PaddingStrategy()):
        self._bracket_strategy = bracket_strategy
        self._padding_strategy = padding_strategy

    def localize(self, text) -> str:
        text: str
        padded = self._padding_strategy.perform(text)
        return self._bracket_strategy.perform(padded)

    class Builder:
        def __init__(self):
            self._padding_strategy = PaddingStrategy()
            self._bracket_strategy = BracketStrategy()

        @property
        def padding_strategy(self):
            return self._padding_strategy

        @padding_strategy.setter
        def padding_strategy(self, padding_strategy):
            self._padding_strategy = padding_strategy
            return self

        @property
        def bracket_strategy(self):
            return self._bracket_strategy

        @bracket_strategy.setter
        def bracket_strategy(self, bracket_strategy):
            self._bracket_strategy = bracket_strategy
            return self

        def build(self):
            return Localizer(padding_strategy=self._padding_strategy, bracket_strategy=self._bracket_strategy)
