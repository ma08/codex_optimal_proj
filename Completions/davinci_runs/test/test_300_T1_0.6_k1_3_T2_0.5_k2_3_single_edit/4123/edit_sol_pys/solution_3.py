from datetime import datetime
from pathlib import Path
from typing import List
from typing import Union
from typing import Any

import os
import sys


class File:
    def __init__(self, path: Union[str, Path]):
        self.path = Path(path).expanduser().resolve()

    def __repr__(self) -> str:
        return f"File({self.path})"

    def __str__(self) -> str:
        return f"{self.path}"

    def __iter__(self) -> List[str]:
        with open(self.path) as f:
            return f.readlines()

    def __len__(self) -> int:
        return len(list(self))

    def __eq__(self, other: Any) -> bool:
        return str(self.path) == str(other.path)

    def __add__(self, other: Any) -> None:
        if isinstance(other, str):
            self.append(other)
        elif isinstance(other, File):
            self.append(other.read())

    def __iadd__(self, other: Any) -> None:
        self.__add__(other)

    def __mul__(self, other: Any) -> None:
        if isinstance(other, int):
            text = self.read()
            for _ in range(other - 1):
                self.append(text)

    def __imul__(self, other: Any) -> None:
        self.__mul__(other)

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()

    def write(self, text: str) -> None:
        with open(self.path, "w") as f:
            f.write(text)

    def append(self, text: str) -> None:
        with open(self.path, "a") as f:
            f.write(text)

    def delete(self) -> None:
        if self.exists():
            os.remove(self.path)

    def rename(self, new_name: str) -> None:
        new_path = self.path.parent.joinpath(new_name)
        self.path.rename(new_path)
        self.path = new_path

    def exists(self) -> bool:
        return self.path.exists()

    def size(self) -> int:
        return self.path.stat().st_size

    def created_at(self) -> datetime:
        return datetime.fromtimestamp(self.path.stat().st_ctime)

    def modified_at(self) -> datetime:
        return datetime.fromtimestamp(self.path.stat().st_mtime)

    def copy(self, destination: Union[str, Path]) -> None:
        destination = Path(destination).expanduser().resolve()
        if destination.is_dir():
            destination = destination.joinpath(self.path.name)
        self.path.copy(destination)

    def move(self, destination: Union[str, Path]) -> None:
        destination = Path(destination).expanduser().resolve()
        if destination.is_dir():
            destination = destination.joinpath(self.path.name)
        self.path.rename(destination)
        self.path = destination

    def name(self) -> str:
        return self.path.name

    def extension(self) -> str:
        return self.path.suffix

    def directory(self) -> str:
        return str(self.path.parent)

    def is_file(self) -> bool:
        return self.path.is_file()

    def is_directory(self) -> bool:
        return self.path.is_dir()
