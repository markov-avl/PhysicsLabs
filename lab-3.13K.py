import math
import os
from dataclasses import dataclass

from pylatex import NoEscape, Subsection, LongTabu, MultiRow, Figure
from pylatex.utils import bold

import models


L = 1


@dataclass
class Experiment:
    number: int
    Ri: int
    


class LaboratoryWork(models.LaboratoryWork):
    def purpose(self) -> None:
        self.append(NoEscape(r"""
            Познакомиться с методом расчёта параметров электрической цепи, основанном на использовании мостовых схем
            (мост постоянного тока), найти неизвестное сопротивление при помощи моста.
        """))

    def brief_theory(self) -> None:
        self.append(NoEscape(r"""
            Для однородного участка цепи закон Ома выражается формулой:
            $$I = \frac{U}{R},$$
            
            где $U$ -- напряжение на данном участке, $R$ -- сопротивление участка, $I$ -- сила тока в нем. \\ [0.25cm]
            
            Следующая схема представляет электрическую цепь <<Мост постоянного тока>>.
        """))

        self.append(NoEscape(r'\renewcommand{\figurename}{Рисунок}'))
        with self.create(Figure(position='h!')) as image:
            image.add_image(os.path.join(os.path.dirname(__file__), 'graphics/dc-bridge.pdf'), width='200px')
            image.add_caption('Мост постоянного тока')

        # TODO: не дописана
        self.append(NoEscape(r"""
            На участке (СД) направление и величина тока будут зависеть от сопротивлений участков $1, 2, 3, 4$.
        """))

    def main(self) -> None:
        pass


def main():
    LaboratoryWork(
        number='3.13K',
        name='Определение неизвестного сопротивления при помощи моста постоянного тока',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.13K')


if __name__ == '__main__':
    main()
