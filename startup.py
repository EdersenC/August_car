import subprocess

# Check if bluetooth service is running
bluetooth_status = subprocess.run(['systemctl', 'is-active', 'bluetooth'], stdout=subprocess.PIPE)

if bluetooth_status.stdout.decode().strip() == 'active':
    # Open the bluetooth command-line interface
    process = subprocess.Popen(['bluetoothctl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send the 'connect XX:XXX:XX:XX' command to the bluetooth command-line interface
    process.stdin.write(b'connect 88:64:40:2B:7B:41\n')
    process.stdin.flush()
    # Send the 'exit' command to the bluetooth command-line interface
    process.stdin.write(b'exit\n')
    process.stdin.flush()

    # Wait for the process to end
    process.wait()

    scripts = ['update.py', 'camerahandler.py']
    process = None
    # Run the scripts in background
    for script in scripts:
        process = subprocess.Popen(['python', script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        process.wait()



