#Los conjuntos son colecciones datos que no tienen orden definido
#Siempre van {}
meses = {"enero", "marzo", "febrero", "abril"}
print(meses)

print("enero" in meses)

# Se agrega nuevo elemento
meses.add("julio")
print(meses)
# Se conjunto de nuevos elementos
meses.update(["agosto", "setiembre", "octubre"])
print(meses)
# Se eliminan elementos (.discard y .remove son lo mismo)
meses.discard("octubre")
print(meses)