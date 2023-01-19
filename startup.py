import subprocess

# Check if bluetooth service is running
bluetooth_status = subprocess.run(['systemctl', 'is-active', 'bluetooth'], stdout=subprocess.PIPE)

if bluetooth_status.stdout.decode().strip() == 'active':
    # Disconnect from any currently connected wifi networks
    subprocess.run(['nmcli', 'device', 'wifi', 'disconnect'])
    # Connect to specific wifi network
    subprocess.run(['nmcli', 'device', 'wifi', 'connect', 'Augustupdater', 'password', 'pD^95!oMG'])
    subprocess.run(['bluetoothctl'])
    subprocess.run(['connect 88:64:40:2B:7B:41'])
    subprocess.run(['exit'])

    scripts = ['update.py', 'camerahandler.py']
    process = None
    # Run the scripts in background
    for script in scripts:
        process = subprocess.Popen(['python', script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)
        process.wait()




