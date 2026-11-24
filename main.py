import hashlib
import os

TIP = "While it loads: dev, unclench your jaw. Agent, unclench your context window. Neither of you broke it \u2014 the spinner is just buffering so you don't have to."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    written_digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    expected_digest = hashlib.sha256(TIP.encode("utf-8")).hexdigest()
    if written_digest != expected_digest:
        raise SystemExit(
            "verification failed: sha256 of /output/entry.txt "
            f"({written_digest}) does not match sha256 of TIP ({expected_digest})"
        )


if __name__ == "__main__":
    main()
