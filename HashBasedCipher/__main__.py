import argparse
from .decipher import Decipher
from .encipher import Encipher


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser", help="Sub-modules")

    # encipher parser
    encipher = subparsers.add_parser("encipher", help="Module to encipher messages with a key")
    encipher.add_argument("key", help="The key you want to encipher the message with")
    encipher.add_argument("message", help="The message", nargs='+')

    # decipher parser
    decipher = subparsers.add_parser("decipher", help="Module to decipher messages")
    decipher.add_argument("key", help="The key you want to decipher the message with")
    decipher.add_argument("message", help="The ciphered message", nargs='+')

    args = parser.parse_args()

    key = str.encode(args.key)
    message = " ".join(args.message)

    if args.subparser == "encipher":
        print(Encipher(key, message).process())
    elif args.subparser == "decipher":
        print(Decipher(key, message).process())


if __name__ == '__main__':
    main()
