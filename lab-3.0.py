from models import LaboratoryWork


class LaboratoryWork1(LaboratoryWork):
    def purpose(self) -> None:
        self.append('Изучение законов электростатики и электростатического поля.')

    def brief_theory(self) -> None:
        pass

    def experiments(self) -> None:
        pass


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
