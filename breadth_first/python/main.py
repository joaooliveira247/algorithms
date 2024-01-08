from collections import deque
from dataclasses import dataclass
from typing import TypeVar
from icecream import ic

Self = TypeVar("Self", bound="Graph")


@dataclass
class Person:
    name: str
    is_mango_seller: bool


class Graph:
    __iter_index: int = 0

    def __init__(self) -> None:
        self.__slot__: dict[str, Person] = {}

    def __repr__(self) -> str:
        return f"({self.__class__.__name__}): {self.__slot__}"

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, name: str) -> list[Person]:
        return self.__slot__[name]

    def add_node(self, name: str, *person: Person) -> str:
        self.__slot__[name] = list(person)
        return f"{name}: {[*person]}"

    def __iter__(self) -> Self:
        self.__static_graph_values: list[tuple[str, Person]] = list(
            self.__slot__.items()
        )
        return self

    def __next__(self) -> tuple[str, list[Person]]:
        if self.__iter_index >= len(self.__slot__):
            raise StopIteration
        value = self.__static_graph_values[self.__iter_index]
        self.__iter_index += 1
        return value


def search(name: str, graph: Graph) -> (str, bool):
    search_queue: deque = deque()
    search_queue += graph[name]
    searched: list[Person] = []
    while search_queue:
        person: Person = search_queue.popleft()
        if not person.name in searched:
            if person.is_mango_seller:
                return f"{person.name} is mango seller", True
            search_queue += graph[person.name]
            searched.append(person.name)
    return "", False


def main() -> None:
    fnf = Graph()
    fnf.add_node(
        "you",
        Person("Alice", False),
        Person("Bob", False),
        Person("Claire", False),
    )
    fnf.add_node("Bob", Person("Anuj", False), Person("Peggy", False))
    fnf.add_node("Alice", Person("Peggy", False))
    fnf.add_node("Claire", Person("Tom", True), Person("Jonny", False))
    fnf.add_node("Anuj")
    fnf.add_node("Peggy")
    fnf.add_node("Thom")
    fnf.add_node("Jonny")

    response, status = search("you", fnf)

    if status:
        print(response)
    return


if __name__ == "__main__":
    main()
