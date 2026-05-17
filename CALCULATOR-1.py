class calculator:
    num_1=int(input('Enter a Number A: '))
    num_2=int(input('Enter a Number B: '))            
    def add(self):
        print("Addition of Two Numbers: ",self.num_1+ self.num_2)
    def sub(self):
        print("Subtraction of Two Numbers: ",self.num_1-self.num_2)
    def mul(self):
        print("Multiplication of Two Numbers: ",self.num_1*self.num_2)
    def div(self):
        print("Division of Two Numbers: ",self.num_1/self.num_2)
def main():
    cal=calculator()
    while True:
        print('1.ADDITION')
        print('2.SUBTRACTION')
        print('3.MULTIPLICATION')
        print('4.DIVITION')
        choice=int(input("Enter Choice: "))
        if choice==1:
            cal.add()
            break
        elif choice==2:
            cal.sub()
            break
        elif choice==3:
            cal.mul()
            break
        elif choice==4:
            cal.div()
            break
        else:
            print("invalid")
main()
