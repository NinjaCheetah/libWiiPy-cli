# "u8.py" from WiiPy by NinjaCheetah
# https://github.com/NinjaCheetah/WiiPy

import pathlib
import libWiiPy


def handle_u8(args):
    input_path = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)

    if args.pack:
        try:
            u8_data = libWiiPy.archive.pack_u8(input_path)
        except ValueError:
            print("Error: Specified input file/folder does not exist!")
            return

        out_file = open(output_path, "wb")
        out_file.write(u8_data)
        out_file.close()

        print("U8 archive packed!")

    elif args.unpack:
        if not input_path.exists():
            raise FileNotFoundError(args.input)

        u8_data = open(input_path, "rb").read()

        if output_path.exists():
            print("Error: Specified output directory already exists!")
            return

        libWiiPy.archive.extract_u8(u8_data, str(output_path))

        print("U8 archive unpacked!")
