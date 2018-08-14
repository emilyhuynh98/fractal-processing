import struct
import csv

csv = open('log.csv', 'w')
csv.write('counter, offset, time, sample\n')

# CONVERT SD CARD DATA TO CSV
# COUNTER, OFFSET, TIME, SAMPLE

with open("log.bin", "rb") as f:
    byte = f.read(4)
    count = 1
    separator = ', '
    while byte:
        unpacked = struct.unpack('i', byte)
        csv.write(str(unpacked[0]) + separator)
        byte = f.read(4)
        count += 1;
        separator = '\n' if (count % 4 == 0) else ', '

csv.close()
f.close() 
