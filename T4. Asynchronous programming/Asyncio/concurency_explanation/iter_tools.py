import itertools
import sys
# for number in itertools.count():
#     print(number)


# for number in itertools.chain(range(10, 80), itertools.count(80, 5)):
#     print(number)

# for repeated_value in itertools.repeat("repeat me", times=7):
#     print(repeated_value)
#
#
# x = itertools.cycle("abcde")
# for infinite_cycle in x:
#     print(infinite_cycle)

for generator_slice in itertools.islice(
        itertools.chain(range(10, 100), itertools.count(100, 5)),
        200):
    print(generator_slice)
