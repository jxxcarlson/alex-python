import sys

capital = float(sys.argv[1])
rate = float(sys.argv[2])/100.0
years = int(sys.argv[3])

for i in range(0, years):
  capital = (1 + rate)*capital
  print "%3d %8.0f" % (i, capital)