import pyttsx3
import random
import time

## Calc who gets what and where
position = 'd4'
l = ['h1', 'd1', 'd2', 'mt', 'ot', 'd3', 'd4', 'h2']
dooms = random.sample(l, 4)
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
vl2 = "You have doom" if i_am_doomed else "No doom"
vl3 = marker

engine.say(vl1)
engine.runAndWait()
time.sleep(6)
engine.say(vl2)
engine.runAndWait()
time.sleep(9)
engine.say(vl3)
engine.runAndWait()


## Print the cheat sheet
print("CHEATSHEET:")
print("Warrior at ", locs[warrior_spawn])
print("Doomed Players ", dooms)
print("Your Marker ", marker)
print("Eye at ", locs[eye_loc])
print("King at ", locs[king_loc])
