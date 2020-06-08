import enum
import io
import json
import os
import traceback

from app_lib.constants import KEY_NAME
from app_lib.struct.document_descriptor import DocumentDescriptor

CHAR_LINE_FEED = "\f"


class ReadState(enum.Enum):
    READ_HEADER = 0
    READ_CHAR_LIST = 1
    READ_BODY = 2


class DocumentIO:
    def __init__(self):
        pass

    @staticmethod
    def read(document: DocumentDescriptor):
        """
        Read file content.
        :param document: Document object to read from
        """
        document_path = document.document_path
        if os.path.isfile(document_path):
            document.document_path = document_path
            document.character_list.clear()
            with open(document_path, "r") as obo_file:
                doc_body_io = io.StringIO()
                header = {}
                read_state = ReadState.READ_HEADER
                for line in obo_file:
                    if line.startswith(CHAR_LINE_FEED):
                        if read_state == ReadState.READ_HEADER:
                            read_state = ReadState.READ_CHAR_LIST
                        elif read_state == ReadState.READ_CHAR_LIST:
                            read_state = ReadState.READ_BODY
                        continue

                    if read_state == ReadState.READ_HEADER:
                        try:
                            header = json.loads(line)
                        except json.decoder.JSONDecodeError:
                            traceback.print_exc()
                    elif read_state == ReadState.READ_CHAR_LIST:
                        try:
                            character_info = json.loads(line)
                        except json.decoder.JSONDecodeError:
                            traceback.print_exc()

                        if character_info.get(KEY_NAME):
                            document.character_list.append(character_info)
                    elif read_state == ReadState.READ_BODY:
                        doc_body_io.write(line)

                document.output_path = header.get("output_path")
                document.output_name_template = header.get("output_name_template")
                document.index_digits = header.get("index_digits")
                document.document_body = doc_body_io.getvalue()
                document.character_list.append({KEY_NAME: ""})

    @staticmethod
    def write(document: DocumentDescriptor):
        """
        Write content of Qt's document object into file.
        :param document:
        :return: Return value of write attempt.
        """
        document_path = document.document_path
        if document_path:
            with open(document_path, "w") as obo_file:
                header = {"output_path": document.output_path,
                          "output_name_template": document.output_name_template,
                          "index_digits": document.index_digits, }
                obo_file.write(json.dumps(header) + "\n")
                obo_file.write("{}\n".format(CHAR_LINE_FEED))
                for character_info in document.character_list:
                    if character_info.get(KEY_NAME):
                        obo_file.write(json.dumps(character_info) + "\n")
                obo_file.write("{}\n".format(CHAR_LINE_FEED))
                obo_file.write(document.document_body)
