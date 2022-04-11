class Operaciones():
    def suma(self,sumando1,sumando2):
        for n in (sumando1, sumando2):
            if not isinstance(n,int) and not isinstance(n,float):
                raise TypeError("No es un int ni un float")
        return sumando1+sumando2

    def ingresoDatos(self,dato):
        if (not type(dato) is float) or (not type(dato) is int):
            try:
                dato=float(dato)
            except ValueError:
                print(f"El dato ingresado \"{dato}\" no se puede convertir a float")
                exit(2)
        return dato