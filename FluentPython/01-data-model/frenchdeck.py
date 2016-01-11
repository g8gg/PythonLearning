import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))  # 从你要知道的角度出发获得正确的答案,而不是去猜对象是否有.szie()还是.len()还是.length()
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    print(deck[0], deck[-1])  # 第一张牌和最后一张
    card = choice(deck)
    print(deck[:3])  # 随便从顶上取三张
    print(deck[12::13])  # 取第13张牌,然后隔13张取一次
    print(deck[12], deck[25], deck[38], deck[51])  # 取第13(12+1)张,然后加13(取第13张)
    # pick just the aces by starting on index 12 and skipping 13 cards at a time "原书这里不对,应skipping 12 cards"

    # 以上这一切的魔法: Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing.

    # 请理解体会一下:
    # We’ve just seen two advantages of using special methods to leverage the Python data model:
    # 1. The users of your classes don’t have to memorize arbitrary method names for standard operations (“How to get the number of items? Is it .size(), .length(), or what?”).
    # 2. It’s easier to benefit from the rich Python standard library and avoid reinventing the wheel, like the random.choice function.

    # iterable: __getitem__
    print("*" * 10)
    for card in deck:
        print(card)

    print("*" * 20)
    for card in reversed(deck):
        print(card)

    # Iteration is often implicit. If a collection has no __contains__ method,
    # the in operator does a sequential scan.
    # Case in point: in works with our FrenchDeck class because it is iterable.
    print("*" * 30)
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    # Sorting
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    # A common system of ranking cards is by rank (with aces being highest)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)  # 因为是按顺序,所以A在最后,所以最大嘛,这样就不需要再多一个rule表达A→2
        return rank_value * len(suit_values) + suit_values[card.suit]  # *len(suit_values)保证不会发生碰撞


    for card in sorted(deck, key=spades_high):
        print(card)

        # 总结: Although FrenchDeck implicitly inherits from object,[5] its functionality is not inherited, but
        # comes from leveraging the data model and composition.

        # 洗牌如何? HOW ABOUT SHUFFLING?
        # As implemented so far, a FrenchDeck cannot be shuffled, because it is immutable: the cards and their positions
        # cannot be changed, except by violating encapsulation and handling the _cards attribute directly.
        # that will be fixed by adding a one-line __setitem__ method.
