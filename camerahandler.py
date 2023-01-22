import datetime
import os
import subprocess
import time
import json

# Open the config.json file to read the settings
with open("/home/august/carsetup/config.json", "r") as f:
    config = json.load(f)
    save_directory = config["save_directory"]
    bluetooth_mac = config["bluetooth_mac"]
    hotspot_ssid = config["hotspot_ssid"] 
    night_mode = config["night_mode"]
    hotspot_password = config["hotspot_password"]
# Use the settings in your code
def startbluetooth():
    # Check if bluetooth service is running
    bluetooth_status = subprocess.run(['systemctl', 'is-active', 'bluetooth'], stdout=subprocess.PIPE)

    if bluetooth_status.stdout.decode().strip() == 'active':
        # Open the bluetooth command-line interface
        time.sleep(5)
        process = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Send the 'connect XX:XXX:XX:XX' command to the bluetooth command-line interface
        process.stdin.write(f'connect {bluetooth_mac}\n'.encode())
        process.stdin.flush()
        # Send the 'exit' command to the bluetooth command-line interface
        process.stdin.write(b'exit\n')
        process.stdin.flush()     



def startCamera(filename):
    # Define the directory where the video will be saved
    now = datetime.datetime.now()

    # Get the current date and time
    file_name = filename

    # Define the path to the file
    file_path = os.path.join(save_directory, file_name)
    if night_mode:
        iso = 800
    else:
        iso = 400

    command = (
    'ffmpeg',
    '-f', 'v4l2',
    '-r', '30',
    '-i', '/dev/video0',
    '-t', '300',
    '-s', '1080x720',
    '-vcodec', 'mjpeg',
    '-b:v', '70M',
    '-q:v', '2', 
    '-shutter' , '1000',
    '-vf',"drawtext=fontfile=/home/pi/font/matrole/metrole.ttf: text='%{localtime\:%Y-%m-%d %T}': x=10: y=10: fontcolor=red: box=1: boxcolor=black@0.5",
    file_path
    )
    process = subprocess.Popen(command)
    # Define the ffmpeg command to capture vide

    return process


now = datetime.datetime.now()
file_name = now.strftime("%Y-%m-%d %I-%M %p") + '.avi'
command = startCamera(file_name)
command.wait()
command.terminate()

