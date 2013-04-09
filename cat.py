#!/usr/bin/python3
import sys
from optparse import OptionParser

class CatCommand:
  def __init__(self):
    self.count = 1

  def run(self, input, options):
    #default options
    e = ""
    
    for line in input:
      #modify printed line according to options
      if options.showend:
        line = line.rstrip()
        e = "$\n"
      if options.shownum:
        line = "{0} {1}".format(self.count, line)

      self.count += 1
      print(line, end=e)


def main():
  #set up options
  usage = "usage: %prog [OPTION]... [FILE]..."
  parser = OptionParser(usage=usage)

  parser.add_option("-E", dest="showend", action="store_true", help="Show $ at line endings")
  parser.add_option("-n", dest="shownum", action="store_true", help="Show line numbers")
  (options, args) = parser.parse_args()

  cat = CatCommand()

  #if filenames given
  if len(args) > 0:
    for arg in args:
      f = open(arg, "r")
      cat.run(f, options)


  #otherwise read from standard in
  else:
    cat.run(sys.stdin, options)

if __name__ == "__main__": main()
