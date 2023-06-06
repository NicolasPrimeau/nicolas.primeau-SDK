#!/usr/bin/env python3.10
import argparse

from the_one_api_sdk.sdk import TheOneApiSdk


def get_args():
    parser = argparse.ArgumentParser("Get quotes")
    parser.add_argument("-m", "--movie-id", help="Movie ID", required=False, dest="movie_id", type=str, default=None)
    return parser.parse_args()


def main():
    args = get_args()
    sdk = TheOneApiSdk()
    for movie in sdk.quotes.list(movie_id=args.movie_id, limit=100):
        print(movie)


if __name__ == '__main__':
    main()
