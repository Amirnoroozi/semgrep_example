import marshal
fin = open('index.mar')
for line in fin:
    # ruleid: marshal-usage
    marshal.dumps(line)
    # ok: marshal-usage
    marshal.someokfunc(line)
