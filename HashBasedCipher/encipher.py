from .generation import HashBasedGeneration


class Encipher:

    __plain_message = None
    __final_message = None
    __key = None

    __generated = None
    __dicts = None

    def __init__(self, key: bytes, message: str):
        self.__key = key
        self.__plain_message = message
        self.__final_message = ''

    def __call__(self):
        self.process()

    def process(self):
        self.__generated = HashBasedGeneration(self.__key).generate()

        # We program the dicts to encode
        self.__dicts = [dict(zip(HashBasedGeneration.ordered, e)) for e in self.__generated]

        # Then we encode the message
        i = len(self.__key) % len(self.__dicts)
        dict_max_index = len(self.__dicts)

        temp_final_message = []

        for c in self.__plain_message:
            i += 1
            if i >= dict_max_index:
                i = 0

            final = ''
            try:
                final = self.__dicts[i][c]
            except KeyError:
                final = c
            finally:
                temp_final_message.append(final)

        # We regroup everything into a single string
        self.__final_message = "".join(temp_final_message)
        return self.__final_message

    @property
    def message(self):
        return self.__final_message if self.__final_message != '' else None
