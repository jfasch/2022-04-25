import sys


translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


#print(sys.argv)
#print('[1]:', sys.argv[1], 'type:', type(sys.argv[1]))

try:
    digit = int(sys.argv[1])
except ValueError:
    print('dududu:', sys.argv[1], 'ist kein integer')
    sys.exit(1)

try:
    print(translation_table[digit])
except KeyError:
    print('dududu:', digit, 'ist keine ziffer (nochmal: ziffern sind 0-9)')
    sys.exit(2)
