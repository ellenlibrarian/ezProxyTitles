# This script goes through an EZProxy config.txt file and extracts the Title line from all stanzas in the file. This yields a list of all the stanzas in the file.
# I wrote this to have a quick way to find out what's in the file. It is part of a larger cleanup of config.txt.

fname = input("Enter file name: ")
fout = open("config-titles.txt", "w")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("T") : # I used T instead of Title because our config.txt file is old and still includes that as a title designation for some stanzas.
        continue
    print(line)
    fout.write(line + "\n")
