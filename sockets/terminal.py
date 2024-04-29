import os
import subprocess

# create terminal with subprocess
# subprocess.run(["bash", "-c", "echo 'Hello, World!'"])
while True:
    command = input(f"{os.getcwd()} > ")
    if command == 'exit':
        break

    commands = command.split(" ")
    if len(commands) == 2 and commands[0] == "cd":
        try:
            os.chdir(commands[1])
        except FileNotFoundError as e:
            print(e.strerror)
    else:
        result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        print(result.stdout)
        print(result.stderr)
