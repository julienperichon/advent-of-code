from utils import get_input_data


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

    @staticmethod
    def _compute_hand_type_index(hand: str) -> int:
        hand_counts = {}
        for card in hand:
            hand_counts[card] = hand_counts.get(card, 0) + 1
        hand_counts_values = list(hand_counts.values())
        match max(hand_counts_values):
            case 1:
                return 0
            case 2:
                return 1 if len(hand_counts) == 4 else 2
            case 3:
                return 3 if len(hand_counts) == 3 else 4
            case 4:
                return 5
            case 5:
                return 6

    @staticmethod
    def _compute_card_index(card: str) -> str:
        return hex(CARD_ORDER.index(card))[2:]


def process_input(input_txt: str) -> list[Hand]:
    processed_input = []
    for line in input_txt.splitlines():
        hand, bid = line.split()
        processed_input.append(Hand(hand, int(bid)))
    return processed_input


input_data = get_input_data("2023_day_7.txt")

processed_input = process_input(input_data)
sorted_hands = sorted(processed_input, key=lambda h: h.hand_value)
total_bid_won = 0
for idx, hand in enumerate(sorted_hands):
    total_bid_won += hand.bid * (idx + 1)
print(f"Total bid won: {total_bid_won}")
