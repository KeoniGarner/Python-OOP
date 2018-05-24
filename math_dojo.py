class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        for arg in list(args):
            if isinstance(arg, list) or isinstance(arg,tuple):
                for number in arg :
                    self.result += number
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        for arg in list(args):
            if isinstance(arg, list) or isinstance(arg,tuple):
                temp_sum = 0
                for number in arg :
                    temp_sum += number
                self.result -= temp_sum
            else:
                self.result -= arg
        return self

print (MathDojo().add(2).add(2,5).subtract(3,2).result)
print (MathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result)
print (MathDojo().add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], (1.1,2.3)).result)