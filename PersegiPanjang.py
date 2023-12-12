def luasPersegiPanjang(panjang, lebar):
    return "Luas Persegi Panjang adalah", panjang * lebar


def KelPersegiPanjang(panjang, lebar):
    return "Keliling Persegi Panjang adalah", 2 * (panjang + lebar)


panjang = int(input("Masukan Panjang = "))
lebar = int(input("Masukan lebar = "))

print(luasPersegiPanjang(panjang, lebar))
print(KelPersegiPanjang(panjang, lebar))