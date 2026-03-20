# Launchpad Mini MK2 PRO LED Script
# Colores + efecto show al tocar

import device
import midi
import time

CHANNEL = 0

# Colores
OFF = 0
DIM = 10
RED = 15
GREEN = 60
YELLOW = 62
ORANGE = 45
BRIGHT = 100

def send(note, color):
    device.midiOutMsg(midi.MIDI_NOTE_ON + (CHANNEL << 4), note, color)

# Animación tipo "flash"
def flash(note):
    send(note, BRIGHT)
    time.sleep(0.02)
    send(note, ORANGE)

# Colores según zona (grid)
def get_color(note):
    if note < 40:
        return RED
    elif note < 60:
        return GREEN
    elif note < 80:
        return YELLOW
    else:
        return ORANGE

def OnNoteOn(event):
    note = event.data1

    base_color = get_color(note)

    # efecto flash
    flash(note)

    # color base
    send(note, base_color)

    event.handled = False

def OnNoteOff(event):
    note = event.data1

    # luz tenue al soltar
    send(note, DIM)

    event.handled = False

def OnInit():
    # animación inicial
    for note in range(36, 100):
        send(note, ORANGE)
        time.sleep(0.005)

    for note in range(36, 100):
        send(note, OFF)
