# import threading
# def fun():
#     print("Hey you called fun")

# def happy():
#     print('running after 5 sec')

# def sing():
#     print("start singing after 10 sec")

# func1=threading.Timer(2, fun)
# func2=threading.Timer(5, happy)
# func3=threading.Timer(3, sing)

# func1.start()
# func2.start()
# func3.start()

# print("End of line")

# print(pow(4, 2))

class Parrot:
    def __init__(self) -> None:
        self._voltage = 10000

    
    @property
    def voltage(self):
        new=[]
        a=[1,1,2,5,8,9,8,78,95,49]
        a.sort()
        lena, lenb = len(a)/2
        for i in range(lena):
            print(a[i])
            for j in range(lena[-1]+1):
                print(a[j])

        return self._voltage
        
parrot=Parrot
print(parrot().voltage)

