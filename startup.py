import subprocess
import os
import sys
import json
# Open the config.txt file
with open("/home/august/carsetup/config.json", "r") as f:
    config = json.load(f)
    save_directory = config["save_directory"]
    bluetooth_mac = config["bluetooth_mac"]
    hotspot_ssid = config["hotspot_ssid"] 
    hotspot_password = config["hotspot_password"]

# Check if bluetooth service is running
bluetooth_status = subprocess.run(['systemctl', 'is-active', 'bluetooth'], stdout=subprocess.PIPE)

if bluetooth_status.stdout.decode().strip() == 'active':
    # Open the bluetooth command-line interface
    process = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send the 'connect XX:XXX:XX:XX' command to the bluetooth command-line interface
    process.stdin.write(f'connect {bluetooth_mac}\n'.encode())
    process.stdin.flush()
    # Send the 'exit' command to the bluetooth command-line interface
    process.stdin.write(b'exit\n')
    process.stdin.flush()





