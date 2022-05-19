# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


Company = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

company_count = int(input('Введите количество компаний для анализа: '))
companies = [0 for _ in range(company_count)]
profit_sum = 0

for i in range(company_count):
    name = input(f'Введите название {i+1}-й компании: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    year = 0
    for quarter in quarters:
        year += quarter

    profit_sum += year
    companies[i] = Company(name, *quarters, year)
    # print(companies[i])

if company_count == 1:
    print(f'На анализ передана 1 компания: {companies[0].name}. Eе годовая прибыль: {companies[0].year}')

else:
    profit_average = profit_sum / company_count

    less = []
    more = []

    for i in range(company_count):

        if companies[i].year < profit_average:
            less.append(companies[i])

        elif companies[i].year > profit_average:
            more.append(companies[i])

    print(f'\nСредняя годовая прибыль по компаниям: {profit_average: .2f}')

    print(f'Компании, чья прибыль меньше среднего {profit_average: .2f}:')
    for comp in less:
        print(f'Компания "{comp.name}" с прибылью {comp.year: .2f}')

    print(f'\nКомпании, чья прибыль больше среднего {profit_average: .2f}:')
    for comp in more:
        print(f'Компания "{comp.name}" с прибылью {comp.year: .2f}')