#!/usr/bin/env python3.10
import argparse

from the_one_api_sdk.sdk import TheOneApiSdk


def get_args():
    parser = argparse.ArgumentParser("Specify a movie to fetch")
    parser.add_argument("-m", "--movie-id", help="Movie ID", required=True, dest="movie_id", type=str)
    return parser.parse_args()


def main():
    args = get_args()
    sdk = TheOneApiSdk()
    print(sdk.movies(args.movie_id).fetch())


if __name__ == '__main__':
    main()
