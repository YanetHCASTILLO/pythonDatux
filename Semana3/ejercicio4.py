class Producto:
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
    def __str__(self) -> str:
        return f"el producto {self.nombre} con codigo:{self.codigo} de pais {self.codigo[0:4]} tiene la cantidad de {self.codigo[5:9]}"

prod1=Producto("cartuchera",'PERU-0001-2023')
prod2=Producto("lapicero",'PERU-0003-2024')
print(prod1)
print(prod2)