from pathlib import Path
import shutil


def main():
    folder = Path(__file__).resolve().parent / "outputs"
    folder.mkdir(exist_ok=True)
    source_file = folder / "source.txt"
    destination_file = folder / "destination.txt"

    try:
        with open(source_file, "w", encoding="utf-8") as file:
            file.write("This is the original content.\n")
            file.write("Adding some more text.")

        with open(source_file, "r", encoding="utf-8") as file:
            content = file.read()
        print("Read content from source file:")
        print(content)

        with open(source_file, "a", encoding="utf-8") as file:
            file.write("\nAppending new content.")

        with open(source_file, "r", encoding="utf-8") as file:
            content = file.read()
        print("\nContent after appending:")
        print(content)

        shutil.copy(source_file, destination_file)
        print("\nFile copied from source.txt to destination.txt.")

        with open(destination_file, "r", encoding="utf-8") as file:
            content = file.read()
        print("\nContent of the destination file:")
        print(content)
    except OSError as error:
        print(f"File operation failed: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
