#Creo una lista de números estrboscópicos, tanto de un dígito como de dos.
digits = ['0', '1', '8']
pairs = ['00', '11', '69', '88', '96']

#Defino una fución que identifique los números estroboscópicos dentro de un rango determinado
#que se le pase a la función por parámetro

def estro(n1, n2):
    if n1<n2:
        n=n2-n1
     

        if n % 2:
            medio = n // 2
            for item in estro(n1, n-1):            
                left = item[:medio]
                right = item[medio:]
                for d in digits:
                    yield "".join([left, d, right])            
        elif n == 2:
            for p in pairs:
                yield p
        elif n > 2:
            for item in estro(n, n - 2):
                for p in pairs:     
                    yield "".join([p[0], item, p[1]])
        else:
            yield ""
                      
#Defino la función, que dados dos valores, saque todos los números estroboscópicos que hay entre ellos.       
def get_estro(num1, num2):

    for value in estro(num1, num2):
        if value[0] != '0':
            yield value
            return value




    








        
        

         





    
    


