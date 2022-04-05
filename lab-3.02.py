import math
from dataclasses import dataclass
from typing import NamedTuple

from pylatex import NoEscape, Subsection, LongTabu
from pylatex.utils import bold

from models import LaboratoryWork


@dataclass
class Data:
    number: int
    l: float
    U: float
    I: float
    lambda_: float | None = None
    delta_lambda: float | None = None
    R: float | None = None
    U_2: float | None = None
    IU: float | None = None


class LaboratoryWork2(LaboratoryWork):
    def purpose(self) -> None:
        pass

    def brief_theory(self) -> None:
        pass

    def main(self) -> None:
        self.append(NoEscape(r"""
            $I = \frac{U}{R}$ (закон Ома)
            
            ...
        """))

        datas = [
            Data(number=1, l=0.3, U=0.3, I=0.09),
            Data(number=2, l=0.3, U=0.4, I=0.115),
            Data(number=3, l=0.3, U=0.5, I=0.145),
            Data(number=4, l=0.3, U=0.6, I=0.175),
            Data(number=5, l=0.3, U=0.7, I=0.2),
            Data(number=1, l=0.4, U=0.4, I=0.09),
            Data(number=2, l=0.4, U=0.6, I=0.135),
            Data(number=3, l=0.4, U=0.8, I=0.18),
            Data(number=4, l=0.4, U=1.0, I=0.220),
            Data(number=5, l=0.4, U=1.1, I=0.245),
            Data(number=1, l=0.5, U=0.4, I=0.07),
            Data(number=2, l=0.5, U=0.6, I=0.105),
            Data(number=3, l=0.5, U=0.8, I=0.14),
            Data(number=4, l=0.5, U=1.0, I=0.18),
            Data(number=5, l=0.5, U=1.2, I=0.215)
        ]

        fraction = 4
        experiments = 5

        lambda_average = {}
        u_2_sum = {}
        iu_sum = {}

        for data in datas:
            data.lambda_ = data.I / data.U
            data.R = 1 / data.lambda_
            data.U_2 = data.U ** 2
            data.IU = data.I * data.U
            if data.number == experiments:
                experiment = list(filter(lambda d: d.l == data.l, datas))
                lambda_values = list(map(lambda d: d.lambda_, experiment))
                lambda_average[data.l] = sum(lambda_values) / len(lambda_values)
                u_2_sum[data.l] = sum(map(lambda d: d.U_2, experiment))
                iu_sum[data.l] = sum(map(lambda d: d.IU, experiment))

        for data in datas:
            data.delta_lambda = abs(lambda_average[data.l] - data.lambda_)

        with self.create(Subsection(NoEscape(r'Зависимость силы тока $I$ от напряжения $U$'))):
            with self.create(LongTabu("|X[l]|X[l]|X[l]|X[l]|X[l]|X[l]|X[l]|", row_height=1.5)) as table:
                table.add_hline()
                table.add_row(["№",
                               NoEscape(r"$l,~\textup{м}$"),
                               NoEscape(r"$U,~\textup{В}$"),
                               NoEscape(r"$I,~\textup{А}$"),
                               NoEscape(r"$\lambda,~\textup{См}$"),
                               NoEscape(r"$\Delta \lambda,~\textup{См}$"),
                               NoEscape(r"$R,~\textup{Ом}$")],
                              mapper=bold,
                              escape=False,
                              color="lightgray")
                table.add_hline()
                table.add_hline()
                for data in datas:
                    table.add_row([r"$%s$" % data.number,
                                   r"$%s$" % data.l,
                                   r"$%s$" % data.U,
                                   r"$%s$" % data.I,
                                   r"$%s$" % round(data.lambda_, fraction),
                                   r"$%s$" % round(data.delta_lambda, fraction),
                                   r"$%s$" % round(data.R, fraction)],
                                  escape=False)

                    table.add_hline()
                    if data.number == experiments:
                        table.add_row([NoEscape(r"$\textup{средние}$"),
                                       "",
                                       "",
                                       "",
                                       r"$%s$" % round(lambda_average[data.l], fraction),
                                       "",
                                       ""],
                                      escape=False)
                        table.add_hline()

        with self.create(Subsection(NoEscape(r'Зависимость силы тока $I$ от напряжения $U$ '
                                             r'(метод наименьших квадратов)'))):
            with self.create(LongTabu("|X[l]|X[l]|X[l]|X[l]|X[l]|X[1.2l]|X[l]|X[l]|X[l]|", row_height=1.5)) as table:
                table.add_hline()
                table.add_row(["№",
                               r"$l,~\textup{м}$",
                               r"$U,~\textup{В}$",
                               r"$U^2,~\textup{В}^2$",
                               r"$I,~\textup{А}$",
                               r"$IU,~\textup{А} \cdot \textup{В}$",
                               r"$\lambda,~\textup{См}$",
                               r"$\Delta \lambda,~\textup{См}$",
                               r"$R,~\textup{Ом}$"],
                              escape=False,
                              color="lightgray")
                table.add_hline()
                table.add_hline()
                for data in datas:
                    table.add_row([r"$%s$" % data.number,
                                   r"$%s$" % data.l,
                                   r"$%s$" % data.U,
                                   r"$%s$" % round(data.U_2, fraction),
                                   r"$%s$" % data.I,
                                   r"$%s$" % round(data.IU, fraction),
                                   r"$%s$" % round(data.lambda_, fraction),
                                   r"$%s$" % round(data.delta_lambda, fraction),
                                   r"$%s$" % round(data.R, fraction)],
                                  escape=False)

                    table.add_hline()
                    if data.number == experiments:
                        table.add_row([r"$\textup{суммы}$",
                                       "",
                                       "",
                                       r"$%s$" % round(u_2_sum[data.l], fraction),
                                       "",
                                       r"$%s$" % round(iu_sum[data.l], fraction),
                                       "",
                                       "",
                                       ""],
                                      escape=False)
                        table.add_hline()


def main():
    LaboratoryWork2(
        number=3.02,
        name='НЕИЗВЕСТНО',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.02')


if __name__ == '__main__':
    main()
