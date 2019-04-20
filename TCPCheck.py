import subprocess
import os

os.system(hping3 -S -c 1 -s 6533 -p 53 10.133.1.1)
os.system(hping3 -2 -c 1 -s 6533 -p 53 10.133.1.1)