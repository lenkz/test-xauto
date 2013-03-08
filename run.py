from subprocess import Popen, PIPE
from time import *
import random
#control_f4_sequence = '''keydown Control_L
#key F4
#keyup Control_L
#'''
#
#shift_a_sequence = '''keydown Shift_L
#key A
#keyup Shift_L
#'''
keyball = '''key B
key a
key l
key l
key Return
'''
keytest = '''key N
key a
key B
key A
key L
key L
key Return
'''
list_call= [keytest,keyball]
def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)
while True:
	keypress(random.choice(list_call))
	sleep(2)

#keypress(control_f4_sequence)
