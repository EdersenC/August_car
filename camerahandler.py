import datetime
import os
import subprocess
import time

def startBluetooth():
    with open("/home/august/config.txt", "r") as f:
    # Read the save directory from the first line of the file
        save_directory = f.readline().strip()
    # Read the bluetooth MAC address from the second line of the file
        bluetooth_mac = f.readline().strip()

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

result = subprocess.run(["python3", "update.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def startCamera(filename):
    # Define the directory where the video will be saved
    now = datetime.datetime.now()
    
    with open("/home/august/config.txt", "r") as f:
    # Read the save directory from the first line of the file
        save_directory = f.readline().strip()

    # Get the current date and time
    

    # Format the date and time for the file name
    file_name = filename

    # Define the path to the file
    file_path = os.path.join(save_directory, file_name)

    # Define the ffmpeg command to capture video
    command = (
    'ffmpeg',
    '-f', 'v4l2',
    '-r', '30',
    '-i', '/dev/video0',
    '-t', '600',
    '-s', '1280x720',
    '-vcodec', 'mjpeg',
    '-b:v', '30M',
    '-q:v', '2',
    '-vf', "drawtext=fontfile=/home/pi/font/matrole/metrole.ttf: text='%{localtime\:%Y-%m-%d %T}': x=10: y=10: fontcolor=red: box=1: boxcolor=black@0.5",
    file_path
    )
    process = subprocess.Popen(command)
    return process

while(True):
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d %I-%M %p") + '.avi'
    command = startCamera(file_name)
    command2 = startBluetooth()
    command.wait()
    command.terminate()

