import subprocess
import os

c1 = subprocess.call(["ls", "-ltr"])
p = subprocess.Popen(["ping", "-c 2", "localhost"], stdout=subprocess.PIPE)
print p.communicate()

print os.access("twoSums.py", os.R_OK)