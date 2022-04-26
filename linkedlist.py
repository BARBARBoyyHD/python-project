#1. Pendefinisian Struktur Data Linked List



print("----- pilih Menu -----")
print("1. Penambahan Data Barang")
print("2. Penghapusan Data Barang")
print("3. Pencarian Data Barang")
print("4. Pengubahan Data Barang")
print("5. Tampil Data Barang")
print("0. keluar")
pilih = int(input("Pilih Menu :"))

# Class Untuk Node
class data :
    def __init__(self,info):
        self.info = info
        self.next = None


# Class Untuk Linked List
class linkedList:
    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return self.awal is None
    def tampilData(self):
        print("Isi Data Barang: ",end=" ")
        if self.isEmpty():
            print("Data Kosong")
        else:
            bantu = self.awal
            while bantu is not None:
                    print(bantu.info," ",end=" ")
                    if (bantu.next != None):
                        print(" ",end=" ")
                    bantu = bantu.next

            print()
    def banyakNode(self):
        if self.isEmpty() :
            bykNode = 0
        else:
            bantu = self.awal
            bykNode = 0
            while bantu is not None: 
                bykNode += 1
                bantu = bantu.next
        return bykNode
    def penghancuran(self):
        Phapus = self.awal
        while Phapus != None:
            Phapus = Phapus.next
            del Phapus
            Phapus = self.awal

