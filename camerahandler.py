import datetime
import os
import subprocess
import time
def startCamera(filename):
    # Define the directory where the video will be saved
    save_directory = '/media/pi/Memorex USB/Dashcamfootage'

    # Get the current date and time
    now = datetime.datetime.now()

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
    process = subprocess.Popen(command)
    process.wait()
    process.terminate()

