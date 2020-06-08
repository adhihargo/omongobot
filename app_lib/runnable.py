import subprocess

from PySide2 import QtCore

from app_lib.espeakng import ESpeakNG


class Runnable(QtCore.QRunnable):
    def __init__(self, espeak_obj: ESpeakNG):
        super(Runnable, self).__init__()
        self.espeak_obj = espeak_obj

        self.__interrupt_mutex__ = QtCore.QMutex()
        self.__set_interrupt__(False)

        self.__running_mutex__ = QtCore.QMutex()
        self.__set_is_running__(False)

    def isRunning(self):
        self.__running_mutex__.lock()
        is_running = self.__running__
        self.__running_mutex__.unlock()
        return is_running

    def run(self):
        self.__set_is_running__(True)

        for cmd_list, line in self.espeak_obj.iter_cmd_list():
            popen = subprocess.Popen(cmd_list, stdin=subprocess.PIPE)
            popen.communicate(bytearray(line, "utf-8"))

            self.__interrupt_mutex__.lock()
            interrupt = self.__interrupt__
            self.__interrupt_mutex__.unlock()
            if interrupt:
                break

        self.__set_is_running__(False)

    def requestInterruption(self):
        self.__set_interrupt__(True)

    def __set_is_running__(self, value):
        self.__running_mutex__.lock()
        self.__running__ = value
        self.__running_mutex__.unlock()

    def __set_interrupt__(self, value):
        self.__interrupt_mutex__.lock()
        self.__interrupt__ = value
        self.__interrupt_mutex__.unlock()
