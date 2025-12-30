#***********FUNCION calcularIMC*******
def calcularIMC(peso, estatura):
    estaturaMetros=estatura/100
    imc=peso/estaturaMetros**2
    return round(imc, 4)
#Recibe dos parámetros
#   peso: float, el peso de la persona en kilos
#   estatura: float, la estatura de la persona en CENTIMETROS
#Calcula el imc
#Antes de aplicar la fórmula transforme los CENTIMETROS en METROS
#Retornar el imc redondeado a 4 decimales, 
#puede usar la función round. Ejemplo: return round(imc,4)
#***********FUNCION interpretarIMC*******
def interpretarIMC(imc):

    if imc>=0 and imc<16:
       resultado="Delgadez severa"
       return resultado
    elif imc>=16 and imc<17:
        cal2="Delgadez moderada"
        return cal2
    elif imc>=17 and imc<18.5:
        resultado="Delgadez leve"
        return resultado
    elif imc>=18.5 and imc<25:
        resultado="Peso normal"
        return resultado
    elif imc>=25 and imc<30:
        resultado="Sobrepeso"
        return resultado
    elif imc>=30 and imc<35:
        resultado="Obesidad Grado 1"
        return resultado
    elif imc>=35 and imc<40:
        resultado="Obesidad Grado 2"
        return resultado
    elif imc>=40:
        resultado="Obesidad Grado 3"
        return resultado
    
    else:
         resultado="IMC fuera de rango"
         return resultado

#Recibe un parámetro
#   imc: float, el valor del imc de la persona
#RETORNA un mensaje del estado de la persona en base al valor
#recibido con la tabla de ejercicios anteriores, por ejemplo
#Obesidad Grado 3, Peso Normal, etc
#IMPORTANTE: colocar bien los extremos de los rangos 

