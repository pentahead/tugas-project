print(" KODE SAPI")
print(" WARRIOR = 1 ")
print(" MAGE    = 2    ")
print(" ASSASIN = 3 ")
print(" NOLEP   = 4   ")
print("\n")


sapi_warrior = 690
sapi_mage = 420
sapi_assasin = 530
sapi_nolep = 330

time = 0
jumlah_sapi = int(input("masukan jumlah sapi: "))
for kode_sapi in range(jumlah_sapi):
    kode_sapi = int(input("masukan kode sapi: "))
    if kode_sapi == 1 :
        time += sapi_warrior
    elif kode_sapi == 2 :
        time += sapi_mage
    elif kode_sapi == 3 :
        time += sapi_assasin
    elif kode_sapi == 4 :
        time += sapi_nolep
    else :
        print("Kode sapi tidak terdaftar")

tahun = int(time // 365)
bulan = int((time - tahun * 365) // 30)
hari = int(time - tahun * 365 - bulan * 30)
print("Jumlah hari yang diperlukan ialah {} tahun, {} bulan,  {} hari".format(
    str(tahun), str(bulan), str(hari)
))