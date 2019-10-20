### Class that allows to left-rotate elements of a string

class LeftRotation(object):
    """
    Class containing objects that will allow the user to left rotate elements inside of a string.
    """
    
    def rotate(self, string, number_rota):
        """
        Method that will allow the user to left rotate elements inside of a string i.e to shift those
        elements from its initial position to a new position on its left, according to a parameter
        specified in input.
        
        Parameters:
            - string: string input
            - number_rota: number of left rotations
        
        Example: 
            - string = "12345"
            - number_rota = 2
            - output = "34512"
        """
    
        self.string = string
        self.number_rota = number_rota
        self.length = len(self.string)
        
        self.empty_string = ''
        self.i = 0

        print("String Input : {}, Type : {}".format(self.string, type(self.string)))
        print("Number of left-rotation needed : {}, Type : {}".format(self.number_rota, type(self.number_rota)))
        print("Length of the string input : {}, Type : {}".format(self.length, type(self.length)))

        if self.length < 1 or self.length > 10**5:
            print('The length of the string must be between 1 and 10^5')
        elif self.number_rota < 1 or self.number_rota > self.length:
            print('The number of left rotation allowed must be between 1 and {}'.format(self.length))
        else:    
            while (self.i < self.length):
                self.empty_string = self.empty_string + self.string[(self.i + self.number_rota) % self.length]
                self.i = self.i + 1
        return self.empty_string