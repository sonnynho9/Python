s=float(input("Digite o Salario:"))
if s < 500:
            st=s*15/100
            sg=st+s
            print ("Seu Salario é:" ,sg,"com reajuste de 15%")
else:
    if s <1000:
            si=s*10/100
            sh=si+s
            print ("Seu Salario é:",sh,"com reajuste de 10%")
    else:
              sf=s*5/100
              sl=sf+s
              print ("Seu Salario é:",sl,"com reajuste de 5%")

