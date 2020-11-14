from typing import List, Any

STRING_CONSTANT = "Ala ma kota"


def count_message_letters(message: str) -> int:
    letters_count = 0
    for _ in message:
        letters_count += 1
    return len(message)


def modify_message_to_list(message: str) -> List[str]:
    return [f"{letter} - {message}" for letter in message]


class SampleClass:
    SOME_CONST = 0

    def __init__(self) -> None:
        self.items = []

    def sample_method(self, item: Any) -> None:
        self.items.append(item)
