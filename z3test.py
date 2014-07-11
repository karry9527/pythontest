__author__ = 'kkk'
from z3 import *
from formula import *

class z3test:
    def __init__(self):
        self.i = 2
        self.j = 2
        self.point_num = 2
        self.variable_num = 2
        self.bool = "b"
        self.r = "r"
        self.c = "c"
        self.s = "s"
        self.v = "v"
        self.d = "d"
        self.M = 20
        self.learn = ICE_Learning()
        s = {"x":1, "y":3}
        self.learn.set_point("c", s)
        s = {"x":3, "y":5}
        self.learn.set_point("e", s)
        self.var = ["x", "y"]

    def f1(self):
        temp = None
        for num in self.learn.get_examples().keys():
            if temp == None:
                temp = Bool(self.bool+str(num))
            else:
                temp = And(temp, Bool(self.bool+str(num)))

        return temp

    def f2(self):
        temp = None
        for num in self.learn.get_counter_examples().keys():
            if temp == None:
                temp = Not(Bool(self.bool+str(num)))
            else:
                temp = And(temp, Not(Bool(self.bool+str(num))))
        print temp
        return temp

    #def f3(self):


    def f4(self, i_num, j_num, p_num):
        condition4 = []
        temp_p = None
        for p in range(1, p_num + 1):
            temp_i = None
            for i in range(1, i_num + 1):
                temp_j = None
                for j in range(1, j_num + 1):
                    if temp_j == None:
                        temp_j = Bool(self.bool+str(i)+str(j)+str(p))
                    else:
                        temp_j = And(temp_j, Bool(self.bool+str(i)+str(j)+str(p)))
                if temp_i == None:
                    temp_i = temp_j
                else:
                    temp_i = Or(temp_i, temp_j)
                    #print temp
            if temp_p == None:
                temp_p = Or(
                    And(Bool(self.bool+str(p)), temp_i),
                    And(Not(Bool(self.bool+str(p))), Not(temp_i))
                )
            else:
                temp_p = And(temp_p, Or(
                    And(Bool(self.bool+str(p)), temp_i),
                    And(Not(Bool(self.bool+str(p))), Not(temp_i))
                ))
        condition4.append(simplify(temp_p))
        print condition4
        return condition4

    def f5(self, i_num, j_num, p_num):
        condition5 = []
        temp_p = None
        for p in range(1, p_num + 1):
            temp_i = None
            for i in range(1, i_num + 1):
                temp_j = None
                for j in range(1, j_num + 1):
                    if temp_j == None:
                        temp_j = Or(
                            And(Bool(self.bool+str(i)+str(j)+str(p)),
                                Int(self.r+str(i)+str(j)+"1"+str(p))+Int(self.r+str(i)+str(j)+"2"+str(p)) <= Int(self.c+str(i)+str(j))),
                            And(Not(Bool(self.bool+str(i)+str(j)+str(p))),
                                Int(self.r+str(i)+str(j)+"1"+str(p))+Int(self.r+str(i)+str(j)+"2"+str(p)) > Int(self.c+str(i)+str(j))))
                    else:
                        temp_j = And(temp_j, Or(
                            And(Bool(self.bool+str(i)+str(j)+str(p)),
                                Int(self.r+str(i)+str(j)+"1"+str(p))+Int(self.r+str(i)+str(j)+"2"+str(p)) <= Int(self.c+str(i)+str(j))),
                            And(Not(Bool(self.bool+str(i)+str(j)+str(p))),
                                Int(self.r+str(i)+str(j)+"1"+str(p))+Int(self.r+str(i)+str(j)+"2"+str(p)) > Int(self.c+str(i)+str(j)))))
                if temp_i == None:
                    temp_i = temp_j
                else:
                    temp_i = And(temp_i, temp_j)
                    #print temp
            if temp_p == None:
                temp_p = temp_i
            else:
                temp_p = And(temp_p, temp_i)
        condition5.append(simplify(temp_p))
        #print condition5
        return condition5
    def f6(self, i_num, j_num, M):
        condition6 = []
        temp_i = None
        for i in range(1, i_num + 1):
            temp_j = None
            for j in range(1, j_num + 1):
                if temp_j == None:
                    temp_j = And(str(-M) <= Int(self.c+str(i)+str(j)), Int(self.c+str(i)+str(j)) <= str(M))
                else:
                    temp_j = And(temp_j, And(str(-M) <= Int(self.c+str(i)+str(j)), Int(self.c+str(i)+str(j)) <= str(M)))
                #print temp_j

            if temp_i == None:
                temp_i = temp_j
            else:
                temp_i = And(temp_i, temp_j)
        condition6.append(simplify(temp_i))
        #print condition6
        return condition6
    def f7(self, i_num, j_num, p_num):
        condition7 = []
        temp_p = None
        for p in range(1, p_num + 1):
            temp_i = None
            for i in range(1, i_num + 1):
                temp_j = None
                for j in range(1, j_num + 1):
                    temp_k = None
                    for k in range(1, 3):
                        if temp_k == None:
                            temp_k = And(Or(Not(Int(self.s+str(i)+str(j)+str(k)) == 0), Int(self.r+str(i)+str(j)+str(k)+str(p)) == 0),
                                         Or(Not(Int(self.s+str(i)+str(j)+str(k)) == 1), Int(self.r+str(i)+str(j)+str(k)+str(p)) == Int(self.d+str(i)+str(j)+str(k)+str(p))),
                                         Or(Not(Int(self.s+str(i)+str(j)+str(k)) == -1), Int(self.r+str(i)+str(j)+str(k)+str(p)) == -Int(self.d+str(i)+str(j)+str(k)+str(p)))
                                         #,Int(self.d+str(i)+str(j)+str(k)+str(p)) == 2
                            )
                        else:
                            temp_k = And(temp_k, And(Or(Not(Int(self.s+str(i)+str(j)+str(k)) == 0), Int(self.r+str(i)+str(j)+str(k)+str(p)) == 0),
                                         Or(Not(Int(self.s+str(i)+str(j)+str(k)) == 1), Int(self.r+str(i)+str(j)+str(k)+str(p)) == Int(self.d+str(i)+str(j)+str(k)+str(p))),
                                         Or(Not(Int(self.s+str(i)+str(j)+str(k)) == -1), Int(self.r+str(i)+str(j)+str(k)+str(p)) == -Int(self.d+str(i)+str(j)+str(k)+str(p))))
                                         #,Int(self.d+str(i)+str(j)+str(k)+str(p)) == 2
                            )
                    if temp_j == None:
                        temp_j = temp_k
                    else:
                        temp_j = And(temp_j, temp_k)
                    #print temp_j
                if temp_i == None:
                    temp_i = temp_j
                else:
                    temp_i = And(temp_i, temp_j)
            if temp_p == None:
                temp_p = temp_i
            else:
                temp_p = And(temp_p, temp_i)
                    #print temp
        condition7.append(simplify(temp_p))
        print condition7
        return condition7

    def f8(self, i_num, j_num, p_num, variable_num):
        condition8 = []
        temp_p = None
        for p in range(1, p_num + 1):
            temp_i = None
            for i in range(1, i_num + 1):
                temp_j = None
                for j in range(1, j_num + 1):
                    temp_k = None
                    for k in range(1, 3):
                        temp_l = None
                        for l in range(1, variable_num +1):
                            if temp_l == None:
                                temp_l = Or(Not(Int(self.v+str(i)+str(j)+str(k)) == str(l)),
                                             Int(self.d+str(i)+str(j)+str(k)+str(p)) == self.learn.get_value(p, l, self.var)
                                )
                            else:
                                temp_l = And(temp_l, Or(Not(Int(self.v+str(i)+str(j)+str(k)) == str(l)),
                                                        Int(self.d+str(i)+str(j)+str(k)+str(p)) == self.learn.get_value(p, l, self.var))
                                )
                        if temp_k == None:
                            temp_k = temp_l
                        else:
                            temp_k = And(temp_k, temp_l)
                    if temp_j == None:
                        temp_j = temp_k
                    else:
                        temp_j = And(temp_j, temp_k)
                    #print temp_j
                if temp_i == None:
                    temp_i = temp_j
                else:
                    temp_i = And(temp_i, temp_j)
            if temp_p == None:
                temp_p = temp_i
            else:
                temp_p = And(temp_p, temp_i)
                    #print temp
        condition8.append(simplify(temp_p))
        #print condition8
        return condition8
    def f9(self, i_num, j_num):
        condition9 = []
        temp_i = None
        for i in range(1, i_num + 1):
            temp_j = None
            for j in range(1, j_num + 1):
                temp_k = None
                for k in range(1, 3):
                    if temp_k == None:
                        temp_k = And("-1" <= Int(self.s+str(i)+str(j)+str(k)), Int(self.s+str(i)+str(j)+str(k)) <= "1")
                    else:
                        temp_k = And(temp_k, And("-1" <= Int(self.s+str(i)+str(j)+str(k)), Int(self.s+str(i)+str(j)+str(k)) <= "1"))
                if temp_j == None:
                    temp_j = temp_k
                else:
                    temp_j = And(temp_j, temp_k)
            if temp_i == None:
                temp_i = temp_j
            else:
                temp_i = And(temp_i, temp_j)
        condition9.append(simplify(temp_i))
        #print condition9
        return condition9
    def f10_11(self, i_num, j_num, variable_num):
        condition = []
        temp_i = None
        for i in range(1, i_num + 1):
            temp_j = None
            for j in range(1, j_num + 1):
                temp_k = None
                for k in range(1, 3):
                    if temp_k == None:
                        temp_k = And("1" <= Int(self.v+str(i)+str(j)+str(k)), Int(self.v+str(i)+str(j)+str(k)) <= str(variable_num), )
                    else:
                        temp_k = And(temp_k, And("1" <= Int(self.v+str(i)+str(j)+str(k)), Int(self.v+str(i)+str(j)+str(k)) <= str(variable_num)))
                if temp_j == None:
                    temp_j = And(temp_k, Int(self.v+str(i)+str(j)+"1") != Int(self.v+str(i)+str(j)+"2"))
                else:
                    temp_j = And(temp_j, temp_k, Int(self.v+str(i)+str(j)+"1") != Int(self.v+str(i)+str(j)+"2"))
            if temp_i == None:
                temp_i = temp_j
            else:
                temp_i = And(temp_i, temp_j)
        condition.append(simplify(temp_i))
        #print condition
        return condition
    def run(self):
        s = Solver()
        n = node()

        s.add(self.f1())
        s.add(self.f2())
        #s.add(self.f3())                                    # problem
        s.add(self.f4(self.i, self.j, self.point_num))
        s.add(self.f5(self.i, self.j, self.point_num))
        s.add(self.f6(self.i, self.j, 2))
        s.add(self.f7(self.i, self.j, self.point_num))
        s.add(self.f8(self.i, self.j, self.point_num, self.variable_num))
        s.add(self.f9(self.i, self.j))
        s.add(self.f10_11(self.i, self.j, self.variable_num))
        #s.add(And(self.f2(), self.f4(2,2,1), self.f5(2,2,1), self.f6(2,2,1), self.f7(2,2,1), self.f8(2,2,1,2), self.f9(2,2), self.f10_11(2,2,2)))
        #s.add(simplify(Or(And(Bool("a") == True, Int("x") <= Int("y")), And(Bool("a") == False, Int("x") > Int("y")))))
        #print simplify(Or(And(True, Int("x") <= Int("y")), And(False, Int("x") > Int("y"))))
        print (s.check())
        print (s.model())
        #print (s.model()[Int(self.s+"111")])
        #s.add(Not(s.model()))
        #print (s.check())
        #print (s.model())


if __name__ == '__main__':
    z = z3test()
    z.run()



#x = Real('x')
#y = Real('y')
#s = Solver()
#s.add(x + y < 5, x > 0, y > 1)
#print (s.check())
#print (s.model())