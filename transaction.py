from datetime import datetime
date = datetime.now()
tahun = date.year
bulan = date.month
hari = date.day

reload = "y"
while reload == "y":
        print("""
-----------------------------------------------
        SELAMAT DATANG DI OREKAA SPORT
              PUSAT SPORT CENTRE
-----------------------------------------------
a. Nike
b. Adidas 
c. Puma
d. Reebok
-----------------------------------------------
*jumlah maksimal untuk pembelian yaitu 5 barang
*pembelian lebih dari 1 mendapat diskon
-----------------------------------------------
                    """)
        pilihan = input("Silahkan pilih merk yang ingin dibeli dengan memasukkan abjad dari list diatas : ")
 
# NIKE
        if pilihan == "a" or pilihan == "A":
            stop = "y"
            while stop == "y":
                nama_barang = "Nike"
                ukuran_barang = []
                tipe_barang = []
                harga_brg = []
                harga_discount = 0
                jumlah_beli = int(input("Berapa barang yang ingin dibeli? : "))

                for i in range(jumlah_beli):
                    print("""
-----------------------------
        LIST PRODUK
-----------------------------
1. Air Force     3. Blazer
2. Air Jordan    4. Waffle One
-----------------------------
                        """)

                    print("Data ke - ", i + 1)
                    tipe_produk = int(input("Input tipe produk (1/2/3/4) : "))
                    if tipe_produk == 1:
                        tipe_barang.append("Air Force")
                        harga_barang = 250000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 2:
                        tipe_barang.append("Air Jordan")
                        harga_barang = 300000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 3:
                        tipe_barang.append("Blazer")
                        harga_barang = 350000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 4:
                        tipe_barang.append("Waffle One")
                        harga_barang = 400000
                        harga_brg.append(harga_barang)
                    else:
                        print("Produk tidak ada dalam list!")

                    print("""
-----------------------
      LIST UKURAN
-----------------------
 - 35-36       - 37-38
 - 39-40       - 41-42
 - 43-44
-----------------------
                        """)

                    ukuran = input("Ukuran sepatu : ")
                    ukuran_barang.append(ukuran)    

                if jumlah_beli <= 5:
                    if jumlah_beli > 1:
                        discount = 0.25
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i
                        print("harga : ", harga)
                        total_harga = int(harga - (discount * harga))
                        print("harga dsc : ", total_harga)

                    else:
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i

                        total_harga = int(jumlah_beli * harga)

                else:
                    print("*Jumlah maksimal untuk pembelian 5 barang\n")

                print("\n----------------------------------------------")
                print("               Struk Pembelian")
                print("----------------------------------------------")
                print("Date: {}/{}/{}".format(hari, bulan, tahun))
                print("----------------------------------------------")
                for i in range(jumlah_beli):
                    print("%d    %s     %s    Rp.%s" % (i+1, tipe_barang[i], ukuran_barang[i], int(harga_brg[i])))
                print("----------------------------------------------")
                print("Harga                        : Rp", harga)
                if jumlah_beli > 1:
                    print("Diskon                   : 25%")
                else:
                    print("Tidak ada diskon")
                print("Total yang harus dibayar     : Rp.", total_harga)
                jumlahbayar = int(input("Uang yang diterima           : Rp. "))
                print("Kembali                      : Rp.", jumlahbayar - total_harga)
                print("----------------------------------------------")
                print("                Terimakasih")
                print("----------------------------------------------")
                
                reload = input("Masukkan y untuk kembali : ")
                break

