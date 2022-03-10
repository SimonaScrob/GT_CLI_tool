import argparse
import os
import xmlrpc.client

from settings import SERVER_HOST, SERVER_PORT, LANGUAGES


def main():
    """
    Function used to parse the command line arguments and communicate with the daemon server for translation.
    """
    description = "gtanslate 1.0: command line utility for translating text"
    usage = "gtranslate -f <filename> -l <lang>"

    parser = argparse.ArgumentParser(description=description, usage=usage)
    parser.add_argument('-f', help='<filename> path to input filename to be translated')
    parser.add_argument('-l', help=' <lang> output language, should be one of "en", "it" or "de"')

    args = parser.parse_args()

    if args.l in LANGUAGES and os.path.exists(args.f):
        with xmlrpc.client.ServerProxy(f"http://{SERVER_HOST}:{SERVER_PORT}/") as proxy:
            translated_text = proxy.translate(args.f, args.l)
            print(translated_text)
    else:
        print('Wrong language or filename')


if __name__ == '__main__':
    main()
