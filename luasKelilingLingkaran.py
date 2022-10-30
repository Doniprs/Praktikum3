# import module math
import math

# Variable jariJari menampung nilai input yang dimasukkan yaitu berupa string
jariJari = input('Masukkan jari-jari lingkaran :')

"""
rumus luas & keliling lingkarang

----------------------------------
luas = phi * r^2
----------------------------------

"""
# convert string to integer
jariJari = int(jariJari)

# hitung luas lingkaran
luas = math.pi * (jariJari*jariJari)

# hitung luas keliling
keliling = 2 * math.pi * jariJari

# output luas & keliling lingkaran

# output luas & keliling lingkaran
# .2f => mengambil 2 langka setelah (,)
print("Berikut Luas Lingkaran = ", format(luas, '.2f'))
print("Berikut Keleling Lingkaran = ", format(keliling, '.2f'))
