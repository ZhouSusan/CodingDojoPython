class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, number, *nums):
        self.number = number
        add_sum = 0
        nums_list = [*nums]
        for idx in range(len(nums_list)):
            add_sum += nums_list[idx]
        self.result += self.number + add_sum
        return self

    def subtract(self, number, *nums):
        self.number = number
        nums_list = [*nums] 
        subtract_total = 0
        for idx in range(len(nums_list)):
           subtract_total += nums_list[idx]
        self.number = self.number + subtract_total
        self.result -= self.number
        return self

md = MathDojo()
num = md.add(2).add(2, 5, 1).subtract(3,2).result
print(num)    #5

md = MathDojo()
num_two = md.add(10, 2).add(1, 2, 4).subtract(1).result
print(num_two) #18

md = MathDojo()
num_two = md.add(12, 10, 18).add(1, 2, 3, 4).subtract(10, 12, 3).result
print(num_two) #25

md = MathDojo()
num_two = md.add(12, 10, 18).add(1, 2, 3, 4).subtract(10, 12, 3, 20, 7).result
print(num_two) #-2