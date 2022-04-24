# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.

a = int(input('Введите сторону а '))
b = int(input('Введите сторону b '))
c = int(input('Введите сторону c '))

if a + b > c and a + c > b and b + c > a:
    if (a==b or a==c or b==c):
        if a==b and b==c:
            print('Это равносторонний треугольник')
        else:
            print('Это равнобедренный треугольник')
    else:
        print('Это треугольник')
else:
    print('Это не треугольник')