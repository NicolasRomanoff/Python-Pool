class calculator:
    '''Calculator for 2 list'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Print the sum of the multiplications of the two vectors'''
        print(f"Dot product is: {sum([v1 * v2 for v1, v2 in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Print a vector having the sum of the other two'''
        print(f"Add Vector is : {[float(v1 + v2) for v1, v2 in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Print a vector having the subtraction result of the other two'''
        print(f"Add Vector is : {[float(v1 - v2) for v1, v2 in zip(V1, V2)]}")
