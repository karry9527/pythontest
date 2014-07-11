__author__ = 'User'

class node:
    def __init__(self):
        node.x = 1
        node.y = 3

    def get_value(self, p, variable):
        if variable == 1:
            return 1
        elif variable == 2:
            return 3



class ICE_Learning:
    def __init__(self):
        self.point_num = 1
        #self.examples_index = []
        #self.counter_examples_index = []
        #self.implications_index = []
        self.examples = {}
        self.counter_examples = {}
        self.implications = {}

    def set_point(self, ice, var):      # ice: this point belong to I or C or E     var: variables' value
        if ice == "i":
            self.set_implications(var)
        elif ice == "c":
            self.set_counter_examples(var)
        elif ice == "e":
            self.set_examples(var)

    def set_examples(self, point):
        self.examples[self.point_num] = point
        self.point_num += 1
        #print self.examples

    def set_counter_examples(self, point):
        self.counter_examples[self.point_num] = point
        self.point_num += 1
        #print self.counter_examples

    def set_implications(self, point):              # need change
        self.implications[self.point_num] = point
        self.point_num += 1
        #print self.implications

    def get_examples(self):
        return self.examples

    def get_counter_examples(self):
        return self.counter_examples

    def get_implications(self):
        return self.implications

    def get_value(self, point_num, varible_num, vars):
        v = vars[varible_num - 1]
        #print v
        if point_num in self.get_examples().keys():
            s = self.examples[point_num]
            return s[v]
        elif point_num in self.get_counter_examples().keys():
            s = self.counter_examples[point_num]
            return s[v]
        elif point_num in self.get_implications().keys():
            s = self.implications[point_num]
            return s[v]

if __name__ == '__main__':
    vars = ["x", "y"]
    s = {"x":1, "y":2}
    learn = ICE_Learning()
    learn.set_point("e", s)
    s = {"x":2, "y":2}
    learn.set_point("i", s)
    s = {"x":3, "y":2}
    learn.set_point("e", s)
    s = {"x":4, "y":2}
    learn.set_point("e", s)
    print learn.get_examples()
    print learn.get_counter_examples()
    print learn.get_implications()
    #for num in learn.get_examples().keys():
    #    print num
    print learn.get_value(1, 2, vars)
    print learn.get_value(5, 1, vars)