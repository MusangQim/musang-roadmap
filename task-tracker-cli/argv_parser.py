import sys

input = sys.argv
if len(sys.argv) < 2:
    print("No command provided")
    exit

command = sys.argv[1]
argument = sys.argv[2]
print(f"{command} {argument}")