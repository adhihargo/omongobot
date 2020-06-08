import os


class DocumentDescriptor(object):
    def __init__(self, document_path):
        super(DocumentDescriptor, self).__init__()

        self.document_path = document_path

        self.output_path = ""
        self.output_name_template = ""
        self.index_digits = 2

        self.character_list = []
        self.document_body = ""

    @property
    def output_path_template(self):
        """
        :return:
        """
        indexed_name_template = self.output_name_template.replace("{INDEX}", "{{INDEX:0{}d}}".format(self.index_digits))
        return os.path.join(self.output_path, indexed_name_template)

    def reset(self):
        self.document_path = ""

        self.output_path = ""
        self.output_name_template = ""
        self.index_digits = 2

        self.character_list = []
        self.document_body = ""
