#DEF

# def lessons():
#     return 'Hello world'



# print(lessons())

# def summ(x,y):
#     return x+y
# print(summ(x=2,y=2))


# def summ(x:int,y:int):
#     return x+y
# a=int(input("введите первое число"))
# b=int(input("Введите второе число"))
# print(summ(a,b))


# def name(a:int ,b=2,c=None)-> None:
#     return
# print(name(10,10,10))

# def name(a,b=2,c=None):
#     """
#     Наша функция вернет Привет мир
#     """
    
def calculator(x,y,z):
    import os
    with open("user_cal.txt","a") as file:
        
        if  z=="+":
            os.system('clear')
            file.write(f'Пользователь сделал запрос: {x}{z}{y}={x+y}\n')
            return f'{x}{z}{y}={x+y}'
        elif z=='-':
            os.system('clear')
            file.write(f'Пользователь сделал запрос: {x}{z}{y}={x-y}\n')
            return f"{x}{z}{y}={x-y}"
        elif z=='*':
            os.system('clear')
            file.write(f'Пользователь сделал запрос: {x}{z}{y}={x*y}\n')
            return f"{x}{z}{y}={x*y}"
        elif z=='/':
            if y==0:
                os.system('clear')
                return 'Nelzya'
            file.write(f'Пользователь сделал запрос: {x}{z}{y}={x/y}\n')
            return f'{x}{z}{y}={x/y}'
        elif z=='**':
            os.system('clear')
            file.write(f'Пользователь сделал запрос: {x}{z}{y}={x**y}\n')
            return f"{x}{z}{y}:{x**y}"
        
        else:
            os.system('clear ')
            file.write(f'Пользователь сделал  плохой запрос: {x}{z}{y}=&&&\n')
            return 'Такой операции нет'
while True:
    num1=int(input("Число 1: "))
    num2=int(input("Число 2: "))
    num3=input("Операция: ")
    print(calculator(num1,num2,num3))