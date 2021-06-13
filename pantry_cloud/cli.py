from .pantry_cloud import Pantry
from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-a", "--api", help="api key.", dest="api", required=True)
    parser.add_argument("-o", "--output", help="output file.", dest="output_file")
    parser.add_argument("-i", "--input", help="input file.", dest="input_file")
    parser.add_argument(
        "-s", "--show", help="Shows account details.", action="store_true"
    )
    parser.add_argument("-b", "--basket", help="Shows data of a basket.", dest="basket")
    parser.add_argument("-u", "--update", help="Updates a basket.", dest="update")
    parser.add_argument(
        "-c",
        "--create",
        help="Creates a new basket , or replace an existing one.",
        dest="create",
    )
    parser.add_argument(
        "-d", "--delete", help="Deletes the entire basket.", dest="delete"
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    api = args.api
    pantry = Pantry(api_key=api)

    if args.show:
        data = pantry.show_account(outputfile=args.output_file)
        print(data)
    if args.basket:
        data = pantry.basket(basket=args.basket, outputfile=args.output_file)
        print(data)
    if args.update:
        data = pantry.update(basket=args.basket, outputfile=args.output_file)
        print(data)
    if args.create:
        data = pantry.create(basket=args.basket, inputfile=args.input_file)
        print(data)
    if args.delete:
        data = pantry.delete(basket=args.basket)
        print(data)


if __name__ == "__main__":
    main()
