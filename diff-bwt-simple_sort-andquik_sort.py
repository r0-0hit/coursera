import random
import timeit


def simple_sort(cards):
    sorted_cards = []
    while cards:
        lowest_card = min(cards)
        sorted_cards.append(lowest_card)
        cards.remove(lowest_card)
    return sorted_cards


def quicksort(cards):
    if len(cards) < 2:
        return cards
    else:
        pivot = random.choice(cards)
        cards.remove(pivot)
        less = [i for i in cards if i <= pivot]
        greater = [i for i in cards if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# def quicksort(cards):
#     if len(cards) < 2:
#         return cards  # Base case: Already sorted if 0 or 1 element
#     else:
#         pivot = cards[0]  # Choose first card as pivot
#         less = [i for i in cards[1:] if i <= pivot]
#         greater = [i for i in cards[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


cards = list(range(1000, 0, -1))

simple_sort_time = timeit.timeit(lambda: simple_sort(cards.copy()), number=1000)
quicksort_time = timeit.timeit(lambda: quicksort(cards.copy()), number=1000)

print(simple_sort_time)  # 6.066193499999827
print(quicksort_time)  # 0.7850062999996226
