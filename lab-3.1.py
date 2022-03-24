import math
from pylatex import NoEscape, Subsection

from models import LaboratoryWork


class LaboratoryWork2(LaboratoryWork):
    def purpose(self) -> None:
        pass

    def brief_theory(self) -> None:
        pass

    def main(self) -> None:
        pass


def main():
    LaboratoryWork2(
        number=3.1,
        name='---',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.0')


if __name__ == '__main__':
    main()
