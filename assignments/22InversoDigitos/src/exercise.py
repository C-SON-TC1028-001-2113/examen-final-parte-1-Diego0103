def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    if num>999999:
        print('Too long')
    else: 
        inv = 0
        ult = 0
        negativo = False
        if num<0:
            negativo = True
            num = num*-1
        while num>=10:
            ult=num%10
            num=num//10
            inv=inv*10+ult
        inv=inv*10+num
        if negativo:
            inv=inv*-1
        print (inv)  



if __name__=='__main__':
    main()
