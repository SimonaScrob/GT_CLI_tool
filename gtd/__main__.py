import multiprocessing
import os
from xmlrpc.server import SimpleXMLRPCServer
from daemon import daemon
from gtd.api_helper import GoogleTranslateAPIHelper
from settings import SERVER_PORT, SERVER_HOST


def do_line_translation(input_data):
    """
    Uses google translate api helper to translate a sentence.
    :param input_data: tuple (<language>, <text>)
    :return: string
    """
    gt_api_helper = GoogleTranslateAPIHelper()
    translated_line = gt_api_helper.translate_text(input_data[1], input_data[0])
    return translated_line


def start_process():
    """
    Used for debugging purposes.
    """
    print('Starting', multiprocessing.current_process().name)


def translate(file_name, language):
    """
    Reads the text from file and creates subprocesses for translating each line.
    :param file_name: str
    :param language: str
    :return: str
    """
    lines = []
    with open(f"../{file_name}") as file:
        for line in file:
            lines.append((line, language))

    builtin_outputs = map(do_line_translation, lines)
    print('Built-in:', list(builtin_outputs))

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size,
                                initializer=start_process,
                                maxtasksperchild=2,
                                )
    pool_outputs = pool.map(do_line_translation, lines)
    pool.close()
    pool.join()

    return "\n".join(pool_outputs)


def run_server():
    """
    Starts the server
    """
    server = SimpleXMLRPCServer((SERVER_HOST, SERVER_PORT))
    print(f"Listening on port {SERVER_PORT}...")
    server.register_function(translate, "translate")
    server.serve_forever()


here = os.path.dirname(os.path.abspath(__file__))
out = open('checking_print.log', 'w+')

def main():
    """
    Run gtd server as daemon.
    """
    print("Translation daemon started")
    with daemon.DaemonContext(working_directory=here, stdout=out):
        run_server()
