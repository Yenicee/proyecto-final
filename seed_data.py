from ejemplo.models import Familiar

Familiar(nombre="Yenice", direccion="Av San Vicente 123", numero_pasaporte=984532).save()
Familiar(nombre="Martha", direccion="San Martin 9843", numero_pasaporte=540890).save()
Familiar(nombre="Liliana", direccion="Cutranco 934", numero_pasaporte=348945).save()
Familiar(nombre="Dardo", direccion="Dos Rios 18", numero_pasaporte=124567).save()
Familiar(nombre="Martin", direccion="Av Mendoza 145", numero_pasaporte=345566).save()

print("Se cargo con éxito los usuarios de pruebas")