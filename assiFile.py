fnameee = input('Enter file name or Metamname of the file : ')
ofile = open(fnameee)
for ha in ofile:
    print(ha.upper())
