import os
from typing import Generator


class ESpeakNG(object):
    def __init__(self, bin_path: str = "", args: list = None):
        """
        :param bin_path: Absolute path of ESpeakNG executable binary.
        :param args: List of execution command line arguments.
        """
        self.bin_path = bin_path
        self.args = args or []
        self.value_generator = []

    @property
    def base_cmd_list(self) -> list:
        """
        :return: List of base command string if bin_path is valid, otherwise an empty string.
        """
        valid_cmd_list = [self.bin_path] + self.args
        return valid_cmd_list if os.path.isfile(self.bin_path) else []

    def iter_cmd_list(self, value_generator: list = None):
        """
        :param value_generator: Generator of (override_args, line) pair, where override_args is arguments overriding main
        ones, to be applied when executing line. If None, use value_list given from set_value_list.
        """
        cmd_list = self.base_cmd_list
        if value_generator is None:
            value_generator = self.value_generator
        if cmd_list:
            for override_args, line in value_generator:
                tmp_cmd_list = cmd_list + override_args
                yield tmp_cmd_list, line

    def set_value_generator(self, value_generator: Generator):
        if not isinstance(value_generator, Generator):
            return

        self.value_generator = value_generator

    def __str__(self) -> str:
        return " ".join(self.base_cmd_list)

    def __repr__(self) -> str:
        return 'ESpeakNG(bin_path="{}", args="{}")'.format(self.bin_path, self.args)
