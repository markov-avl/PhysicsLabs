import math
import os
from dataclasses import dataclass

from pylatex import NoEscape, Subsection, LongTabu, MultiRow, Figure
from pylatex.utils import bold

import models

L = 1
R = {1: 10000, 2: 3300, 3: 2200}


@dataclass
class Experiment:
    number: int
    x_1: float
    x_2: float
    x_3: float
    R_x: float = 0
    e_x: float = 0
    e_R_x: float = 0
    delta_R_x: float = 0
    R_x_1_i: float = 0
    R_x_2_i: float = 0
    R_x_3_i: float = 0
    x_avg: float = 0


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

        self.append(NoEscape(r"""
            На участке (СД) направление и величина тока будут зависеть от сопротивлений участков $1, 2, 3, 4$.
            
            Применим для уравновешанного моста правила Кирхгофа. Если в участке СД ток отсутствует, то в ветвях 1, 2
            сила тока будет одинакова. То же самое можно сказать о силе тока в ветвях 3, 4. В этом случае для конутров
            АСДА с ДСВД на основании 2 Кирхгофа можно записать уравнения:
            
            $$I_1 R_1 - I_2 R_3 = 0~,~I_1 R_2 - I_2 R_4 = 0 \Rightarrow \frac{R_1}{R_2} = \frac{R_3}{R_4}$$
        """))

    def main(self) -> None:
        self.append(NoEscape(r"""
            $l = 1~\textup{м}$ \\
            
            $\overline{R_{{x_j}_i}} = R_{\textup{э}_j} \cdot \frac{l - x_j}{x_j} ~ \textup{Ом}$ \\
            
            $\overline{R_{x_i}} = \frac{\sum_{j = 1}^{n}\overline{R_{{x_j}_i}}}{n} ~ \textup{Ом}$ \\
            
            $\varepsilon_{x_i} = \frac{\sum_{j = 1}^{n}\frac{\Delta x_{j_i}}{x_{j_i}}}{n} ~ \textup{м}$ \\
            
            $\varepsilon_{R_{x_i}} = \sqrt{\varepsilon_{x_i}^2 + \varepsilon_{R_\textup{э}}^2} ~ \textup{Ом}$ \\
            
            $\Delta R_{x_i} = \overline{R_{x_i}} \cdot \varepsilon_{R_{x_i}} ~ \textup{Ом}$ \\
        """))

        experiments = [
            Experiment(1, 0.39, 0.17, 0.13),
            Experiment(2, 0.93, 0.86, 0.8)
        ]
        fraction = 2

        for experiment in experiments:
            experiment.x_avg = (experiment.x_1 + experiment.x_2 + experiment.x_3) / 3
            R_avg = (R[1] + R[2] + R[3]) / 3
            experiment.R_x_1_i = R[1] * ((L - experiment.x_1) / experiment.x_1)
            experiment.R_x_2_i = R[2] * ((L - experiment.x_2) / experiment.x_2)
            experiment.R_x_3_i = R[3] * ((L - experiment.x_3) / experiment.x_3)

            experiment.R_x = (experiment.R_x_1_i + experiment.R_x_2_i + experiment.R_x_3_i) / 3
            experiment.e_x = (abs(experiment.x_avg - experiment.x_1) / experiment.x_1 +
                              abs(experiment.x_avg - experiment.x_2) / experiment.x_2 +
                              abs(experiment.x_avg - experiment.x_3) / experiment.x_3) / 3
            experiment.e_R_x = 0
            experiment.delta_R_x = 0
            # experiment.e_R_x = math.sqrt(experiment.e_x ** 2 + R_avg ** 2)
            # experiment.delta_R_x = experiment.R_x * experiment.e_R_x

        with self.create(LongTabu("|X[0.2l]|X[l]|X[l]|X[l]|X[0.6l]|X[0.3l]|X[0.3l]|X[0.4l]|", row_height=1.5)) as table:
            table.add_hline()
            table.add_row([MultiRow(2, data=NoEscape(r"№")),
                           NoEscape(r"$R_{\textup{э}_1}~(10~\textup{кОм})$"),
                           NoEscape(r"$R_{\textup{э}_2}~(3.3~\textup{кОм})$"),
                           NoEscape(r"$R_{\textup{э}_3}~(2.2~\textup{кОм})$"),
                           NoEscape(r"$\overline{R_x},$"),
                           NoEscape(r"$\varepsilon_x,$"),
                           NoEscape(r"$\varepsilon_{R_x},$"),
                           NoEscape(r"$\Delta \overline{R_x},$")],
                          escape=False,
                          color="lightgray")
            self.append(NoEscape(r"\cline{2-4}"))
            table.add_row(["",
                           NoEscape(r"$x_1,~\textup{м}$"),
                           NoEscape(r"$x_2,~\textup{м}$"),
                           NoEscape(r"$x_3,~\textup{м}$"),
                           NoEscape(r"\textup{Ом}"),
                           NoEscape(r"\textup{м}"),
                           NoEscape(r"\textup{Ом}"),
                           NoEscape(r"\textup{Ом}")],
                          escape=False,
                          color="lightgray")
            table.add_hline()
            table.add_hline()

            for experiment in experiments:
                table.add_row([NoEscape(r"$%d$" % experiment.number),
                               NoEscape(r"$%s$" % experiment.x_1),
                               NoEscape(r"$%s$" % experiment.x_2),
                               NoEscape(r"$%s$" % experiment.x_3),
                               NoEscape(r"$%s$" % round(experiment.R_x, fraction)),
                               NoEscape(r"$%s$" % round(experiment.e_x, fraction)),
                               "",
                               ""],
                              # NoEscape(r"$%s$" % round(experiment.e_R_x, fraction)),
                              # NoEscape(r"$%s$" % round(experiment.delta_R_x, fraction))],
                              escape=False,
                              color="lightgray")
                table.add_hline()

        self.append(NoEscape(r"""
            $\overline{R_{{x_1}_1}} = %s \cdot \frac{%s - %s}{%s} = %s ~ \textup{Ом}$ \\
        """ % (R[1], L, experiments[0].x_1, experiments[0].x_1, round(experiments[0].R_x_1_i, fraction))))
        self.append(NoEscape(r"""
            $\overline{R_{{x_1}_2}} = %s \cdot \frac{%s - %s}{%s} = %s ~ \textup{Ом}$ \\
        """ % (R[2], L, experiments[0].x_2, experiments[0].x_2, round(experiments[0].R_x_2_i, fraction))))
        self.append(NoEscape(r"""
            $\overline{R_{{x_1}_3}} = %s \cdot \frac{%s - %s}{%s} = %s ~ \textup{Ом}$ \\
        """ % (R[3], L, experiments[0].x_3, experiments[0].x_3, round(experiments[0].R_x_3_i, fraction))))
        self.append(NoEscape(r"""
            $\overline{R_{x_1}} = \frac{%s + %s + %s}{3} = %s ~ \textup{Ом}$ \\
        """ % (round(experiments[0].R_x_1_i, fraction),
               round(experiments[0].R_x_2_i, fraction),
               round(experiments[0].R_x_3_i, fraction),
               round(experiments[0].R_x, fraction))))
        self.append(NoEscape(r"""
            $\overline{x_1} = \frac{%s + %s + %s}{3} = %s ~ \textup{м}$ \\
        """ % (experiments[0].x_1,
               experiments[0].x_2,
               experiments[0].x_3,
               round(experiments[0].x_avg, fraction))))
        self.append(NoEscape(r"""
            $\varepsilon_{x_1} = \frac{\frac{|%s - %s|}{%s} + \frac{|%s - %s|}{%s} + \frac{|%s - %s|}{%s}}{3} = %s ~ \textup{м}$ \\
        """ % (experiments[0].x_avg,
               experiments[0].x_1,
               experiments[0].x_1,
               experiments[0].x_avg,
               experiments[0].x_2,
               experiments[0].x_2,
               experiments[0].x_avg,
               experiments[0].x_3,
               experiments[0].x_3,
               round(experiments[0].e_x, fraction))))


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
