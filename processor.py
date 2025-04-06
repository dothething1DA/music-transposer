basic_notes = ['do', 'reb', 're', 'mib', 'mi', 'fa', 'solb', 'sol', 'lab', 'la', 'sib', 'si']

note_id = {}
notes = basic_notes.copy()

for note in basic_notes:
    temp = list(note)
    temp[0] = temp[0].upper()
    temp = ''.join(temp)
    notes.append(temp)

for note in basic_notes:
    temp = list(note)
    temp[0] = temp[0].upper()
    temp[1] = temp[1].upper()
    if (len(temp) > 2 and temp[2].lower() == 'l'):
        temp[2] = temp[2].upper()
    temp = ''.join(temp)
    notes.append(temp)

for i in range(len(notes)):
    note_id[notes[i]] = i

def process_text(txt):
    lowest = 100
    cur_line = 1
    txt = txt.split("\n")
    for line in txt:
        cur_word = 1
        note_list = line.split()
        for note in note_list:
            if ((note in note_id) == False):
                return f"Error: Invalid note on line {cur_line}, word {cur_word}: {note}"
            nid = note_id[note]
            lowest = min(lowest, nid)
            cur_word += 1
        cur_line += 1

    res = ""
    for line in txt:
        note_list = line.split()
        for note in note_list:
            nid = note_id[note]
            res += notes[nid - lowest]
            res += " "
        res += "\n"

    return res
