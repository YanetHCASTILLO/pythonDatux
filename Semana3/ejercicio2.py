class Producto:
    def __init__(self,nombre,tipo,cantidad) -> None:
        self.nombre=nombre
        self.tipo=tipo
        self.cantidad=cantidad
    def __str__(self) -> str:
        return f"{self.nombre} es de tipo {self.tipo} y la cantidad disponible es: {self.cantidad}"

class Catalogo:
    listaProducto=[]
    def __init__(self) -> None:
        self.name="Catalogo Producto"
        self.listaProducto=[]
    def agregar(self, x):  # p será un objeto Pelicula
        self.listaProducto.append(x)
    def mostrar(self):
        for iterador in self.listaProducto:
            print(iterador)  # Print toma por defecto str(p)
    
    
producto1=Producto("llanta","respuesto",20)
producto2=Producto("puerta","respuesto",10)

c1=Catalogo()
c1.agregar(producto1)
c1.agregar(producto2)
c1.mostrar()