#!/usr/bin/env python3.10
from the_one_api_sdk.sdk import TheOneApiSdk


def main():
    sdk = TheOneApiSdk()
    for movie in sdk.movies.list():
        print(movie)


if __name__ == '__main__':
    main()
