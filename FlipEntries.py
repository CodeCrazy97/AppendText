'''
 Places the journal entries at the bottom of the file at the top.

 Only meant to be ran once to fix the writings file. I had been placing the journal
 entries in ascending order, from the earliest dates first. That was inconvenient,
 because I'd have to go to the bottom of the file to be able to add a new entry.

 Created: 06/26/2021

'''

JOURNAL_FILE = "C:\\Users\\Ethan\\Documents\\Writings\\Weekly Report.txt"

f = open(JOURNAL_FILE, 'r')
last_entry = ""
fixed_entries = ""
for line in f:
    if "*** " in line:  # beginning of another entry
        fixed_entries = last_entry + fixed_entries
        last_entry = line # reset the entry
    else:
        last_entry += line

fixed_entries = last_entry + fixed_entries  #place very last entry in the fixed entries

print(fixed_entries)

f.close()