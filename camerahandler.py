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
    hotspot_password = config["hotspot_password"]
# Use the settings in your code

        



def startCamera(filename):
    # Define the directory where the video will be saved
    now = datetime.datetime.now()

    # Get the current date and time
    file_name = filename

    # Define the path to the file
    file_path = os.path.join(save_directory, file_name)

    # Define the ffmpeg command to capture video
    command = (
    'ffmpeg',
    '-f', 'v4l2',
    '-r', '30',
    '-i', '/dev/video0',
    '-t', '300'
    '-s', '1280x720',
    '-vcodec', 'mjpeg',
    '-b:v', '70M',
    '-q:v', '2',
    '-vf', "drawtext=fontfile=/home/pi/font/matrole/metrole.ttf: text='%{localtime\:%Y-%m-%d %T}': x=10: y=10: fontcolor=red: box=1: boxcolor=black@0.5",
    file_path
    )
    process = subprocess.Popen(command)

    return process


subprocess.run(['python3','startup.py'])    
while(True):
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d %I-%M %p") + '.avi'
    command = startCamera(file_name)
    command.wait()
    command.terminate()

