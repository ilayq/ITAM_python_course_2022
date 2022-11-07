class Binary:

    def __init__(self, num: int):
        self.num = bin(num)[2:]

    def __int__(self):
        return int(self.num, base=2)

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
            res += str((int(this_copy[i]) + int(other_copy[i]) + prev) % 2)
            if (int(this_copy[i]) + int(other_copy[i]) + prev) > 1:
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
                prev = 1
                res += '1'
            else:
                res += str(int(this_copy[i]) - int(other_copy[i]) - prev)
                prev = 0
        ind = 0
        if prev:
            res += '1'
        res = res[::-1]
        for i in range(len(res)):
            if res[i] == '0':
                ind = i
            else:
                break
        res = res[ind:]
        return res

    def __mul__(self, other):
        s = 0
        for i in range(int(other)):
            s += int(self.num, base=2)
        return bin(s)[2:]

    def __floordiv__(self, other):
        s = Binary(int(self.num, base=2))
        c = 0

        while int(s - other, base=2) >= 0:
            s -= other
            s = Binary(int(s, base=2))
            c += 1
        return bin(c)[2:]

    def __str__(self):
        return str(self.num)


s = input().split()
a = Binary(int(s[0], base=2))
b = Binary(int(s[1], base=2))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
