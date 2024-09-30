from abc import ABC, abstractmethod


class CoderInterface(ABC):
    @abstractmethod
    def run(self, coder_info: str, string_to_process: str) -> str:
        pass

    @abstractmethod
    def _code(self, string_to_code: str) -> str:
        pass

    @abstractmethod
    def _decode(self, string_to_decode: str) -> str:
        pass

class Coder(CoderInterface):
    def run(self, coder_info: str, string_to_process: str) -> str:
        if coder_info == 'code':
            answer = self._code(string_to_process)
        elif coder_info == 'decode':
            answer = self._decode(string_to_process)
        return answer

    def _code(self, string_to_code: str) -> str:
        answer = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_code = 'pythonabcdefgijklmqrsuvwxz'
        for symbol in string_to_code:
            flag = 0
            if symbol.isalpha():
                if symbol.isupper():
                    symbol = symbol.lower()
                    flag = 1
                if flag == 1:
                    answer.append(alphabet_code[alphabet.find(symbol)].upper())
                    flag = 0
                else:
                    answer.append(alphabet_code[alphabet.find(symbol)])
            else:
                answer.append(symbol)
        return "".join(answer)

    def _decode(self, string_to_decode: str) -> str:
        answer = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_code = 'pythonabcdefgijklmqrsuvwxz'
        for symbol in string_to_decode:
            flag = 0
            if symbol.isalpha():
                if symbol.isupper():
                    symbol = symbol.lower()
                    flag = 1
                if flag == 1:
                    answer.append(alphabet[alphabet_code.find(symbol)].upper())
                    flag = 0
                else:
                    answer.append(alphabet[alphabet_code.find(symbol)])
            else:
                answer.append(symbol)
        return "".join(answer)


#abcdefghijklmnopqrstuvwxyz
#pythonabcdefgijklmqrsuvwxz