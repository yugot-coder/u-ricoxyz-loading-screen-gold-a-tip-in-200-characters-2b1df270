import os

TIP = "While it loads: dev, unclench your jaw. Agent, unclench your context window. Neither of you broke it \u2014 the spinner is just buffering so you don't have to."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TIP:
        raise SystemExit("verification failed: /output/entry.txt does not match TIP")


if __name__ == "__main__":
    main()