# Operasi Pencarian
# Pencarian Data
    def PencarianAngka (self) :
        if self.isEmpty():
            print ("Data Kosong")
        else:
            CariAngka = int(input("Masukan Angka Yang Dicari : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == CariAngka):
                    ketemu = True
                else:
                    bantu = bantu.next
            if(ketemu):
                print("Angka",CariAngka,"Ditemukan")
            else:
                print("Angka",CariAngka,"Tidak Ditemukan")
# Pencarian Node
    def PencarianNode (self) :
        if self.isEmpty():
            print ("Data Kosong")
        else:
            CariNode = int(input("Masukan Node Yang Dicari : "))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if (posisi == CariNode):
                    ketemu = True
                else:
                    bantu = bantu.next
                    posisi += 1
            if(ketemu):
                print("Node Ke -",CariNode,"Ditemukan")
            else:
                print("Node Ke -",CariNode,"Tidak Ditemukan")

# Penambahan Data
# Penambahan di Depan
    def SisipDepanSingle(self,DataBaru):
        Baru = data(DataBaru)
        if(not self.isEmpty()):
            Baru.next = self.awal
        self.awal = Baru
# Penambahan di Belakang
    def SisipBelakangSingle(self,DataBaru):
        Baru = data(DataBaru)
        if(self.isEmpty()):
            self.awal = Baru
        else:
            bantu = self.awal
            while (bantu.next is not None):
                bantu = bantu.next
            bantu.next = Baru

# Penambahan di Tengah (Sisip)
    def SisipTengahSingle(self, DataBaru):
        SisipSetelah = int(input("Sisipkan Setelah : "))
        bantu = self.awal
        ketemu = False
        while(not ketemu) and (bantu is not None):
            if(bantu.info == SisipSetelah):
                ketemu = True
            else:
                bantu = bantu.next
        if(ketemu):
            Baru = data(DataBaru)
            if(bantu.next is None):
                self.SisipBelakangSingle(DataBaru)
            else:
                Baru.next = bantu.next
                bantu.next = Baru
        else:
            print("Data",SisipSetelah,"Tidak Ditemukan")

# Pengubahan Data
    def UbahData(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            DataUbah = int(input("Masukan Data Yang Ingin Diubah : "))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == DataUbah):
                    ketemu = True
                else:
                    bantu = bantu.next
            if (ketemu):
                DataBaru = int(input("Masukan Data Peubah : "))
                bantu.info = DataBaru
            else:
                print("Angka", DataUbah, "Tidak Ditemukan")

# Penghapusan Data
    def SatuNode(self):
        bantu = self.awal
        if(bantu.next is None):
            return True
        else:
            return False
# Penghapusan Depan
    def HapusDepanSingle(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            Elemen = Phapus.info
            if(self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next
            del Phapus
            print("Data Yang Dihapus Adalah : ",Elemen)
# Penghapusan Belakang
    def HapusBelakangSingle(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            if(self.SatuNode()):
                self.awal = None
            else:
                # Pencarian Node Terakhir
                while(Phapus.next is not None):
                    Phapus = Phapus.next
                # Pencarian Node Sebelum Node Terakhir
                bantu = self.awal
                while(bantu.next is not Phapus):
                    bantu = bantu.next

                bantu.next = None

            Elemen = Phapus.info
            del Phapus
            print("Data Yang Dihapus Adalah : ",Elemen)


# Penghapusan Tengah
    def HapusTengahSingle(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            DataHapus = int(input("Masukan Angka Yang Akan Dihapus : "))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.info == DataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next
            if (ketemu):
                Elemen = Phapus.info
                if(Phapus == self.awal):
                    self.HapusDepanSingle()
                elif (Phapus.next is None):
                    self.HapusBelakangSingle()
                else:
                    bantu = self.awal
                    while(bantu.next is not Phapus):
                        bantu = bantu.next
                    bantu.next = Phapus.next
                    del Phapus
                    print("Data Yang Dihapus Adalah : ", Elemen)
            else:
                print("Angka", DataHapus, "Tidak Ditemukan")

# Pengurutan Data Secara Ascending Minimum Sort
    def UrutData(self):
        i = self.awal
        while(i.next is not None):
            min = i
            j = i.next
            while(j is not  None):
                if(j.info < min.info):
                    min = j
                j = j.next
            #Proses Pertukaran
            temp = min.info
            min.info = i.info
            i.info = temp

            #Tempatkan i ke simpul berikutnya
            i = i.next



# 2. Inisialisai Linked List
list1 = linkedList()
# print("Awal Linked List1 :",list1.awal)

# 3. Memasukan Data Ke Linked List Secara Langsung
# node1 = data(["Dinar","IF2",10121060])
node1 = data(234)
node2 = data(345)
node3 = data(223)
node4 = data(101)
node5 = data(255)

# print("Isi Node1 :",node1.info,"->",node1.next)
# print("Isi Node2 :",node2.info,"->",node2.next)


# Membuat Linked List dari 4 Node
list1.awal = node1
node1.next = node3
node3.next = node2
node2.next = node4
node4.next = node5

# print("Isi Node1 :",node1.info,"->",node1.next)
# print("Isi Node2 :",node2.info,"->",node2.next)
if pilih == 1:
    print("------ Menu Penambahan ------")
    print("1.Penambahan Data Barang di Depan")
    print("2.Penambahan Data Barang di Belakang")
    print("3.Penambahan Data Barang di Tengah")
    pilhpnmbhn = int(input("Pilih Menu : "))
    if pilhpnmbhn == 1:
        DataBaru = int(input("Masukan Data Baru : "))
        list1.SisipDepanSingle(DataBaru)
        list1.tampilData()
    elif pilhpnmbhn == 2:
        DataBaru = int(input("Masukan Data Baru : "))
        list1.SisipBelakangSingle(DataBaru)
        list1.tampilData()
    elif pilhpnmbhn == 3:
        DataBaru = int(input("Masukan Data Baru : "))
        list1.SisipTengahSingle(DataBaru)
        list1.tampilData()


# 4. Traversal Linked List - Menampilkan Data
#list1.tampilData()

# 5. Traversal Linked List - Menghitung Banyaknya Data
# print("Banyak Data : ",list1.banyakNode())

# 7. Pencarian Linked List
# Pencarian Medan Data
# list1.PencarianAngka()
# Penarian Node
# list1.PencarianNode()

# 8. Penambahan Data
#DataBaru = int(input("Masukan Data Baru : "))
# Penambahan di Depan
#list1.SisipDepanSingle(DataBaru)
# Penambahan di Belakang
#list1.SisipBelakangSingle(DataBaru)
# Penambahan di Tengah (Sisip)
#list1.SisipTengahSingle(DataBaru)

# 9. Pengubahan Data
# list1.UbahData()

# 10. Penghapusan Data
# Penghapusan Depan
# list1.HapusDepanSingle()
# Penghapusan Belakang
# list1.HapusBelakangSingle()
# Penghapusan Tengah
# list1.HapusTengahSingle()
#if(list1.isEmpty()):
    #print("Data Kosong")
#else:
    #list1.UrutData()


#list1.tampilData()

# 6. Penghancuran Linked List
#list1.penghancuran()
# list1.tampilData()
#print("Banyak Data : ",list1.banyakNode())