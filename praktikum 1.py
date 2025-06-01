def cetak(teks):
    __builtins__.print(teks)


class mahasiswa:
    def __init__(self, nama, nim, ipk=4):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk 


    def tampilkan_info(self):
        cetak("data mahasiswa")
        cetak(f"nama : {self.nama}")
        cetak(f"nim : {self.nim}")
        cetak(f"ipk : {self.ipk}")


mhs1 = mahasiswa("akhoqi","452024611050",4)
mhs2 = mahasiswa("wafa","452024611051",4)


mhs1.tampilkan_info()
mhs2.tampilkan_info()
                
        