import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3 ,4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    N = 0
    
    for i in range(7, -1, -1):
        N += 2**i
        dec_i = binary(N)
        GPIO.output(dac, dec_i)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 1:
            N -= 2**i
    return N
try:
    nap = 0
    result = []
    t_st = time.time()
    k = 0

    print("\n")
    print('Зарядка конденсатора')
    print("\n")
    # Зарядка конденсатора
    while nap < 210:
        k += 1
        nap = adc()
        result.append((nap*3.3) / 255)
        b_nap = binary(nap)
        GPIO.output(leds, b_nap)
        print((nap*3.3) / 255)

    GPIO.output(troyka, 0)
    
    print("\n")
    print('Разрядка конденсатора')
    print("\n")
    # Разрядка конденсатора
    while nap > 256 * 0.75:
        k += 1
        nap = adc()
        result.append((nap*3.3) / 255)
        GPIO.output(leds, b_nap)
        print((nap*3.3) / 255)

    t_f = time.time()
    t = t_f - t_st
    t_1 = t / k
    nu = 1 / t_1
    kw = 3.3 / 255
    # Запись данных в файл
    print('Запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in result:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(nu) + '\n' + 'kw')
    # Построение графиков
    print('Построение графиков')
    y = [i * (3.3 / 256) for i  in result]
    x = [i * t_1 for i in range(len(result))]
    plt.plot(x, y)
    plt.xlabel("Время")
    plt.ylabel("Напряжение")
    # Вывод экспериментальных данных'
    print('Вывод экспериментальных данных')
    print('\n')
    print('Продолжительность эксперимента ', t)
    print('Период измерения ', t_1)
    print('Средняя частота дискритизации', nu)
    print('Шаг квантования АЦП', kw)
    plt.show()


finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
