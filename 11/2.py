class Time:
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
        self.fix()

    def show(self):
        print(self.h, ":", self.m, ":", self.s)

    def sum(self, other):
        s_new = self.s + other.s
        m_new = self.m + other.m
        h_new = self.h + other.h
        result = Time(h_new, m_new, s_new)
        return result
    
    def sub(self , other):
        s_new = self.s - other.s
        m_new = self.m - other.m
        h_new = self.h - other.h
        result = Time(h_new, m_new, s_new)
        return result

    def time_to_sec(self):
        result = self.h*3600 + self.m*60 + self.s
        return result

    def sec_to_time(seconds):
        hour = seconds // 3600
        seconds = seconds - (hour * 3600)
        minute = seconds // 60
        seconds = seconds - (minute * 60)
        second = seconds
        time = Time(hour, minute, second)
        return time

    def GMT_to_IRT(self):
        teh_h = self.h + 4
        teh_m = self.m + 30
        teh_s = self.s
        result = Time(teh_h, teh_m, teh_s)
        return result

    def fix(self):
        if self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s < 0:
            self.s += 60
            self.m -= 1

        if self.m < 0:
            self.m += 60
            self.h -= 1


while True:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Enter + to add two times ")
    print("Enter - to subtract two times")
    print("Enter 1 to convert time to seconds ")
    print("Enter 2 to convert seconds to time ")
    print("Enter 3 to convert Greenwich time to Iran Time ")
    print("Exit")

    operator = input("Choose your operator: ")


    
    if operator == "exit":
        break
    
    elif operator == "1":
        h = int(input("enter hour: "))
        m = int(input("enter minute: "))
        s = int(input("enter second: "))

        t1 = Time(h, m, s)
        t1.show()

        second = t1.time_to_sec()
        print("second: ", second)
        

    elif operator == "2":
        second = int(input("enter second: "))
        time = Time.sec_to_time(second)
        time.show()

    elif operator == "3":
        h = int(input("enter hour: "))
        m = int(input("enter minute: "))
        s = int(input("enter second: "))

        t1 = Time(h, m, s)
        t1.show()

        time = t1.GMT_to_IRT()
        time.show()
        

    elif operator == "+":
        h1 = int(input("enter hour1: "))
        m1 = int(input("enter minute1: "))
        s1 = int(input("enter second1: "))

        h2 = int(input("enter hour2: "))
        m2 = int(input("enter minute2: "))
        s2 = int(input("enter second2: "))

        t1 = Time(h1, m1, s1)
        t1.show()

        t2 = Time(h2, m2, s2)
        t2.show()
        t3 = t1.sum(t2)
        t3.show()

    elif operator == "-":
        h1 = input("enter hour: ")
        m1 = input("enter minute: ")
        s1 = input("enter second: ")

        h2 = input("enter hour: ")
        m2 = input("enter minute: ")
        s2 = input("enter second: ")

        t1 = Time(h1, m1, s1)
        t1.show()

        t2 = Time(h2, m2, s2)
        t2.show()
        t3 = t1.sum(t2)
        t3.show()

    else:
        print('try again!')