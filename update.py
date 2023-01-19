import subprocess

# Set the Git repository URL, username, and password
url = "https://github.com/username/repo.git"
username = "EdersenC"
password = "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"

# Run the git pull command with the username and password as command line arguments
result = subprocess.run(["git", "pull", url, username, password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output of the command
print(result.stdout.decode())
print(result.stderr.decode())

# Check the return code
if result.returncode == 0:
    print("Command completed successfully.")
else:
    print("Command failed with return code", result.returncode)

# Exit the script
exit(result.returncode)

