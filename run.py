from subprocess import Popen, PIPE
from time import *
#control_f4_sequence = '''keydown Control_L
#key F4
#keyup Control_L
#'''
#
#shift_a_sequence = '''keydown Shift_L
#key A
#keyup Shift_L
#'''
keytest = '''key N
key a
key B
key A
key L
key L
key Return
'''
def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)
while True:
	keypress(keytest)
	sleep(1)

#keypress(control_f4_sequence)
