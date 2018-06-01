import threading
import time

def fun_timer():
    global timer,hours
    hours+=1
    if hours >23:
        hours=0
    
    timer = threading.Timer(5.0, fun_timer)#5s执行一次fun_timer
    timer.start()


def main():
    global hours

    hours = 0
    fun_timer()  #启动定时器
    while True:
        print()
        command = input("Command:")
        if command == "print":
            print("Now is %-2d"%hours)
        elif command == "quit":
            print("Bye.....")
            timer.cancel()
            break


   

if __name__ =="__main__":
    main()

##在使用Python定时器时需要注意如下4个方面：
##（1）定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名，第一个参数表示多长时间后调用后面第二个参数指明的函数。第二个参数注意是函数对象，进行参数传递，用函数名(如fun_timer)表示该对象，不能写成函数执行语句fun_timer()，不然会报错。用type查看下，可以看出两者的区别。
##（2）必须在定时器执行函数内部重复构造定时器，因为定时器构造后只执行1次，必须循环调用。
##（3）定时器间隔单位是秒，可以是浮点数，如5.5，0.02等，在执行函数fun_timer内部和外部中给的值可以不同。
##（4）可以使用cancel停止定时器的工作