# ADIDAS
        elif pilihan == "b" or pilihan == "B":
            stop = "y"
            while stop == "y":
                nama_barang = "Adidas"
                ukuran_barang = []
                tipe_barang = []
                harga_brg = []
                harga_discount = 0
                jumlah_beli = int(input("Berapa barang yang ingin dibeli? : "))

                for i in range(jumlah_beli):
                    print("""
-----------------------------
        LIST PRODUK
-----------------------------
1. Ultraboost   3. Gazelle
2. Superstar    4. Stan Smith
-----------------------------
                        """)

                    print("Data ke - ", i + 1)
                    tipe_produk = int(input("Input tipe produk (1/2/3/4) : "))
                    if tipe_produk == 1:
                        tipe_barang.append("Ultraboost")
                        harga_barang = 250000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 2:
                        tipe_barang.append("Superstar")
                        harga_barang = 300000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 3:
                        tipe_barang.append("Gazelle")
                        harga_barang = 350000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 4:
                        tipe_barang.append("Stan Smith")
                        harga_barang = 400000
                        harga_brg.append(harga_barang)
                    else:
                        print("Produk tidak ada dalam list!")

                    print("""
-----------------------
      LIST UKURAN
-----------------------
 - 35-36       - 37-38
 - 39-40       - 41-42
 - 43-44
-----------------------
                        """)

                    ukuran = input("Ukuran sepatu : ")
                    ukuran_barang.append(ukuran)    

                if jumlah_beli <= 5:
                    if jumlah_beli > 1:
                        discount = 0.25
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i
                        print("harga : ", harga)
                        total_harga = int(harga - (discount * harga))
                        print("harga dsc : ", total_harga)

                    else:
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i

                        total_harga = int(jumlah_beli * harga)

                else:
                    print("*Jumlah maksimal untuk pembelian 5 barang\n")

                print("\n----------------------------------------------")
                print("               Struk Pembelian")
                print("----------------------------------------------")
                print("Date: {}/{}/{}".format(hari, bulan, tahun))
                print("----------------------------------------------")
                for i in range(jumlah_beli):
                    print("%d    %s     %s    Rp.%s" % (i+1, tipe_barang[i], ukuran_barang[i], int(harga_brg[i])))
                print("----------------------------------------------")
                print("Harga                        : Rp", harga)
                if jumlah_beli > 1:
                    print("Diskon                   : 25%")
                else:
                    print("Tidak ada diskon")
                print("Total yang harus dibayar     : Rp.", total_harga)
                jumlahbayar = int(input("Uang yang diterima           : Rp. "))
                print("Kembali                      : Rp.", jumlahbayar - total_harga)
                print("----------------------------------------------")
                print("                Terimakasih")
                print("----------------------------------------------")
                
                reload = input("Masukkan y untuk kembali : ")
                break

# PUMA
        elif pilihan == "c" or pilihan == "C":
            stop = "y"
            while stop == "y":
                nama_barang = "Puma"
                ukuran_barang = []
                tipe_barang = []
                harga_brg = []
                harga_discount = 0
                jumlah_beli = int(input("Berapa barang yang ingin dibeli? : "))

                for i in range(jumlah_beli):
                    print("""
-----------------------------
        LIST PRODUK
-----------------------------
1. Future Rider   3. Mayze
2. RS-X Winter    4. Suede
-----------------------------
                        """)

                    print("Data ke - ", i + 1)
                    tipe_produk = int(input("Input tipe produk (1/2/3/4) : "))
                    if tipe_produk == 1:
                        tipe_barang.append("Future Rider")
                        harga_barang = 250000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 2:
                        tipe_barang.append("RS-X Winter")
                        harga_barang = 300000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 3:
                        tipe_barang.append("Mayze")
                        harga_barang = 350000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 4:
                        tipe_barang.append("Suede")
                        harga_barang = 400000
                        harga_brg.append(harga_barang)
                    else:
                        print("Produk tidak ada dalam list!")

                    print("""
-----------------------
      LIST UKURAN
-----------------------
 - 35-36       - 37-38
 - 39-40       - 41-42
 - 43-44
-----------------------
                        """)

                    ukuran = input("Ukuran sepatu : ")
                    ukuran_barang.append(ukuran)    

                if jumlah_beli <= 5:
                    if jumlah_beli > 1:
                        discount = 0.25
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i
                        print("harga : ", harga)
                        total_harga = int(harga - (discount * harga))
                        print("harga dsc : ", total_harga)

                    else:
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i

                        total_harga = int(jumlah_beli * harga)

                else:
                    print("*Jumlah maksimal untuk pembelian 5 barang\n")

                print("\n----------------------------------------------")
                print("               Struk Pembelian")
                print("----------------------------------------------")
                print("Date: {}/{}/{}".format(hari, bulan, tahun))
                print("----------------------------------------------")
                for i in range(jumlah_beli):
                    print("%d    %s     %s    Rp.%s" % (i+1, tipe_barang[i], ukuran_barang[i], int(harga_brg[i])))
                print("----------------------------------------------")
                print("Harga                        : Rp", harga)
                if jumlah_beli > 1:
                    print("Diskon                   : 25%")
                else:
                    print("Tidak ada diskon")
                print("Total yang harus dibayar     : Rp.", total_harga)
                jumlahbayar = int(input("Uang yang diterima           : Rp. "))
                print("Kembali                      : Rp.", jumlahbayar - total_harga)
                print("----------------------------------------------")
                print("                Terimakasih")
                print("----------------------------------------------")
                
                reload = input("Masukkan y untuk kembali : ")
                break

