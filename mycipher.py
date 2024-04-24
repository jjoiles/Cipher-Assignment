import sys

encryption = ("")
count_letter = 0
count_line = 0

shifter = int(sys.argv[1])

input_text = sys.stdin.read()


for i in input_text:
    if i.isalpha():
        i = i.upper()
        encryption += chr((ord(i) - 65 + shifter) % 26 + 65)
        count_line += 1
        count_letter += 1
    if count_letter == 5:
        encryption += (" ")
        count_letter = 0

    if count_line == 50:
        encryption += ("\n")
        count_letter = 0

print (encryption)

      