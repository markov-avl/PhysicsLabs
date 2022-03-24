import math
from pylatex import NoEscape, Subsection

from models import LaboratoryWork


class LaboratoryWork1(LaboratoryWork):
    def purpose(self) -> None:
        self.append(NoEscape(r"""
            Изучение законов электростатики и электростатического поля.
        """))

    def brief_theory(self) -> None:
        self.append(NoEscape(r"""
            Если сила $F$ действует на точечный заряд $q$ в поле другого заряда, то напряжённость электрического
            поля $E$ заряженного тела определяется как:
            $$\vec{E} = \frac{\vec{F}}{q},$$
            
            где $F$ -- сила Кулона, которая прямо пропорциональна произведению отдельных зарядов и обратно
            пропорциональна квадрату расстояния между ними.
            
            $$\vec{F} = k \frac{q_1 q_2}{\varepsilon r^2},$$
            
            где $q_1$ и $q_2$ -- два заряда, $r$ -- расстояние, $\varepsilon$ -- диэлектрическая проницаемость среды
            $(\varepsilon_\textup{воздуха} \approx \varepsilon_\textup{вакуума} = 1)$, $k$ -- электрическая постоянная
            равная $9 \cdot 10^9 ~ \frac{\textup{Н} \cdot \textup{м}^2}{\textup{Кл}^2}$ в системе СИ.
            
            $$k = \frac{1}{4 \pi \varepsilon_0},$$
            
            где $\varepsilon_0$ -- электрическая постоянная равная
            $8,85 \cdot 10^{-12} ~ \frac{\textup{Кл}^2}{\textup{Н} \cdot \textup{м}^2}$.
            
            Потенциал поля, создаваемого точечным зарядом $q$ в вакууме, относительно бесконечности, определяется
            выражением:
            $$\varphi = \frac{q}{4 \pi \varepsilon_0 r},$$
            
            где $\varepsilon_0$ -- диэлектрическая проницаемость вакуума, $r$ -- расстояние от источника поля заряда
            $q$ до точки, в которой определяется потенциал поля.
            
            Величина напряжённости на участке электрического поля может быть рассчитана из разности потенциалов как:
            $$E_s = -\frac{\partial \varphi}{\partial s} \cong -\frac{\Delta \varphi}{\Delta s},$$
            
            где $\Delta \varphi$ -- разность потенциалов двух соседних эквипотенциальных линий, а $\Delta s$ --
            расстояние между ними, измеренное по силовой линии.
        """))

    def main(self) -> None:
        with self.create(Subsection(NoEscape(r'График зависимости потенциала $\varphi$ от координаты $x$ в опыте с '
                                             r'2-мя плоскими электродами'))):
            # формулы
            self.append(NoEscape(r"""
                $$\varphi = const$$
                $$\vec{E} = -grad$$
                $$grad = \frac{\partial}{\partial x}\vec{i} + \frac{\partial}{\partial y}\vec{j} +
                \frac{\partial}{\partial z}\vec{k}$$
                $$|\vec{E}| = |\frac{\Delta \varphi}{\Delta s}|$$
            """))

            fraction = 3

            # вычисление E_i
            e_measurement = r'\frac{\textup{В}}{\textup{м}}'
            x = list(map(lambda i: round(i / 100, fraction), [0, 2.8, 7.3, 12.3, 16.65, 21.75, 25.45]))
            phi = [11.5, 10, 8, 6, 4, 2, 0]
            e = list()
            for x_i in range(1, len(x)):
                e.append(round((phi[x_i - 1] - phi[x_i]) / (x[x_i] - x[x_i - 1]), fraction))
                self.append(NoEscape(r"""
                    $E_%s = \frac{%s - %s}{%s - %s} = %s ~ %s$ \\
                """ % (x_i, phi[x_i - 1], phi[x_i], x[x_i], x[x_i - 1], e[-1], e_measurement)))

            # вычисление Eср и tan(phi)
            e_average = round(sum(e) / len(e), fraction)
            self.append(NoEscape(r"""
                $E_\textup{ср} = %s ~ %s \\$
            """ % (e_average, e_measurement)))

            # вычисление delta(E_i)
            delta_e_i = list()
            delta_e_i_2 = list()
            for i, e_i in enumerate(e):
                delta_e_i_2.append(round((e_average - e_i) ** 2, fraction))
                delta_e_i.append(round(math.sqrt(delta_e_i_2[-1]), fraction))
                self.append(NoEscape(r"""
                    $(\Delta E_{%s})^2 = (%s - %s)^2 = %s ~ %s 
                    ~ \Rightarrow ~
                    \Delta E_{%s} = %s ~ %s \\$
                """ % (i + 1, e_average, e_i, delta_e_i_2[-1], e_measurement, i + 1, delta_e_i[-1], e_measurement)))

            # tan(phi)


def main():
    LaboratoryWork1(
        number=3.0,
        name='Изучение электростатического поля',
        group='Б9119-02.03.03техпро',
        course=3,
        student='Марков А.В.'
    ).compile('result/lab-3.0')


if __name__ == '__main__':
    main()
