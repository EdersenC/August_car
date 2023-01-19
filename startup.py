import subprocess

# Check if bluetooth service is running
bluetooth_status = subprocess.run(['systemctl', 'is-active', 'bluetooth'], stdout=subprocess.PIPE)

if bluetooth_status.stdout.decode().strip() == 'active':

    subprocess.run(['bluetoothctl','connect 88:64:40:2B:7B:41','exit'])

    scripts = ['update.py', 'camerahandler.py']
    process = None
    # Run the scripts in background
    for script in scripts:
        process = subprocess.Popen(['python', script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        process.wait()




