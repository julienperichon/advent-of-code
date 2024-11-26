test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def process_input(input_txt: str) -> list[tuple[str, int]]:
    processed_input = []
    for line in input_txt.splitlines():
        hand, bid = line.split()
        processed_input.append((hand, int(bid)))
    return processed_input

class Card:
    def __init__(self, name: str) -> None:
        self.name = name

    def _is_valid_operand(self, other: object) -> bool:
        return isinstance(other, Card)

    def __eq__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplementedError
        
