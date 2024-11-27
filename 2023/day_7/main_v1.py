test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

CARD_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.hand_value_str = (
            f"0x{self._compute_hand_type_index(hand)}{self._compute_card_index(hand[0])}"
            f"{self._compute_card_index(hand[1])}{self._compute_card_index(hand[2])}"
            f"{self._compute_card_index(hand[3])}{self._compute_card_index(hand[4])}"
        )
        self.hand_value = int(self.hand_value_str, base=16)

    def _compute_hand_type_index(self, hand: str) -> int:
        hand_counts = {}
        for card in hand:
            hand_counts[card] = hand_counts.get(card, 0) + 1
        hand_counts_values = list(hand_counts.values())
        match len(hand_counts):
            case 1:
                return 6
            case 2:
                return 5 if max(hand_counts_values) == 4 else 4
            case 3:
                return 3 if max(hand_counts_values) == 3 else 2
            case 4:
                return 1
            case 5:
                return 0

    @staticmethod
    def _compute_card_index(card: str) -> str:
        return hex(CARD_ORDER.index(card))[2:]


def process_input(input_txt: str) -> list[Hand]:
    processed_input = []
    for line in input_txt.splitlines():
        hand, bid = line.split()
        processed_input.append(Hand(hand, int(bid)))
    return processed_input


with open("input.txt", "r") as input_file:
    input_data = input_file.read()
processed_input = process_input(input_data)
sorted_hands = sorted(processed_input, key=lambda h: h.hand_value)
total_bid_won = 0
for idx, hand in enumerate(sorted_hands):
    total_bid_won += hand.bid * (idx + 1)
print(f"Total bid won: {total_bid_won}")
