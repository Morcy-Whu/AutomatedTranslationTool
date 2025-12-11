# TranslateFile
import argparse
from Translate import translate
from GetContent import getcontent
from StoreString import store_string
from Readcontent import read


def main():
    parser = argparse.ArgumentParser(description="Translate content from a text file.")

    parser.add_argument(
        "-i", "--input",
        type=str,
        help="Path to the input text file. If omitted, the default path is used."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to save the translated output. If omitted, the default path is used."
    )
    parser.add_argument(
        "-r", "--read",
        type=bool,
        help="Read aloud the translated result."
    )

    args = parser.parse_args()

    # ----------- Load input -----------
    try:
        content = getcontent(args.input) if args.input else getcontent()
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    print("\n[Original Content]\n", content)

    # ----------- Translate -----------
    try:
        result = translate(content)
    except Exception as e:
        print(f"Translation failed: {e}")
        return

    print("\n[Translated Result]\n", result)

    # ----------- Store output -----------
    try:
        store_string(result, path=args.output)
    except Exception as e:
        print(f"Failed to store output file: {e}")
        return

    # ----------- Optional: read aloud -----------
    if args.read:
        read(text=result)


if __name__ == "__main__":
    main()
