import argparse

from lib.keyboard import Keyboard


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""Py-dial: Translate numbers to letters""",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('number', help="Phone number.", type=int)

    args = parser.parse_args()
    return args


def run(args=None):
    letters = Keyboard().get_letters(str(args.number))

    print("Number: %s" % args.number)
    print("Letters: %s" % "-".join(letters))


def main():
    run(parse_args())


if __name__ == "__main__":
    main()
