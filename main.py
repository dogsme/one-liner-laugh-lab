#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock."""
import os

LINE = "I didn't eat the sock \u2014 I rescued it from the washing machine. It lives in my dustbin now, rent-free, and has never been happier."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
