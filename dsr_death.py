### Drangonsong's Reprise Utimate Death of the Heaven's personal Sim
###
### This is intended to help players get more consistent with the death of the heavens mech.
### This sim was made with the assumption that you are using a stragegy for selecting which player
### goes where in a straight line similar to this toolbox: https://ff14.toolboxgaming.space/?id=346958196041561&preview=1
### for the group's strategy for this mechanic. it will calc each mechanic of the phase and tell you
### which ones are affecting you in the following order:
###
### - Warrior location
### - Doom order (from closest to warrior to furthest from warrior)
### - What play station marker you have and where the eye / king thordan are
###
### To run this on your own machine, you need python 3 installed and the pyttsx3 library installed
### Usage: python3 dsr_death.py <position>



import pyttsx3
import random
import time
from sys import argv

## Vairables to change
position = argv[1] if len(argv) > 1 else 'd4' # this should be your position in the line up for death


## Calc who gets what and where
lineup = ['h1', 'd1', 'd2', 'mt', 'ot', 'd3', 'd4', 'h2']
dooms = random.sample(lineup, 4)
i_am_doomed = 'd4' in dooms
marker = ''
doom_markers = ['red', 'yellow', 'purple']
non_doom_markers = ['blue', 'yellow', 'purple']
if i_am_doomed:
    marker = random.sample(doom_markers, 1)[0]
else:
    marker = random.sample(non_doom_markers, 1)[0]


locs = ['A', 'B', 'C', 'D', '1', '2', '3', '4']
eye_loc = random.randint(0, 7)
king_loc = random.randint(0, 7)
warrior_spawn = random.randint(0, 7)

while abs(eye_loc - king_loc) <= 1 or abs(eye_loc - king_loc) == 7:
    king_loc = random.randint(0, 7)

## Read out the mechanic
engine = pyttsx3.init()

vl1 = f"Warrior at {locs[warrior_spawn]}"
vl2 = "Doom Ordering:"
for x in lineup:
    vl2 = f"{vl2} Doom, " if x in dooms else f"{vl2} No Doom, "
vl3 = f"{marker}.  Eye at {locs[eye_loc]}, King at {locs[king_loc]}"

engine.say(vl1)
engine.runAndWait()
time.sleep(4)
engine.say(vl2)
engine.runAndWait()
time.sleep(6)
engine.say(vl3)
engine.runAndWait()


## Print the cheat sheet
print("CHEATSHEET:")
print("Warrior at: ", locs[warrior_spawn])
print("Your Position: ", position)
print("Doomed Players: ", dooms)
print("Your Marker: ", marker)
print("Eye at ", locs[eye_loc])
print("King at ", locs[king_loc])
