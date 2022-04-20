import math
from dataclasses import dataclass

from pylatex import NoEscape, Subsection, LongTabu, MultiRow
from pylatex.utils import bold

import models


@dataclass
class Data:
    number: int
    l: float
    U: float
    I: float
    lambda_: float | None = None
    delta_lambda: float | None = None
    R: float | None = None
    R_: float | None = None
    U_2: float | None = None
    IU: float | None = None


class LaboratoryWork(models.LaboratoryWork):
    def purpose(self) -> None:
        self.append(NoEscape(r"""
            Определение сопротивления с помощью закона Ома на однородном участке цепи. Ознакомление с обработкой
            методом наименьших квадратов.
        """))

    def brief_theory(self) -> None:
        self.append(NoEscape(r"""
            $$I = \lambda (\varphi_1 - \varphi_2) = \lambda \cdot U,$$

            где $I$ -- сила тока в проводнике, $\lambda$ -- коэффициент пропорциональности между напряжением на
            концах проводника и силой тока в это проводнике, а $\varphi_1 - \varphi_2$ -- разность потенциалов, что
            по сути является напряжением $U$. \\ [0.25cm]
            
            Электрическое сопротивление $R$ -- физическая скалярная величина, характеризующая свойство проводника
            умешать скорость упорядоченного движения свободных носителей зарядов в проводнике. Единицей измерения
            электрического сопротивления проводника является Ом ($1 ~ \textup{Ом} = \frac{1 ~ {\textup{В}}}
            {1 ~ \textup{А}}$).
            
            $$R = \frac{U}{I},$$
            
            данное выражение носит имя <<Закон Ома для однородного участка цепи>>. \\ [0.25cm]
            
            Сопротивление однородного металлического проводника $R$, как и его проводимость $\lambda$, зависит от
            геометрических размеров проводника длины $l$ и площади поперечного сечения $S$, а также от удельного
            сопротивления проводника $\rho$:
            
            $$R = \rho \frac{l}{S},$$
            
            где $\rho$ служит характеристикой вещества, из которого изготовлен проводник.
        """))

    def main(self) -> None:
        self.append(NoEscape(r"""
            $I = \frac{U}{R}$ (закон Ома)
        """))

        # мои данные (не измененные)
        # datas = [
        #     Data(number=1, l=0.3, U=0.3, I=0.09),
        #     Data(number=2, l=0.3, U=0.4, I=0.115),
        #     Data(number=3, l=0.3, U=0.5, I=0.145),
        #     Data(number=4, l=0.3, U=0.6, I=0.175),
        #     Data(number=5, l=0.3, U=0.7, I=0.2),
        #     Data(number=1, l=0.4, U=0.4, I=0.09),
        #     Data(number=2, l=0.4, U=0.6, I=0.135),
        #     Data(number=3, l=0.4, U=0.8, I=0.18),
        #     Data(number=4, l=0.4, U=1.0, I=0.220),
        #     Data(number=5, l=0.4, U=1.1, I=0.245),
        #     Data(number=1, l=0.5, U=0.4, I=0.07),
        #     Data(number=2, l=0.5, U=0.6, I=0.105),
        #     Data(number=3, l=0.5, U=0.8, I=0.14),
        #     Data(number=4, l=0.5, U=1.0, I=0.18),
        #     Data(number=5, l=0.5, U=1.2, I=0.215)
        # ]

        # мои данные (измененные)
        datas = [
            Data(number=1, l=0.3, U=0.4, I=0.115),
            Data(number=2, l=0.3, U=0.5, I=0.145),
            Data(number=3, l=0.3, U=0.6, I=0.175),
            Data(number=4, l=0.3, U=0.7, I=0.2),
            Data(number=5, l=0.3, U=0.8, I=0.225),
            Data(number=1, l=0.4, U=0.4, I=0.09),
            Data(number=2, l=0.4, U=0.5, I=0.115),
            Data(number=3, l=0.4, U=0.6, I=0.135),
            Data(number=4, l=0.4, U=0.7, I=0.16),
            Data(number=5, l=0.4, U=0.8, I=0.18),
            Data(number=1, l=0.5, U=0.4, I=0.07),
            Data(number=2, l=0.5, U=0.5, I=0.085),
            Data(number=3, l=0.5, U=0.6, I=0.105),
            Data(number=4, l=0.5, U=0.7, I=0.12),
            Data(number=5, l=0.5, U=0.8, I=0.14)
        ]

        # чужие данные
        # datas = [
        #     Data(number=1, l=0.3, U=0.6, I=0.103),
        #     Data(number=2, l=0.3, U=0.7, I=0.119),
        #     Data(number=3, l=0.3, U=0.8, I=0.136),
        #     Data(number=4, l=0.3, U=0.9, I=0.152),
        #     Data(number=5, l=0.3, U=1.0, I=0.166),
        #     Data(number=1, l=0.4, U=0.6, I=0.081),
        #     Data(number=2, l=0.4, U=0.7, I=0.094),
        #     Data(number=3, l=0.4, U=0.8, I=0.106),
        #     Data(number=4, l=0.4, U=0.9, I=0.119),
        #     Data(number=5, l=0.4, U=1.0, I=0.132),
        #     Data(number=1, l=0.5, U=0.6, I=0.066),
        #     Data(number=2, l=0.5, U=0.7, I=0.075),
        #     Data(number=3, l=0.5, U=0.8, I=0.087),
        #     Data(number=4, l=0.5, U=0.9, I=0.098),
        #     Data(number=5, l=0.5, U=1.0, I=0.108)
        # ]

        fraction = 4
        experiments = 5

        lambda_average = {}
        u_2_sum = {}
        iu_sum = {}

        for data in datas:
            data.lambda_ = data.I / data.U
            data.R = 1 / data.lambda_
            data.R_ = data.U / data.I
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

            self.append(NoEscape(r"""
                $\lambda_{l,i} = \frac{I_{l,i}}{U_{l,i}}$, где $l$ -- длина проводника \\
                
                $\Delta \lambda_{i} = | \frac{\sum^{%s}_{j = 1} \lambda_{l,j}}{%s} - \lambda_{l,i} |$,
                    где $l$ -- длина проводника \\
                
                $R_{l,i} = \frac{1}{\lambda_{l,i}}$, где $l$ -- длина проводника \\
            """ % (experiments, experiments)))

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

            # lambda
            self.append(NoEscape(r"""
                $\lambda_{%s,%s} = \frac{I_{%s,%s}}{U_{%s,%s}} = \frac{%s}{%s} = %s~\textup{См}$ \\
            """ % (datas[0].l,
                   datas[0].number,
                   datas[0].l,
                   datas[0].number,
                   datas[0].l,
                   datas[0].number,
                   datas[0].I,
                   datas[0].U,
                   round(datas[0].lambda_, fraction))))
            # delta lambda
            self.append(NoEscape(r"""
                $\Delta \lambda_{%s,%s} = | \frac{\sum^{%s}_{j = 1} \lambda_{%s,j}}{%s} - \lambda_{%s,i} | =
                    | %s - %s | = %s~\textup{См}$ \\
            """ % (datas[0].l,
                   datas[0].number,
                   experiments,
                   datas[0].l,
                   experiments,
                   datas[0].l,
                   round(lambda_average[datas[0].l], fraction),
                   round(datas[0].lambda_, fraction),
                   round(datas[0].delta_lambda, fraction))))
            # R
            self.append(NoEscape(r"""
                $R_{%s,%s} = \frac{1}{\lambda_{%s,%s}} = \frac{1}{%s} = %s~\textup{В}$ \\
            """ % (datas[0].l,
                   datas[0].number,
                   datas[0].l,
                   datas[0].number,
                   round(datas[0].lambda_, fraction),
                   round(datas[0].R, fraction))))

        for data in datas:
            data.delta_lambda = abs(lambda_average[data.l] - data.lambda_)

        lambda_sum = {}
        delta_lambda_sum = {}
        tau = 2.77

        for data in datas:
            if data.l not in lambda_sum:
                lambda_sum[data.l] = iu_sum[data.l] / u_2_sum[data.l]
                delta_lambda_sum[data.l] = tau * math.sqrt(
                    (
                        sum([d.U ** 2 for d in filter(lambda d: d.l == data.l, datas)]) *
                        sum([d.I ** 2 for d in filter(lambda d: d.l == data.l, datas)]) -
                        iu_sum[data.l] ** 2
                    ) / ((experiments - 1) * (sum([d.U ** 2 for d in filter(lambda d: d.l == data.l, datas)]) ** 2))
                )

        with self.create(Subsection(NoEscape(r'Зависимость силы тока $I$ от напряжения $U$ '
                                             r'(метод наименьших квадратов)'))):
            self.append(NoEscape(r"""
                $\lambda_l = \frac{\sum^{%s}_{i = 1} U_{l,i} I_{l,i}}{\sum^{%s}_{i = 1} U^2_{l,i}}$,
                    где $l$ -- длина проводника
                
                $\Delta \lambda_l = \tau_{%s, 0.95}
                    \sqrt{
                        \frac{\sum_{i = 1}^{%s} U^2_{l,i} \cdot \sum_{i = 1}^{%s} I^2_{l,i} -
                            (\sum^{%s}_{i = 1} U_{l,i} I_{l,i})^2}
                        {%s \cdot (\sum_{i = 1}^{%s} U^2_{l,i})^2}
                    }$, где $l$ -- длина проводника
                    
                $R_{l,i} = \frac{U_{l,i}}{I_{l,i}}$, где $l$ -- длина проводника
            """ % (experiments, experiments, experiments, experiments, experiments, experiments, experiments - 1,
                   experiments)))

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
                                   MultiRow(experiments, data=NoEscape(r"$%s$" % round(lambda_sum[data.l], fraction)))
                                   if data.number == 1 else "",
                                   MultiRow(experiments, data=NoEscape(r"$%s$" % round(delta_lambda_sum[data.l],
                                                                                       fraction)))
                                   if data.number == 1 else "",
                                   r"$%s$" % round(data.R_, fraction)],
                                  escape=False)
                    self.append(NoEscape(r"\cline{1-6} \cline{9-9}"))

                    if data.number == experiments:
                        self.append(NoEscape(r"\cline{7-8}"))
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
            # lambda
            self.append(NoEscape(r"""
                $\lambda_{%s} = \frac{\sum^{%s}_{i = 1} U_{%s,i} I_{%s,i}}{\sum^{%s}_{i = 1} U^2_{%s,i}} =
                    \frac{%s}{%s} = %s~\textup{См}$ \\
            """ % (datas[0].l,
                   experiments,
                   datas[0].l,
                   datas[0].l,
                   experiments,
                   datas[0].l,
                   round(iu_sum[datas[0].l], fraction),
                   round(u_2_sum[datas[0].l], fraction),
                   round(lambda_sum[datas[0].l], fraction))))
            # delta lambda
            self.append(NoEscape(r"""
                $\Delta \lambda_{%s} = \tau_{%s, 0.95} \sqrt{
                    \frac{\sum_{i = 1}^{%s} U^2_{%s,i} \cdot \sum_{i = 1}^{%s} I^2_{%s,i} -
                        (\sum^{%s}_{i = 1} U_{%s,i} I_{%s,i})^2}
                    {%s \cdot (\sum_{i = 1}^{%s} U^2_{%s,i})^2}
                } = %s \sqrt{\frac{%s \cdot %s - %s}{%s \cdot %s}} = %s~\textup{См}$ \\
            """ % (datas[0].l,
                   experiments,
                   experiments,
                   datas[0].l,
                   experiments,
                   datas[0].l,
                   experiments,
                   datas[0].l,
                   datas[0].l,
                   experiments - 1,
                   experiments,
                   datas[0].l,
                   tau,
                   round(sum([d.U ** 2 for d in filter(lambda d: d.l == datas[0].l, datas)]), fraction),
                   round(sum([d.I ** 2 for d in filter(lambda d: d.l == datas[0].l, datas)]), fraction),
                   round(iu_sum[datas[0].l] ** 2, fraction),
                   experiments - 1,
                   round(sum([d.U ** 2 for d in filter(lambda d: d.l == datas[0].l, datas)]) ** 2, fraction),
                   round(delta_lambda_sum[datas[0].l], fraction))))
            # R
            self.append(NoEscape(r"""
                $R_{%s,%s} = \frac{U_{%s,%s}}{I_{%s,%s}} = \frac{%s}{%s} = %s~\textup{В}$ \\ [1cm]
            """ % (datas[0].l,
                   datas[0].number,
                   datas[0].l,
                   datas[0].number,
                   datas[0].l,
                   datas[0].number,
                   datas[0].U,
                   datas[0].I,
                   round(datas[0].R_, fraction)
                   )))

        self.append(NoEscape(r"""
            $$R_{l} = R_{l,\textup{ср}} \pm \Delta R_{l}$$
        """))

        for data in datas:
            if data.number == experiments:
                experiment = list(filter(lambda d: d.l == data.l, datas))
                r_average = sum([d.R for d in experiment]) / len(experiment)
                self.append(NoEscape(r"""
                    $R_{%s,\textup{ср}} = \frac{\sum^{%s}_{i = 1} R_{%s,i}}{%s} = %s~\textup{В}$ \\
                """ % (data.l, experiments, data.l, experiments, round(r_average, fraction))))

                r_2_sum = sum([(r_average - d.R) ** 2 for d in experiment])
                delta_r = tau * math.sqrt(r_2_sum / (len(experiment) * (len(experiment) - 1)))
                self.append(NoEscape(r"""
                    $\Delta R_{%s} =
                        \tau_{%s,0.95} \sqrt{\frac{\sum_{i = 1}^{%s} (\Delta R_{%s,i})^2}{%s(%s - 1)}} = 
                        %s \sqrt{\frac{%s}{%s}} = %s = %s \cdot 10^{-2}~\textup{В}$ \\
                """ % (data.l, experiments, experiments, data.l, experiments, experiments, tau,
                       round(r_2_sum, fraction),
                       len(experiment) * (len(experiment) - 1),
                       round(delta_r, fraction),
                       round(delta_r * 10 ** 2, fraction - 2))))

                self.append(NoEscape(r"""
                    $R_{%s} = R_{%s,\textup{ср}} \pm \Delta R_{%s} = %s \pm %s \cdot 10^{-2}~\textup{В}$ \\ [0.5cm]
                """ % (data.l, data.l, data.l, round(r_average, fraction), round(delta_r * 10 ** 2, fraction - 2))))


def main():
    LaboratoryWork(
        number=3.2,
        name='Изучение вольтамперной характеристики проводников методом наименьших квадратов',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.2')


if __name__ == '__main__':
    main()
