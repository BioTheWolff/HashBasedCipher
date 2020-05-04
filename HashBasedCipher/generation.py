import hashlib
import random


def move_all_elements_to_right(to_move: list, times: int = 1) -> list:
    if times < 1:
        return to_move

    for i in range(times):
        to_move.insert(0, to_move.pop(len(to_move) - 1))

    return to_move


class HashBasedGeneration:

    letters_no_caps = [chr(i) for i in range(97, 97 + 26)]
    letters_caps = [chr(i) for i in range(65, 65 + 26)]
    figures = [chr(i) for i in range(48, 58)]
    ordered = letters_no_caps + letters_caps + figures

    __key = None
    __hash = None
    __generated = None

    def __init__(self, key: bytes) -> None:
        if not isinstance(key, bytes):
            raise Exception('Key must be bytes')

        self.__key = key
        self.__hash = ''
        self.__generated = []

    def generate(self):
        self.__hash = hashlib.sha1(self.__key).hexdigest()

        for e in self.__hash:
            random.seed(e, version=2)
            gen = random.random() * 60

            temp = self.ordered.copy()
            temp = move_all_elements_to_right(temp, round(gen))

            self.__generated.append(temp)

        return self.__generated
