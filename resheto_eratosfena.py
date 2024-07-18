class resheto():
    def eratosfen(self,main_number):

        my_list = [i for i in range(main_number+1)]

        my_list[1]=0

        number1 = 2
        while number1 <= main_number:
            if my_list[number1] != 0:

                number2 = number1 + number1

                while number2 <= main_number:

                    my_list[number2] = 0
                
                    number2 = number2 + number1
            number1 += 1
        my_list = [i for i in my_list if i != 0]
        return my_list
if __name__ == "__main__":
    obj = resheto()
    print(obj.eratosfen(35))