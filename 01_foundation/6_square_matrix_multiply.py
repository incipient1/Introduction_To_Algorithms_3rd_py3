import pprint
def matrix_multiply(a,b):
    def matrix_multiply_mask(mata,matb):
        if mata.row == 1:
            c11 = [[\
                    mata.mat_list[mata.row_list[0]][mata.col_list[0]] *\
                    matb.mat_list[matb.row_list[0]][matb.col_list[0]] \
                    ]]
            return Matrix(c11)
        else:
            mata11 = mata.divide('11')
            mata12 = mata.divide('12')
            mata21 = mata.divide('21')
            mata22 = mata.divide('22')

            matb11 = matb.divide('11')
            matb12 = matb.divide('12')
            matb21 = matb.divide('21')
            matb22 = matb.divide('22')

            s1 = matb12 - matb22
            s2 = mata11 + mata12
            s3 = mata21 + mata22
            s4 = matb22 - matb11
            s5 = mata11 + mata22
            s6 = matb11 + matb12
            s7 = mata12 - mata22
            s8 = matb21 + matb22
            s9 = mata11 - mata21
            s10 = matb11 + matb12

            p1 = matrix_multiply_mask(mata11,s1)
            p2 = matrix_multiply_mask(s2,matb22)
            p3 = matrix_multiply_mask(s3,matb11)
            p4 = matrix_multiply_mask(mata22,s4)
            p5 = matrix_multiply_mask(s5,s6)
            p6 = matrix_multiply_mask(s7,s8)
            p7 = matrix_multiply_mask(s9,s10)

            c11 = (p5 + p4 - p2 + p6)
            c12 = (p1 + p2)
            c21 = (p3 + p4)
            c22 = (p5 + p1 - p3 -p7)

            return matrix_merge(c11,c12,c21,c22)

    mata = Matrix(a)
    matb = Matrix(b)
    product = matrix_multiply_mask(mata,matb)
    return product.mat_list

def matrix_merge(c11,c12,c21,c22):
    mat_list = []
    for i in c11.row_list:
        mat_list.append(c11.mat_list[i] + c11.mat_list[i])

    for i in c21.row_list:
        mat_list.append(c21.mat_list[i] + c21.mat_list[i])

    return Matrix(mat_list)

class Matrix(object):
    def __init__(self,*args):
        if len(args) == 1 and isinstance(args[0],list):
            self.mat_list = args[0]
            self.row = len(args[0])
            self.col = len(args[0][0])
            self.row_list = range(self.row)
            self.col_list = range(self.col)

    def __add__(self,mat2):    # __add__ 、 __sub__ 是类的专有方法
        mat_list = []
        for i in range(self.row):
            list_1 = []
            for j in range(self.col):
                list_1.append(
                              self.mat_list[ self.row_list[i] ][ self.col_list[j] ] + \
                              mat2.mat_list[ mat2.row_list[i] ][ mat2.col_list[j] ] \
                              )
            mat_list.append(list_1)

        return Matrix(mat_list)

    def __sub__(self,mat2):
        mat_list = []
        for i in range(self.row):
            list_1 = []
            for j in range(self.col):
                list_1.append(self.mat_list[ self.row_list[i] ][ self.col_list[j] ] - \
                              mat2.mat_list[ mat2.row_list[i] ][ mat2.col_list[j] ] \
                              )
            mat_list.append(list_1)

        return Matrix(mat_list)

    def divide(self,block):
        result = Matrix()
        result.mat_list = self.mat_list
        result.row = self.row // 2
        result.col = self.col // 2
        dic = {'11':[ self.row_list[:result.row],self.col_list[:result.col] ],
               '12':[ self.row_list[:result.row],self.col_list[result.col:] ],
               '21':[ self.row_list[result.row:],self.col_list[:result.col] ],
               '22':[ self.row_list[result.row:],self.col_list[result.col:] ]
               }
        result.row_list = dic[block][0]
        result.col_list = dic[block][1]
        return result

a = [[2,-7,5,-3],
     [5,-7,9,-7],
     [-3,-6,8,1],
     [1,0,-2,-1]]
b = [[4,8,-12,5],
     [2,1,9,4],
     [12,23,-21,5],
     [8,-3,0,7]]
c = matrix_multiply(a, b)
pprint.pprint(c)