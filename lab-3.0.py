import math
from dataclasses import dataclass

from pylatex import NoEscape, Subsection, LongTabu, MultiRow
from pylatex.utils import bold

import models


@dataclass
class Experiment:
    number: int
    N: int
    Z: float
    T_scale: float
    U_2: float
    U_scale: float
    T: float | None = None
    delta_T: float | None = None
    nu: float | None = None
    omega: float | None = None
    U_max: float | None = None
    delta_U: float | None = None


class LaboratoryWork(models.LaboratoryWork):
    def purpose(self) -> None:
        self.append(NoEscape(r"""
            Ознакомиться с принципом работы электронного осциллографа и приобретение навыков измерения некоторых
            электрических величин с помощью электронного осциллографа.
        """))

    def brief_theory(self) -> None:
        self.append(NoEscape(r"""
            $$U = U_{max} \cdot sin(\omega t + \varphi_0),$$
            
            где $U$ -- мгновенное значение переменного напряжения, $U_{max}$ -- максимальное значение напряжения,
            $\omega$ -- угловая скорость, $t$ -- время, $\varphi_0$ -- начальная фаза напряжения,
            $(\omega t + \varphi_0)$ -- фаза. \\
            
            $$\omega = \frac{2 \pi}{T},$$
            
            где $T$ -- период. \\
            
            $$T = \frac{Z_T}{N_T},$$
            
            где $N_T$ -- количество периодов, $Z_T$ -- количество клеток на $N_T$ периодов. \\
            
            $$U_{max} = \frac{Z_T \cdot M}{2},$$
            
            где $Z_T$ -- количество клеток, $M$ -- масштаб $U$.
        """))

    def main(self) -> None:
        self.append(NoEscape(r"""
            $T = \frac{Z_T}{N} \cdot T_\textup{масштаб} ~ \textup{с}$ \\
            
            $\Delta T = \frac{T_\textup{масштаб}}{10} ~ \textup{с}$ \\
            
            $\nu = \frac{1}{T} ~ \textup{Гц}$ \\
            
            $\omega = 2 \pi \nu ~ \textup{с}^{-1}$ \\
            
            $U_{max} = Z \cdot \frac{U}{2} ~ \textup{В}$ \\
            
            $\Delta U = \frac{U}{10} ~ \textup{В}$
        """))

        experiments = [
            Experiment(number=1, N=4, Z=8.2, T_scale=0.001, U_2=3, U_scale=0.5),
            Experiment(number=2, N=4, Z=8.3, T_scale=0.001, U_2=5.4, U_scale=0.2),
            Experiment(number=3, N=4, Z=9.2, T_scale=0.001, U_2=5.4, U_scale=0.2),
            Experiment(number=4, N=6, Z=9.2, T_scale=0.001, U_2=3.2, U_scale=0.5),
            Experiment(number=5, N=5, Z=8.5, T_scale=0.001, U_2=5.8, U_scale=0.2)
        ]
        fraction = 4

        # вычисление всех нужных значений
        for experiment in experiments:
            experiment.T = (experiment.Z / experiment.N) * experiment.T_scale
            experiment.delta_T = experiment.T / 10
            experiment.nu = 1 / experiment.T
            experiment.omega = 2 * math.pi * experiment.nu
            experiment.U_max = experiment.U_2 * (experiment.U_scale / 2)
            experiment.delta_U = experiment.U_scale / 10

        with self.create(LongTabu("|X[1.5l]|X[0.6l]|X[l]|X[l]|X[l]|X[1.6l]|", row_height=1.5)) as table:
            table.add_hline()
            table.add_row(["Эксперимент",
                           NoEscape(r"$N~(T)$"),
                           NoEscape(r"$Z~(T)$"),
                           NoEscape(r"$T_\textup{масштаб}$"),
                           NoEscape(r"$Z~(2U)$"),
                           NoEscape(r"$U_\textup{масштаб},~\frac{\textup{В}}{\textup{дел}}$")],
                          mapper=bold,
                          escape=False,
                          color="lightgray")
            table.add_hline()
            table.add_hline()

            for experiment in experiments:
                table.add_row([experiment.number,
                               NoEscape(r"$%s$" % (round(experiment.N, fraction, ))),
                               NoEscape(r"$%s$" % (round(experiment.Z, fraction, ))),
                               NoEscape(r"$%s$" % (round(experiment.T_scale, fraction, ))),
                               NoEscape(r"$%s$" % (round(experiment.U_2, fraction, ))),
                               NoEscape(r"$%s$" % (round(experiment.U_scale, fraction, )))],
                              mapper=bold,
                              escape=False,
                              color="lightgray")
                table.add_hline()

        with self.create(LongTabu("|X[1.5l]|X[0.7l]|X[0.7l]|X[0.9l]|X[l]|X[0.7l]|X[0.6l]|", row_height=1.5)) as table:
            table.add_hline()
            table.add_row(["Эксперимент",
                           NoEscape(r"$T,~\textup{с}$"),
                           NoEscape(r"$\Delta T,~\textup{с}$"),
                           NoEscape(r"$\nu,~\textup{Гц}$"),
                           NoEscape(r"$\omega,~\textup{с}^{-1}$"),
                           NoEscape(r"$U_{max},~\textup{В}$"),
                           NoEscape(r"$\Delta U,~\textup{В}$")],
                          mapper=bold,
                          escape=False,
                          color="lightgray")
            table.add_hline()
            table.add_hline()

            for experiment in experiments:
                table.add_row([experiment.number,
                               NoEscape(r"$%s$" % (round(experiment.T, fraction),)),
                               NoEscape(r"$%s$" % (round(experiment.delta_T, fraction),)),
                               NoEscape(r"$%s$" % (round(experiment.nu, fraction),)),
                               NoEscape(r"$%s$" % (round(experiment.omega, fraction),)),
                               NoEscape(r"$%s$" % (round(experiment.U_max, fraction),)),
                               NoEscape(r"$%s$" % (round(experiment.delta_U, fraction),))],
                              mapper=bold,
                              escape=False,
                              color="lightgray")
                table.add_hline()

        self.append(NoEscape(r"""
            $U_{max_3} = \pm %s ~ \textup{В}$ \\
        """ % experiments[2].U_max))
        self.append(NoEscape(r"""
            $T_3 = %s ~ \textup{с}$ \\
        """ % experiments[2].T))
        self.append(NoEscape(r"""
            $\omega_3 = %s ~ \textup{с}^{-1}$ \\
        """ % int(experiments[2].omega)))
        self.append(NoEscape(r"""
            $U_3 = %s \cdot sin(%s t) ~ \textup{В}$ \\
        """ % (experiments[2].U_max, int(experiments[2].omega))))
        self.append(NoEscape(r"""
            $U_{max_3} = (%s \pm 0.05) ~ \textup{В} \Rightarrow \varepsilon_{U} = %s\%%$ \\
        """ % (experiments[2].U_max, int(0.05 / experiments[2].U_max * 100))))
        self.append(NoEscape(r"""
            $T_3 = (%s \pm %s) ~ \textup{с} \Rightarrow \varepsilon_{T} = %s\%%$ \\
        """ % (experiments[2].T, experiments[2].delta_T, int(experiments[2].delta_T / experiments[2].T * 100))))


def main():
    LaboratoryWork(
        number=3.0,
        name='Изучение электронного осциллографа',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.0')


if __name__ == '__main__':
    main()
