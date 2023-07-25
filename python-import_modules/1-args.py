#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]  # Exclude the script name from the arguments
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} {argument if num_args == 1 else arguments}:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
