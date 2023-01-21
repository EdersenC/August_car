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
def startBluetooth():
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
        
def update():
    # Get current date
    now = datetime.datetime.now()
    version_date = now.strftime("%Y-%m-%d")


    # Run the git pull command with the username and password as command line arguments
    result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Print the output of the command
    print(result.stdout.decode())
    print(result.stderr.decode())

    # Check the return code
    if result.returncode == 0:
        # Get current version from git tag
        version = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        current_version = version.stdout.decode().strip()
        # Append version date to current version
        new_version = f"{version_date}-{current_version}"
        print("New version: ", new_version)
        # Write new version to text files
        with open("/home/august/carsetup/August_car/AugustCar_SoftWareVersion.txt", "w") as f:
            f.write(new_version)
        print("Command completed successfully.")
        subprocess.run(["git", "pull"])
        subprocess.run(["sudo", "apt-get", "update", ""])
        subprocess.run(["sudo", "apt-get", "upgrade", "-y", "bluetooth", "--allow-unauthenticated"])
        subprocess.run(["sudo", "apt-get", "upgrade", "-y", "wifi", "--allow-unauthenticated"])
        subprocess.run(["sudo", "apt-get", "install", "-y", "fswebcam", "--allow-unauthenticated"])

        print("Bluetooth, WiFi and fswebcam updated successfully.")
    else:
        print("Command failed with return code", result.returncode)

    # Exit the script
    exit(result.returncode)

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
    '-t', '120',
    '-s', '1280x720',
    '-vcodec', 'mjpeg',
    '-b:v', '60M',
    '-q:v', '2',
    '-vf', "drawtext=fontfile=/home/pi/font/matrole/metrole.ttf: text='%{localtime\:%Y-%m-%d %T}': x=10: y=10: fontcolor=red: box=1: boxcolor=black@0.5",
    file_path
    )
    process = subprocess.Popen(command)
    return process
command2 = startBluetooth()
command3 = update()
while(True):

    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d %I-%M %p") + '.avi'
    command = startCamera(file_name)
    command.wait()
    command.terminate()

