from abc import ABC, abstractmethod
from contextlib import contextmanager
from ConfigException import InvalidPath


class FileReaderInterface(ABC):
    @abstractmethod
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        """"generate buffer file reader"""
        pass

class FileForCodingReader(FileReaderInterface):
    @contextmanager
    def read_file(self, file_name: str, buffer_size: int):
        try:
            f = open(file_name, "r", buffering=buffer_size)
            yield f.readline()
        except Exception as e:
            return InvalidPath("Invalid file path")
        finally:
            f.close()
