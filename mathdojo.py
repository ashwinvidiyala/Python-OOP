class MathDojo(object):
    def __init__(self, number = 0):
        self.number = number

    def add(self, num1, *nums):
        tuple_number = 0
        array_number = 0
        if type(num1) == list:
            for z in num1:
                array_number += z
        else:
            array_number = num1
        for x in nums:
            if type(x) == list:
                for y in x:
                    tuple_number = tuple_number +  int(y)
            else:
                tuple_number = tuple_number +  int(x)
        self.number = self.number + array_number + tuple_number
        return self

    def subtract(self, num1, *nums):
        tuple_number = 0
        array_number = 0
        if type(num1) == list:
            for z in num1:
                array_number += z
        else:
            array_number = num1
        for x in nums:
            if type(x) == list:
                for y in x:
                    tuple_number = tuple_number +  int(y)
            else:
                tuple_number = tuple_number +  int(x)
        self.number = self.number - array_number - tuple_number
        return self

    def result(self):
        print "The result is:", self.number

md = MathDojo()
md.add([1,2], [5, 6, 7], [7,8,9]).subtract([1,1], [1,1], 1, [1,1,1])
print md.number
