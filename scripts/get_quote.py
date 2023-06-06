#!/usr/bin/env python3.10
import argparse

from the_one_api_sdk.sdk import TheOneApiSdk


def get_args():
    parser = argparse.ArgumentParser("Specify a quote to fetch")
    parser.add_argument("-q", "--quote-id", help="Quote ID", required=True, dest="quote_id", type=str)
    return parser.parse_args()


def main():
    args = get_args()
    sdk = TheOneApiSdk()
    print(sdk.quotes(args.quote_id).fetch())


if __name__ == '__main__':
    main()
