
es_primo =True

# Busco divisores en el rango de [2; numero-1]
for num in range(2, 10^5):
    if 10^5 % num == 0:
        es_primo=False
        break # 

if es_primo:
    print("numero es primo",es_primo)
else:
    print("numero no es primo",es_primo)
