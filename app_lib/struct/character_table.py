from app_lib.constants import KEY_NAME


class CharacterTable:
    def __init__(self, character_list):
        super(CharacterTable, self).__init__()
        self.__character_list__ = character_list

    def __getitem__(self, k):
        for character in self.__character_list__:
            if character.get(KEY_NAME) == k:
                return character

        raise KeyError

    def get(self, k, default=None):
        for character in self.__character_list__:
            if character.get(KEY_NAME) == k:
                return character

        return default

    def items(self):
        return self.__character_list__

    def keys(self):
        return {character[KEY_NAME] for character in self.__character_list__}

    def values(self):
        return super().values()

    def __repr__(self) -> str:
        return repr(self.__character_list__)
