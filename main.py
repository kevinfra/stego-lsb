import sys
import argparse
from stego import decode,hide,formulas


parser = argparse.ArgumentParser("ECI Steganographer", description = 'Steganography CLI tool that uses LSB manipulation to encode text into BMP images')
subparsers = parser.add_subparsers(dest = "subparser")

parser_hide = subparsers.add_parser("hide", help = "hide text in image")
parser_hide.add_argument("--infile", "-i", type=str, nargs=1, required=True)
parser_hide.add_argument("--bytes", "-b", type=int, nargs=1, choices=(2,3,4,5,6,7,8), required=True)
parser_hide.add_argument("--text", "-t", type=str, nargs=1, required=True)

parser_decode = subparsers.add_parser("decode", help = "extract text from image")
parser_decode.add_argument("--infile", "-i", type=str, nargs=1, required=True)

parser_decode = subparsers.add_parser("compare", help = "compare two images")
parser_decode.add_argument("--first", "-f", type=str, nargs=1, required=True)
parser_decode.add_argument("--second", "-s", type=str, nargs=1, required=True)


if __name__ == '__main__':
    args = vars(parser.parse_args())
    if args.get("subparser") is None:
        print(parser.print_help())
    else:
        command = args.get("subparser")
        if command == "hide":
            image = args["infile"][0]
            if not image.endswith(".bmp"):
                print("non-bmp image passed as input")
                sys.exit(0)
            hide.hide(args['infile'][0], args['text'][0], args['bytes'][0])
        elif command == "decode":
            image = args["infile"][0]
            if not image.endswith(".bmp"):
                print("non-bmp image passed as input")
                sys.exit(0)
            print(decode.decode(image))
        elif command == "compare":
            first = args["first"][0]
            if not first.endswith(".bmp"):
                print("non-bmp image passed as input")
                sys.exit(0)
            second = args["second"][0]
            if not second.endswith(".bmp"):
                print("non-bmp image passed as input")
                sys.exit(0)
            res = formulas.compare(first,second)
            print(f"MSE: {res[0]}\nPS2NR: {res[1]}\nSSIM: {res[2]}")

