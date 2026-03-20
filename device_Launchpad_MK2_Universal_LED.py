# Launchpad Mini MK2 PRO+ LED Script
# Luces con velocity real + efecto ritmo + animaciones

import device
import midi
import time
import random

CHANNEL = 0

# Colores base
OFF = 0
DIM = 10
RED = 15
GREEN = 60
YELLOW = 62
ORANGE = 45
BRIGHT = 100

last_time = 0

def send(note, color):
    device.midiOutMsg(midi.MIDI_NOTE_ON + (CHANNEL << 4), note, int(color))

# Color según velocity real
def velocity_to_color(vel):
    if vel < 40:
        return RED
    elif vel < 80:
        return ORANGE
    else:
        return BRIGHT

# Efecto ritmo (flash global)
def rhythm_flash():
    for n in range(36, 100):
        send(n, random.choice([RED, GREEN, YELLOW]))
    time.sleep(0.01)

def OnNoteOn(event):
    global last_time

    note = event.data1
    velocity = event.data2

    # Color según qué tan fuerte tocás
    color = velocity_to_color(velocity)

    # Prender pad tocado
    send(note, color)

    # Efecto show (si tocás seguido)
    now = time.time()
    if now - last_time < 0.15:
        rhythm_flash()

    last_time = now

    event.handled = False

def OnNoteOff(event):
    note = event.data1

    # Luz tenue al soltar
    send(note, DIM)

    event.handled = False

def OnInit():
    # Animación inicio tipo DJ
    for i in range(36, 100):
        send(i, random.choice([RED, GREEN, YELLOW]))
        time.sleep(0.005)

    for i in range(36, 100):
        send(i, OFF)