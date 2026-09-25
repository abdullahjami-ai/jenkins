"""
A throwaway script used to demo VOLUMES (-v).

We never copy this file into an image. We mount the folder into a
plain python container at runtime, and the container runs it.
"""

import platform
import socket
import sys

print("=" * 46)
print("  Hello! I am a Python script running in Docker")
print("=" * 46)
print(f"  Python version : {sys.version.split()[0]}")
print(f"  Machine name   : {socket.gethostname()}   <- container ID")
print(f"  OS inside      : {platform.system()} {platform.machine()}")
print("=" * 46)
print("  This file was never copied into the image -")
print("  it was MOUNTED from your laptop with -v")
print("=" * 46)
