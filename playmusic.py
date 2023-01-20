import subprocess
import os
import time

# Function to check if phone is connected to the hotspot
def check_phone_connection():
    while True:
        output = subprocess.check_output("iwconfig wlan0", shell=True)
        if "Not-Associated" in output:
            print("Phone is not connected to the hotspot. Waiting for connection...")
            time.sleep(5)
        else:
            print("Phone is connected to the hotspot.")
            return True

# Function to play music using the spop client
def play_music():
    os.system("spop")

# Function to do a git pull
def git_pull():
    os.system("git pull")

# Main program
check_phone_connection()
play_music()
git_pull()
