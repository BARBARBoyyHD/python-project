# 1. Pendefinisian Struktur Data Linked List
print("MENU PILIHAN")
print("____________")
print("1. Penambahan Data Barang")
print("2. Penghapusan Data Barang")
print("3. Pencarian Data Barang")
print("4. Pengubahan Data Barang")
print("5. Tampil Data Barang")
print("0. Keluar")
pilih = int(input("Masukkan Menu Pilihan : "))

class Barang:
    def __init__(self,KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual):
        self.KodeBrg = KodeBrg
        self.NamaBrg = NamaBrg
        self.StatusStok = StatusStok
        self.HargaBeli = HargaBeli
        self.Stok = Stok
        self.HargaJual = HargaJual
        
class DataBarang:
    def __init__(self,Barang):
        self.info = Barang
        self.next = None

# Class Linked List
class LinkedList:
    def __init__(self):
        self.awal = None

    def IsEmpty(self):
        return self.awal is None

    def BanyakNode(self):
        if self.IsEmpty():
            byknode = 0
        else:
            bantu = self.awal
            byknode = 0
            while bantu is not None:
                byknode = byknode + 1
                bantu = bantu.next

        return byknode

    def HargaJual(self):
        if self.IsEmpty():
            untung = int(input("Berapa Persen Keuntungan : "))
            untung =  untung / 100
            HargaJual = (HargaBeli * untung) + HargaBeli
        else:
            untung = int(input("Berapa Persen Keuntungan : "))
            untung = untung / 100
            HargaJual = (HargaBeli * untung) + HargaBeli
        return HargaJual

    def StatusStok(self):
        if self.IsEmpty():
            if Stok <= 35:
                StatusStok = "Aman"
            else:
                StatusStok = "Tidak Aman"
        else:
            if Stok <= 35:
                StatusStok = "Aman"
            else:
                StatusStok = "Tidak Aman"

        return StatusStok

    def Penghancuran(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

    # Penambahan Data
    # Penambahan di Depan
    def TambahDepanSingle(self,DataBaru):
        Baru = DataBarang(DataBaru)
        if (not self.IsEmpty()):
            Baru.next = self.awal
        self.awal = Baru

    # Penambahan di Belakang
    def TambahBelakangSingle(self, DataBaru):
        Baru = DataBarang(DataBaru)
        if (self.IsEmpty()):
            self.awal = Baru
        else:
            bantu = self.awal
            while (bantu.next is not None):
                bantu = bantu.next
            bantu.next = Baru

    # Penambahan di Tengah (sisip)
    def TambahTengahSingle(self,DataBaru):
        SisipSetelah = str(input('Sisipkan Setelah : '))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (bantu.info,KodeBrg == SisipSetelah):
                ketemu = True
            else:
                bantu = bantu.next

        if (ketemu):
            Baru = DataBarang(DataBaru)
            if (bantu.next is None):
                self.TambahBelakangSingle(DataBaru)
            else:
                Baru.next = bantu.next
                bantu.next = Baru
        else:
            print('Data ', SisipSetelah, ' Data Tidak Ditemukan')

    # PENGHAPUSAN DATA
    def SatuNode(self):
        bantu = self.awal
        if (bantu.next is None):
            return True
        else:
            return False

    # Penghapusan Depan
    def HapusDepanSingle(self):
        if (self.IsEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            Elemen = Phapus.info
            if (self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next

            del Phapus
            print('Data yang dihapus adalah : ', Elemen)

    # Penghapusan Belakang
    def HapusBelakangSingle(self):
        if (self.IsEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            if (self.SatuNode()):
                self.awal = None
            else:
               
                while (Phapus.next is not None):
                    Phapus = Phapus.next

              
                bantu = self.awal
                while (bantu.next is not Phapus):
                    bantu = bantu.next

                bantu.next = None

            Elemen = Phapus.info
            del Phapus
            print('Data yang dihapus: ', Elemen)

    # Penghapusan Tengah
    def HapusTengahSingle(self):
        if (self.IsEmpty()):
            print('Data Kosong')
        else:
            DataHapus = str(input('Masukkan Data Yang Ingin Dihapus : '))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.info,KodeBrg == DataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next

            if (ketemu):
                Elemen = Phapus.info
                if (Phapus == self.awal):
                    self.HapusDepanSingle()
                elif (Phapus.next is None):
                    self.HapusBelakangSingle()
                else:
                    bantu = self.awal
                    while (bantu.next is not Phapus):
                        bantu = bantu.next

                    bantu.next = Phapus.next

                    del Phapus
                    print('Data yang dihapus: ', Elemen)
            else:
                print('Angka ', DataHapus, ' Tidak Ditemukan')

#Operasi Pencarian
#Pencarian Kode
    def PencarianKodeBarang (self):
        if self.IsEmpty():
            print('Data Kosong')
        else:
            CariKode = str(input('Masukkan Kode Yang Dicari : '))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if(bantu.info == CariKode):
                    ketemu = True
                else:
                    bantu = bantu.next
                    posisi = posisi+1

            if(ketemu):
                print('Kode ke- ',CariKode,' Ditemukan')
            else:
                print('Kode ke- ',CariKode,' Tidak Ditemukan')

    # Pengubahan Data
    def UbahData(self):
        if (self.IsEmpty()):
            print('Data Kosong')
        else:
            DataUbah = int(input('Masukkan Data Yang Ingin Diubah : '))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == DataUbah):
                    ketemu = True
                else:
                    bantu = bantu.next

            if (ketemu):
                DataBaru = int(input("Data Peubah : "))
                bantu.info = DataBaru
            else:
                print('Data ', DataUbah, ' Tidak Ditemukan')

    def UrutStokDataAsc(self):
        i = self.awal
        while(i.next is not None):
            min = i
            j = i.next
            while(j is not None):
                if(j.info < min.info):
                    min = j
                j = j.next
            temp = min.info
            min.info = i.info
            i.info = temp          
            i = i.next

    def TampilData(self):
        print('Isi Linked List : ', end='')
        if self.IsEmpty():
            print('Data Kosong')              
        else:
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, ' ', end='')
                if (bantu.next is not None):
                    print('->  ', end='')
                bantu = bantu.next
                i = self.awal
                while(i.next is not None):
                    min = i
                    j = i.next
                    while(j is not None):
                        if(j.info > min.info):
                            min = j
                        j = j.next
                    temp = min.info                  
                    min.info = i.info
                    i.info = temp          
                    i = i.next

            print()


List1 = LinkedList()

while pilih != 0: # jika tidak memilih angka 0 maka pengulangan akan berjalan continu 
    if pilih == 1:
        print("MENU PENAMBAHAN DATA")
        print("____________________")
        print("1. Penambahan Data Barang Di Depan")
        print("2. Penambahan Data Barang Di Belakang")
        print("3. Penambahan Data Barang Di Tengah")
        print("0. Keluar")
        pilih = int(input("Masukan Menu Pilihan : "))
        while pilih != 0:
            KodeBrg = str(input("Masukkan Kode Barang : "))
            NamaBrg = str(input("Masukkan Nama Barang : "))
            Stok = int(input("Masukkan Stok : "))
            StatusStok = List1.StatusStok()
            HargaBeli = int(input("Masukkan Harga Beli : "))
            HargaJual = List1.HargaJual()
            if pilih == 1:
                List1.TambahDepanSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
                List1.TampilData()
            elif pilih == 2:
                List1.TambahBelakangSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
                List1.TampilData()
            elif pilih == 3:
                List1.TambahTengahSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
                List1.TampilData()
            print("MENU PENAMBAHAN DATA")
            print("____________________")
            print("1. Penambahan Data Barang Di Depan")
            print("2. Penambahan Data Barang Di Belakang")
            print("3. Penambahan Data Barang Di Tengah")
            print("0. Keluar")
            pilih = int(input("Masukan Menu Pilihan : "))
    elif pilih == 2:
        print("MENU PENGHAPUSAN DATA")
        print("1. Penghapusan Data Barang Di Depan")
        print("2. Penghapusan Data Barang Di Belakang")
        print("3. Penghapusan Data Barang Di Tengah")
        print("0. Keluar")
        pilih = int(input("Masukkan Menu Pilihan : "))
        while pilih != 0:
            if pilih == 1:
                List1.HapusDepanSingle()
                List1.TampilData()
            elif pilih == 2:
                List1.HapusBelakangSingle()
                List1.TampilData()
            elif pilih == 3:
                List1.HapusTengahSingle()
                List1.TampilData()
            print("MENU PENGHAPUSAN DATA")
            print("1. Penghapusan Data Barang Di Depan")
            print("2. Penghapusan Data Barang Di Belakang")
            print("3. Penghapusan Data Barang Di Tengah")
            print("0. Keluar")
            pilih = int(input("Masukkan Menu Pilihan : "))
    elif pilih == 3:
        print("MENU PENCARIAN DATA")
        print("1. Pencarian Kode Barang Tertentu")
        print("2. Pencarian Status Stok Tertentu")
        print("3. Pencarian Harga Jual Tertentu")
        print("0. Keluar")
        pilih = int(input("Masukkan Menu Pilihan : "))
        while pilih != 0:
            if pilih == 1:
                List1.PencarianKodeBarang()

    elif pilih == 4:
        List1.UbahData()
    elif pilih == 5 :
        List1.TampilData()
    elif pilih == 6:
        List1.Penghancuran()


    print("MENU PILIHAN")
    print("____________")
    print("1. Penambahan Data Barang")
    print("2. Penghapusan Data Barang")
    print("3. Pencarian Data Barang")
    print("4. Pengubahan Data Barang")
    print("5. Tampil Data Barang")
    print("0. Keluar")
    pilih = int(input("Masukkan Menu Pilihan : "))













