import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)

pwm2 = machine.PWM(pin)
pwm2.freq(500)
pwm2.duty(1023)

while True:
    for i in range(1023, 0, -10):
        #print(i)
        time.sleep_ms(10)
        pwm2.duty(i)
    pwm2.duty(0)
    for i in range(0, 1024, 10):
        #print(i)
        time.sleep_ms(10)
        pwm2.duty(i)
    pwm2.duty(1024)
    time.sleep_ms(500)