######


import threading

def func():
    for x in range(100):
        print("salom")
def func2():
    for x in range(100):
        print("javohir")

func()
func2()

foo1 = threading.Thread(target=func)
foo2 = threading.Thread(target=func2)


foo1.start()
foo2.start()