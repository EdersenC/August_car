import subprocess

# Open the config.txt file
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

    # Check the status of mplayer
    mplayer = subprocess.Popen(["mplayer", "-slave", "-quiet", "-idle"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Send the pause command to toggle the pause state
    mplayer.stdin.write(b"pause\n")
    mplayer.stdin.flush()

    # Wait for the process to end
    process.wait()

    scripts = ['update.py', 'camerahandler.py']
    process = None
    # Run the scripts in background
    for script in scripts:
        process = subprocess.Popen(['python', script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        process.wait()
