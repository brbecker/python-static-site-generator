import shutil
from pathlib import Path
from typing import List


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension: str) -> bool:
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path) -> None:
        raise NotImplementedError

    def read(self, path: Path) -> str:
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext: str = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path) -> None:
        self.copy(path, source, dest)
