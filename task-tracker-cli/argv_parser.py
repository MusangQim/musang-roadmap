import sys


def main() -> None:
    input_user = sys.argv
    if len(input_user) < 2:
        print("No command provided")
        sys.exit(1)
    command = sys.argv[1]
    try:
        argument = sys.argv[2]
    except IndexError:
        argument = None
    print(f"{command} {argument}")


if __name__ == "__main__":
    main()
