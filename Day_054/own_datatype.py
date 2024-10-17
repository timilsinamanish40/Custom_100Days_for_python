class Fraction:
    def __init__(self, x, y ):
        self.num = x
        self.den = y

    def __str__(self):
        # return str(self.num) + "/" + str(self.den)
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        new_num =self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        
        return "{}/{}".format(new_num,new_den)
        # return Fraction(new_num, new_den)


    def __sub__(self, other):
        new_num =self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        
        return "{}/{}".format(new_num,new_den)
        # return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num =self.num * other.num 
        new_den = self.den * other.den
        
        return "{}/{}".format(new_num,new_den)
        # return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num =self.num * other.den 
        new_den = other.num * self.den
        
        return "{}/{}".format(new_num,new_den)
        # return Fraction(new_num, new_den)


    def convert_to_decimal(self):
        return self.num / self.den


fr1 = Fraction(1,2)
fr2 = Fraction(2,3)

print(fr1)
print(fr2)

print("The addition is : " ,fr1 + fr2 )
print("The subtraction is : " ,fr1 - fr2 )
print("The multiplication is : " ,fr1 * fr2 )
print("The division is : " ,fr1 / fr2 )
print(fr1.convert_to_decimal())