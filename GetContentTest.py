# GetContentTest.py
from GetContent import getcontent
import argparse

# A = getcontent()
# print(A)
# # Output
# # Hello world.
#
# B = getcontent(r"C:\Users\ericm\Desktop\Tem\Tem.txt")
# print(B)
# # Output
# # I love python

def main():
    parser = argparse.ArgumentParser(description="Get content from a text file.")

    # Add -p parameter
    parser.add_argument(
        "-p",
        "--path",
        type = str,
        help = "path to the txt file. If omitted, the default path is used"
    )

    args = parser.parse_args()
    if args.path is None:
        result = getcontent()
    else:
        result = getcontent(args.path)
    print(result)

if __name__ == "__main__":
    main()

