HUB_NAME = "Controller5"

import os
import subprocess

target = os.getenv("TARGET")
print(target)
command = f"pybricksdev run ble --name {HUB_NAME} {target}"

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError:
    print("Error uploading code to hub")
    print("Make sure to set HUB_NAME and turn the hub on")
