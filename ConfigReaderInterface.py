from abc import ABC, abstractmethod
from ConfigException import InvalidArgName, InvalidFirstArg, InvalidLastArg


class ConfigReaderInterface(ABC):
    def __init__(self):
        self.buffer_size_param_name = "buffer_size"
        self.file_name_for_coder_param_name = "file_name"
        self.coder_run_option_param_name = "coder_option"

        self._param_delimiter = "="

        self._config_dict = \
            {
                self.buffer_size_param_name: None,
                self.file_name_for_coder_param_name: None,
                self.coder_run_option_param_name: None
            }

    @abstractmethod
    def read_config(self, config_file_name: str) -> dict:
        """"
        coder_option can be only "code" or "decode"

        config_dict:return

        ConfigException:raise
        """
        pass

class ConfigForCodingReader(ConfigReaderInterface):
    def read_config(self, config_file_name: str) -> dict:
        with open(config_file_name, 'r') as f:
            while string := f.readline():
                elements = string.split(self._param_delimiter)
                if self._config_dict.get(elements[0].strip(), False) != False:
                    self._config_dict[elements[0].strip()] = elements[1].strip((" |\n"))
                else:
                    raise InvalidArgName("Invalid name of argument")
        if not self._config_dict[self.buffer_size_param_name].isdigit():
            raise InvalidFirstArg("Invalid value of the first argument")

        self._config_dict[self.buffer_size_param_name] = int(self._config_dict[self.buffer_size_param_name])

        if self._config_dict[self.coder_run_option_param_name] != "code" \
            and self._config_dict[self.coder_run_option_param_name] != "decode":
            raise InvalidLastArg("Invalid value of the last argument")

        return self._config_dict
