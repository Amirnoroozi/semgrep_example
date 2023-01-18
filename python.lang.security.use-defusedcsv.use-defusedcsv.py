import csv
with open("file", 'r') as fin:
    # ok: use-defusedcsv
    reader = csv.reader(fin)
with open("file", 'w') as fout:
    # ruleid: use-defusedcsv
    writer = csv.writer(fout, quoting=csv.QUOTE_ALL)
import defusedcsv as csv
    writer = csv.writer(fout)
