from pylatex import Document, Section, NewPage, VerticalSpace, Center, FlushRight, LargeText, Package
from pylatex.utils import NoEscape
from .enviroments import Titlepage, Sloppypar
from .commands import MakeUppercase


class LaboratoryWork(Document):
    def __init__(self, number: int | float, name: str, group: str, course: int, student: str) -> None:
        super().__init__(
            documentclass='article',
            fontenc='T2A',
            inputenc='utf8',
            lmodern=True,
            page_numbers=True,
            indent=True,
            document_options=["a4paper", "12pt"],
            font_size='large',
            geometry_options=dict(tmargin='2cm', lmargin='1.5cm', rmargin='1.5cm')
        )
        self._number = number
        self._name = name
        self._group = group
        self._course = course
        self._student = student
        self.packages.append(Package('indentfirst'))
        # self.preamble.append(NoEscape(r'\onehalfspacing '))

    def compile(self, filename: str) -> None:
        self._titlepage()
        with self.create(Sloppypar()):
            self._purpose()
            self._brief_theory()
            self._experiments()
        self.generate_pdf(filename, clean_tex=False)

    def _titlepage(self) -> None:
        with self.create(Titlepage()):
            self.append(VerticalSpace('6cm'))
            with self.create(Center()):
                self.extend([
                    LargeText(NoEscape(fr'Лабораторная работа №{self._number} \\')),
                    VerticalSpace('1cm'),
                    LargeText(MakeUppercase(f'<<{self._name}>>')),
                    VerticalSpace('2cm'),
                ])
            with self.create(FlushRight()):
                self.extend([
                    LargeText(NoEscape(fr'Группа: {self._group} \\')),
                    LargeText(NoEscape(fr'Курс: {self._course} \\')),
                    LargeText(NoEscape(fr'Студент: {self._student} \\'))
                ])
        self.append(NewPage())

    def _purpose(self) -> None:
        with self.create(Section('Цель работы')):
            self.purpose()

    def purpose(self) -> None:
        raise NotImplementedError

    def _brief_theory(self) -> None:
        with self.create(Section('Краткая теория')):
            self.brief_theory()
        self.append(NewPage())

    def brief_theory(self) -> None:
        raise NotImplementedError

    def _experiments(self) -> None:
        with self.create(Section('Описание экспериментов')):
            self.experiments()

    def experiments(self) -> None:
        raise NotImplementedError
