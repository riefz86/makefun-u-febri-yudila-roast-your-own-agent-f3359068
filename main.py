import os

ROAST = "My agent spent nine minutes 'verifying' a file it never opened, then announced the check passed — grading its own homework and giving itself an A."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
