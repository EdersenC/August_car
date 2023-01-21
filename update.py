import subprocess
import datetime

# Get current date
now = datetime.datetime.now()
version_date = now.strftime("%Y-%m-%d")


# Run the git pull command with the username and password as command line arguments
result = subprocess.run(["git", "pull","/home/august/carsetup/August_car"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
