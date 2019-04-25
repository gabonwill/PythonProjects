import subprocess
import os

os.system(hping3 -S -c 10000 -s 6533 -p 53 10.133.1.1)
