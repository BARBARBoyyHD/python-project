
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

    def HargaJual(self,HargaBeli):
        if self.IsEmpty():
            untung = int(input("Berapa Persen Keuntungan : "))
            untung =  untung / 100
            HargaJual = (HargaBeli * untung) + HargaBeli
        else:
            untung = int(input("Berapa Persen Keuntungan : "))
            untung = untung / 100
            HargaJual = (HargaBeli * untung) + HargaBeli
        return HargaJual

    def StatusStok(self,Stok):
        if self.IsEmpty():
            if Stok >= 35:
                StatusStok = "Aman"
            elif Stok < 35:
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
    def TambahTengahSingle(self,DataBaru,KodeBrg):
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
                # Pencarian Node terakhir
                while (Phapus.next is not None):
                    Phapus = Phapus.next

                # pencarian node sebelum node terakhir
                bantu = self.awal
                while (bantu.next is not Phapus):
                    bantu = bantu.next

                bantu.next = None

            Elemen = Phapus.info
            del Phapus
            print('Data yang dihapus: ', Elemen)

    # Penghapusan Tengah
    def HapusTengahSingle(self,KodeBrg):
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
    def PencarianKodeBarang(self,cari):
        if self.IsEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                if cari in str(bantu.KodeBrg):
                    print(f"{bantu.nim} \t | {bantu.nama} \t\t | {bantu.nilai} \t\t | {bantu.indeks}")
                bantu = bantu.next

    def PencarianStatusStok(self,cari):
        if self.IsEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                if cari in bantu.StatusStok:
                    print(f"{bantu.nim} \t | {bantu.nama} \t\t | {bantu.nilai} \t\t | {bantu.indeks}")
                bantu = bantu.next

    def PencarianHargaJual(self,cari):
        if self.IsEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                if cari in bantu.HargaJual:
                    print(f"{bantu.nim} \t | {bantu.nama} \t\t | {bantu.nilai} \t\t | {bantu.indeks}")
                bantu = bantu.next

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

            #Proses pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp
            #Tempatkan i ke Simpul berikutnya
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

            print()


List1 = LinkedList()

def menuUtama():
    print("MENU PILIHAN")
    print("____________")
    print("1. Penambahan Data Barang")
    print("2. Penghapusan Data Barang")
    print("3. Pencarian Data Barang")
    print("4. Pengubahan Data Barang")
    print("5. Tampil Data Barang")
    print("0. Keluar")
    while True:
        menu = input("Masukkan Menu Pilihan : ")
        if menu == "1":
            menuPenambahan()
        elif menu == "2":
            menuPenghapusan()
        elif menu == "3":
            menuPencarian()
        elif menu == "4":
            menuPengubahan()
        elif menu == "5":
            menuTampil()
        elif menu == "0":
            List1.Penghancuran()
            print("Kamu keluar dari menu")

            break
        else:
            print("Pilihan menu hanya 0 sampai 5")

def menuPenambahan():
    print("MENU PENAMBAHAN DATA")
    print("____________________")
    print("1. Penambahan Data Barang Di Depan")
    print("2. Penambahan Data Barang Di Belakang")
    print("3. Penambahan Data Barang Di Tengah")
    print("0. Keluar")
    pilih = int(input("Masukkan Menu Pilihan : "))
    while pilih != 0:
        KodeBrg = str(input("Masukkan Kode Barang : "))
        NamaBrg = str(input("Masukkan Nama Barang : "))
        Stok = int(input("Masukkan Stok : "))
        StatusStok = List1.StatusStok(Stok)
        HargaBeli = int(input("Masukkan Harga Beli : "))
        HargaJual = List1.HargaJual(HargaBeli)
        if pilih == 1:
            List1.TambahDepanSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
            List1.TampilData()
        elif pilih == 2:
            List1.TambahBelakangSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
            List1.TampilData()
        elif pilih == 3:
            List1.TambahTengahSingle([KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual],[KodeBrg,NamaBrg,StatusStok,HargaBeli,Stok,HargaJual])
            List1.TampilData()
        elif pilih == 0:
            print("Kembali ke Menu Utama")
            menuUtama()
            print("MENU PENAMBAHAN DATA")

        print("____________________")
        print("1. Penambahan Data Barang Di Depan")
        print("2. Penambahan Data Barang Di Belakang")
        print("3. Penambahan Data Barang Di Tengah")
        print("0. Keluar")
        pilih = int(input("Masukkan Menu Pilihan : "))
        if pilih == 0 :
            menuUtama()


def menuPenghapusan():
    print("MENU PENGHAPUSAN DATA")
    print("1. Penghapusan Data Barang Di Depan")
    print("2. Penghapusan Data Barang Di Belakang")
    print("3. Penghapusan Data Barang Di Tengah")
    print("0. Keluar")
    pilih = int(input("Masukkan Menu Pilihan : "))
    while pilih != 0:
        pilih = int(input("Masukkan Menu Pilihan : "))
        if pilih == 1:
            List1.HapusDepanSingle()
            List1.TampilData()
        elif pilih == 2:
            List1.HapusBelakangSingle()
            List1.TampilData()
        elif pilih == 3:
            List1.HapusTengahSingle()
            List1.TampilData()
        elif pilih == 0:
            print("Kembali ke Menu Utama")
            menuUtama()
        print("____________________")
        print("1. Penambahan Data Barang Di Depan")
        print("2. Penambahan Data Barang Di Belakang")
        print("3. Penambahan Data Barang Di Tengah")
        print("0. Keluar")
        pilih = int(input("Masukkan Menu Pilihan : "))
        if pilih == 0 :
            menuUtama()

def menuPencarian():
    print("MENU PENCARIAN DATA")
    print("1. Pencarian Kode Barang Tertentu")
    print("2. Pencarian Status Stok Tertentu")
    print("3. Pencarian Harga Jual Tertentu")
    print("0. Keluar")
    pilih = int(input("Masukkan Menu Pilihan : "))
    while pilih != 0:
        print("Menu tersebut tidak terdaftar, silahkan masukkan kembali menu yang diinginkan")
        pilih = int(input("Masukkan Menu Pilihan : "))
        if pilih == 1:
            cari = input("Masukkan Kode Barang : ")
            print("Kode Barang \t | Nama Barang\t | Status Stok\t | Harga Beli\t | Stok\t | Harga Jual\t ")
            List1.PencarianKodeBarang(cari)
            menuUtama()
        elif pilih == 2:
            cari = input("Masukkan Kode Barang : ")
            print("Kode Barang \t | Nama Barang\t | Status Stok\t | Harga Beli\t | Stok\t | Harga Jual\t ")
            List1.PencarianStatusStok(cari)
            menuUtama()
        elif pilih == 3:
            cari = input("Masukkan Kode Barang : ")
            print("Kode Barang \t | Nama Barang\t | Status Stok\t | Harga Beli\t | Stok\t | Harga Jual\t ")
            List1.PencarianHargaJual(cari)
            menuUtama()
        elif pilih == 0:
            print("Kembali ke Menu Utama")
            menuUtama()
        print("____________________")
        print("1. Penambahan Data Barang Di Depan")
        print("2. Penambahan Data Barang Di Belakang")
        print("3. Penambahan Data Barang Di Tengah")
        print("0. Keluar")
        pilih = int(input("Masukkan Menu Pilihan : "))
        if pilih == 0 :
            menuUtama()

def menuPengubahan():
    List1.UbahData()

def menuTampil():
    List1.TampilData()


menuUtama()

