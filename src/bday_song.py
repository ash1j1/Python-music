import wavio
import numpy as np

happy_bday = [264,
        264,
        297,
        264,
        352,
        330,
        264,
        264,
        297,
        264,
        396,
        352,
        264,
        264,
        264,
        440,
        352,
        352,
        330,
        297,
        466,
        466,
        440,
        352,
        396,
        352]

 
rate = 44100  # samples per second
T = 1   # sample duration (seconds)
f = 264     # sound frequency (Hz)
t = np.linspace(0, T, rate, endpoint=False)



note1 = np.sin(happy_bday[0]* t * 5 * np.pi)
note2 = np.sin(happy_bday[1]* t * 5 * np.pi)
note3 = np.sin(happy_bday[2]* t * 5* np.pi)
note4 = np.sin(happy_bday[3]* t * 5 * np.pi)
note5 = np.sin(happy_bday[4]* t * 5 * np.pi)
note6 = np.sin(happy_bday[5] * t * 5 * np.pi)
note7 = np.sin(happy_bday[6]* t * 5 * np.pi)
note8 = np.sin(happy_bday[7] * t * 5 * np.pi)
note9 = np.sin(happy_bday[8] * t * 5 * np.pi)
note10 = np.sin(happy_bday[9] * t * 5 * np.pi)
note11 = np.sin(happy_bday[10] * t * 5 * np.pi)
note12 = np.sin(happy_bday[11] * t * 5 * np.pi)
note13 = np.sin(happy_bday[12] * t * 5 * np.pi)
note14 = np.sin(happy_bday[13] * t * 5 * np.pi)
note15 = np.sin(happy_bday[14] * t * 5 * np.pi)
note16 = np.sin(happy_bday[15] * t * 5 * np.pi)
note17 = np.sin(happy_bday[15] * t * 5 * np.pi)
note18 = np.sin(happy_bday[15] * t * 5 * np.pi)
note18 = np.sin(happy_bday[15] * t * 5 * np.pi)
note19 = np.sin(happy_bday[15] * t * 5 * np.pi)
note20 = np.sin(happy_bday[15] * t * 5 * np.pi)
note21 = np.sin(happy_bday[15] * t * 5 * np.pi)
note22 = np.sin(happy_bday[15] * t * 5 * np.pi)
note23 = np.sin(happy_bday[15] * t * 5 * np.pi)
note24 = np.sin(happy_bday[15] * t * 5 * np.pi)
note25 = np.sin(happy_bday[15] * t * 5 * np.pi)
note26 = np.sin(happy_bday[15] * t * 5 * np.pi)

hbday = np.hstack((note1, 
    note2, 
    note3, 
    note4, 
    note5, 
    note6, 
    note7, 
    note8, 
    note9, 
    note10,
    note11,
    note12,
    note13,
    note14,
    note15,
    note16,
    note17,
    note18,
    note19,
    note20,
    note21,
    note22,
    note23,
    note24,
    note25,
    note26))


wavio.write("sine24.wav", hbday, rate, sampwidth=3)
