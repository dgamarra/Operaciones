from src.logica.Operaciones import Operaciones

if __name__ == '__main__':
    operacion = Operaciones()
    sumando1 = operacion.ingresoDatos(input("Ingrese el primer sumando  : "))
    sumando2 = operacion.ingresoDatos(input("Ingrese el segundo sumando : "))
    resultado = operacion.suma(sumando1, sumando2)
    print("{0:.2f} + {1:.2f} = {2:.2f}".format(sumando1, sumando2, resultado))

    sumando1="3.5"
    sumando2=4
    sumando1 = operacion.ingresoDatos(sumando1)
    sumando2 = operacion.ingresoDatos(sumando2)
    resultado = operacion.suma(sumando1, sumando2)
    print("{0:.2f} + {1:.2f} = {2:.2f}".format(sumando1, sumando2, resultado))

    sumando1="3.8"
    sumando2=4
    sumando1 = operacion.ingresoDatos(sumando1)
    sumando2 = operacion.ingresoDatos(sumando2)
    resultado = operacion.suma(sumando1, sumando2)
    print("{0:.2f} + {1:.2f} = {2:.2f}".format(sumando1, sumando2, resultado))

    #sumando1="3.10"
    #sumando2=4
    #resultado = operacion.suma(sumando1, sumando2)
    #print("{0:.2f} + {1:.2f} = {2:.2f}".format(sumando1, sumando2, resultado))

    operacion = Operaciones()
    minuendo = operacion.ingresoDatos(input("Ingrese el minuendo     : "))
    sustraendo = operacion.ingresoDatos(input("Ingrese el sustraendo : "))
    resultado = operacion.resta(minuendo, sustraendo)
    print("{0:.2f} - {1:.2f} = {2:.2f}".format(minuendo, sustraendo, resultado))