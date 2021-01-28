import math
import re
import json

file = open("inputD2P1.txt", "r")
pws = file.read().replace("-", "\n").split("\n")