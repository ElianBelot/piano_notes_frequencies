# ===============[ INITIALIZATION ]===============
a = 2**(1/12)       # Twelth root of 2 = 1.0594...
v = 345             # The speed of sound in air, in m/s

frequencies = []    # Recipient for calculated frequencies
names = []          # Recipient for calculated note names

notes = 'CDEFGAB'   # Notes string starting from A


# ===============[ CALCULATING FREQUENCIES ]===============
for i in range(1, 89):
    frequencies.append(a**(i-49) * 440) # A4 (440Hz) is reference occupies rank 49 on a piano


# ===============[ CALCULATING WAVELENGHTS ]===============
wavelenghts = list(map(lambda f: (v/f) * 100, frequencies)) # Multiply by 100 to get cm


# ===============[ CALCULATING NAMES ]===============
# For every octave (0 to 8)
for i in range(9):

    # For every note (C to B)
    for n in range(len(notes)):
        names.append(f'{notes[n]}{i}')

        # Add sharp and flat notes if not B or E
        if notes[n] not in 'EB':
            names.append(f'{notes[n]}#{i} / {notes[n+1]}b{i}')

# Only allow piano notes
names = names[names.index('A0'):names.index('C8') + 1]


# ===============[ EXPORTING TO CSV ]===============
with open('notes.csv', 'w') as file:
    file.write('Note, Frequency (Hz), Wavelenght (cm)')

    for n, f, w in zip(names, frequencies, wavelenghts):
        file.write(f'\n{n}, {round(f, 2):.2f}, {round(w, 2):.2f}')

