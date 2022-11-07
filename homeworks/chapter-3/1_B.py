class Ternary:

    def __init__(self, num: str):
        self.num = num

    def __int__(self):
        return int(self.num, base=3)

    def __add__(self, other):
        res = ''
        this_copy = self.num[::-1]
        other_copy = other.num[::-1]
        while len(this_copy) != len(other_copy):
            if len(this_copy) > len(other_copy):
                other_copy += '0'
            else:
                this_copy += '0'
        prev = 0
        for i in range(len(this_copy)):
            res += str((int(this_copy[i]) + int(other_copy[i]) + prev) % 3)
            if (int(this_copy[i]) + int(other_copy[i]) + prev) > 2:
                prev = 1
            else:
                prev = 0
        if prev:
            res += '1'
        return res[::-1]

    def __sub__(self, other):
        res = ''
        this_copy = self.num[::-1]
        other_copy = other.num[::-1]
        while len(this_copy) != len(other_copy):
            if len(this_copy) > len(other_copy):
                other_copy += '0'
            else:
                this_copy += '0'
        prev = 0
        if int(self) < int(other):
            return '-' + (other - self)
        for i in range(len(this_copy)):
            if int(this_copy[i]) - int(other_copy[i]) - prev < 0:
                res += str((int(this_copy[i]) - int(other_copy[i]) - prev + 3) % 3)
                prev = 1
            else:
                res += str((int(this_copy[i]) - int(other_copy[i]) - prev) % 3)
                prev = 0
        ind = -1
        if prev:
            res += '1'
        res = res[::-1]
        for i in range(len(res)-1):
            if res[i] == '0':
                ind = i
            else:
                break
        if ind > -1:
            res = res[ind+1:]
        return str(res)

    def __mul__(self, other):
        s = 0
        for i in range(int(other)):
            s += int(self)
        r = ''
        while s > 0:
            r += str(s%3)
            s //= 3
        return r[::-1]

    def __floordiv__(self, other):
        s = Ternary(self.num)
        c = 0
        while int(s - other, base=3) >= 0:
            s -= other
            s = Ternary(s)
            c += 1
        r = ''
        while c > 0:
            r += str(c % 3)
            c //= 3
        return r[::-1]

    def __str__(self):
        return str(self.num)


s = input().split()
a = Ternary(s[0])
b = Ternary(s[1])
print(a + b)
print(a - b)
print(a * b)
print(a // b)
