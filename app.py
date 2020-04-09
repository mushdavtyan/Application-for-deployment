#!/usr/bin/env python3

import datetime
import os

def do_magic():
   now = datetime.datetime.now()
   return "Hello! {0}".format(now)


if __name__ == "__main__":
   if "REQUEST_URI" in os.environ:
      print("Content-Type: text/html\n\n")
      print(do_magic())
   else:
      print(do_magic())

