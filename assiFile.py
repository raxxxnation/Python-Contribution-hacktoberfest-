fname = input('Enter file name : ')
ofile = open(fname)
for ha in ofile:
    print(ha.upper())
