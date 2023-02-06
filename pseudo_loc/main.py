import os
import sys
import logging

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

import utils
from pseudo_loc.lib import Localizer
from pseudo_loc.app_output_target import customize
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, width=80)


class Processor:
    def __init__(self, reader, localizer, writer, exclusion_list, output_target):
        self.localizer = localizer
        self.reader = reader
        self.writer = writer
        self.content = None
        self.exclusion_list = exclusion_list
        self.output_target = output_target

    def execute(self):
        try:
            self.content = self.reader.read()
            # pp.pprint(self.content)
        except FileNotFoundError:
            print("Error: File Not Found: {}".format(self.reader.filename))
            return

        set_of_identifiers = set([])
        if self.exclusion_list:
            data = self.exclusion_list.read()
            list_of_identifiers = data.split("\n")
            set_of_identifiers = set(list_of_identifiers)

            print("Exclusion List:", set_of_identifiers)

        results = {}
        for message_id, message in self.content.items():
            if message is None:
                continue

            if type(message) is dict and message['message'] is not None:
                message = message['message']

            logging.info("Pseudo-localize: \"{0}\": \"{1}\"".format(message_id, message))

            if message_id in set_of_identifiers:
                localized = message
            else:
                localized = self.localizer.localize(message)

            print(f'localized message: {localized}')

            results[message_id] = {
                "message": localized
            }
        os.makedirs(self.output_target['folder_path'], exist_ok=True)
        self.writer.write(results)


def main(args):
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
        filename='pseudo_loc.log', level=logging.INFO)

    logging.info(f"Input files: {args.files}")
    logging.info(f"Output folder: {args.output_folder}")
    logging.info(f"Exclusion list: {args.exclusion_list}")
    logging.info(f"Add Padding: {args.pad}")

    localizer = Localizer()
    localizer.pad_text = args.pad

    for filename in args.files:
        logging.info(f"Processing \"{filename}\"...")
        reader = utils.FileReader.get(filename)

        output_target: dict = customize(filename, args.output_folder)
        writer = utils.FileWriter.get(output_target['file_path'])

        Processor(reader, localizer, writer, args.exclusion_list, output_target).execute()

        print(f"The pseudo-localized file has been saved here: {output_target['file_path']}")