# Reebok
        elif pilihan == "d" or pilihan == "D":
            stop = "y"
            while stop == "y":
                nama_barang = "Reebok"
                ukuran_barang = []
                tipe_barang = []
                harga_brg = []
                # total_harga = []
                harga_discount = 0
                jumlah_beli = int(input("Berapa barang yang ingin dibeli? : "))
                for i in range(jumlah_beli):
                    print("""
-----------------------------
        LIST PRODUK
-----------------------------
1. Pump Omni      3. LT Court
2. Vintage Chalk  4. NPC II
-----------------------------
                        """)
                    print("Data ke - ", i + 1)
                    tipe_produk = int(input("Input tipe produk (1/2/3/4) : "))
                    if tipe_produk == 1:
                        tipe_barang.append("Pump Omni")
                        harga_barang = 250000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 2:
                        tipe_barang.append("Vintage Chalk")
                        harga_barang = 300000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 3:
                        tipe_barang.append("LT Court")
                        harga_barang = 350000
                        harga_brg.append(harga_barang)
                    elif tipe_produk == 4:
                        tipe_barang.append("NPC II")
                        harga_barang = 400000
                        harga_brg.append(harga_barang)
                    else:
                        print("Produk tidak ada dalam list!")

                    print("""
-----------------------
      LIST UKURAN
-----------------------
 - 35-36       - 37-38
 - 39-40       - 41-42
 - 43-44
-----------------------
                        """)

                    ukuran = input("Ukuran sepatu : ")
                    ukuran_barang.append(ukuran)    

                if jumlah_beli <= 5:
                    if jumlah_beli > 1:
                        discount = 0.25
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i
                        print("harga : ", harga)
                        total_harga = int(harga - (discount * harga))
                        print("harga dsc : ", total_harga)

                    else:
                        harga = 0

                        for i in harga_brg:
                            harga = harga + i

                        total_harga = int(jumlah_beli * harga)

                else:
                    print("*Jumlah maksimal untuk pembelian 5 barang\n")

                print("\n----------------------------------------------")
                print("               Struk Pembelian")
                print("----------------------------------------------")
                print("Date: {}/{}/{}".format(hari, bulan, tahun))
                print("----------------------------------------------")
                for i in range(jumlah_beli):
                    print("%d    %s     %s    Rp.%s" % (i+1, tipe_barang[i], ukuran_barang[i], int(harga_brg[i])))
                print("----------------------------------------------")
                print("Harga                        : Rp", harga)
                if jumlah_beli > 1:
                    print("Diskon                   : 25%")
                else:
                    print("Tidak ada diskon")
                print("Total yang harus dibayar     : Rp.", total_harga)
                jumlahbayar = int(input("Uang yang diterima           : Rp. "))
                print("Kembali                      : Rp.", jumlahbayar - total_harga)
                print("----------------------------------------------")
                print("                Terimakasih")
                print("----------------------------------------------")
                
                reload = input("Masukkan y untuk kembali : ")
                break

        else:
            ulang = input("Apakah anda ingin mengulangi y/n : ")