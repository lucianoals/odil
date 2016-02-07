import argparse
import sys

import _odil

def main():
    parser = argparse.ArgumentParser(description="Convert a DICOM file")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--transfer-syntax", "-t", help="Transfer syntax")
    parser.add_argument(
        "--item-length", "-i", choices=["Explicit", "Undefined"], 
        default="Explicit", help="Item length encoding")
    parser.add_argument(
        "--use-group-length", "-g", action="store_true", 
        help="Include group length tags")
    arguments = parser.parse_args()

    if arguments.transfer_syntax not in dir(_odil.registry):
        parser.error("Unknown transfer syntax")
    uid = getattr(_odil.registry, arguments.transfer_syntax)
    if uid not in _odil.registry.uids_dictionary:
        parser.error("Unknown transfer syntax")
    if _odil.registry.uids_dictionary[uid].type != "Transfer Syntax":
        parser.error("Not a transfer syntax")
    arguments.transfer_syntax = uid

    arguments.item_length = getattr(
        _odil.Writer.ItemEncoding, "{}Length".format(arguments.item_length))

    convert(**arguments.__dict__)

def convert(input, output, transfer_syntax, item_length, use_group_length):
    header, data_set = _odil.read(input)

    to_remove = [
        "FileMetaInformationVersion",
        "MediaStorageSOPClassUID", "MediaStorageSOPInstanceUID", 
        "TransferSyntaxUID", 
        "ImplementationClassUID", "ImplementationVersionName"
    ]
    for name in to_remove:
        header.remove(getattr(_odil.registry, name))

    _odil.write(data_set, output, header, transfer_syntax, item_length, use_group_length)

if __name__ == "__main__":
    sys.exit(main())
