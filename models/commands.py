from pylatex import Command


class MakeUppercase(Command):
    def __init__(self, arguments: any) -> None:
        super().__init__('MakeUppercase', arguments)
