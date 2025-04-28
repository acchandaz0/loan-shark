# The script of the game goes in this file.
# The game starts here.
label start:
    # 1:World Building #1
    scene bg_kage with Dissolve(5.0)
    scene bg_desa with dissolve
    "Suatu Hari yang cerah di Klaten....."

    # 1:World Building #2
    scene bg_bengkel with dissolve
    "Di bengkel kecil Raka, dinding setengah kayu setengah seng"

    # 1:World Building #3
    "Sosok Raka Mahesa menatap jejeran wayang kulit yang tinggal bayangan, hasil jerih payah milik dirinya dan mendiang kakeknya telah dikirim seminggu lalu"

    # 1:Flash back #1
    scene bg_handshake with dissolve
    "Seminggu lalu, ia menyerahkan semuanya ke Pak Ardi..."

    # 1:Flash back #2
    scene bg_theater with dissolve
    "Seorang pria sopan dan murah senyum yang mengaku punya koneksi dengan kolektor seni internasional"

    # 1:Flash back #3
    scene bg_pachipachi with dissolve
    "Katanya, ia hanya butuh satu batch untuk pembuktian, lalu bisa membuka pasar baru untuk kerajinan lokal"

    # 1:Back to reality #1
    scene bg_layar_lockscreen with dissolve
    "Pembayaran dijanjikan hari ini. Namun, Pak Ardi menghilang tanpa jejak."

    # 1:Back to reality #2
    scene bg_layar_wa_centang1 with dissolve
    "Sudah dihubungi berkali-kali tapi tidak terjawab."

    # 1: Anxious #1
    scene bg_motor_ngebut with dissolve
    "Dengan pikirannya yang berpacu, Raka pun dengan cemas menuju ke kediaman Pak Ardi"

    # 1: Anxious #2
    scene bg_black with dissolve
    "Tapi yang ia temukan hanya..." #(bg black)

    scene bg_reveal_rumah with dissolve
    show raka kecewa belakang with dissolve
    "Rumah kontrakan yang kosong dan berantakan, seolah penghuninya melarikan diri dengan terburu-buru" #(bg reveal)
    
    # 1: Anxious #3
    scene bg_rumah1
    "Ia terdiam, hingga heningnya dipecahkan"

    # 1: Perbincangan Awal: 1
    show mystery cewe at right with moveinright 
    mystery "Mas...."

    # 1: Breaking the silence: 2
    scene bg_rumah2 with dissolve
    show raka_normal_depan at left
    show tetangga at right with moveinright
    tetangga "Mas nyari Pak Ardi ya?"
    menu:
        "Iya, Bu":
            tetangga "Pak Ardi sudah pergi mas, tiga hari lalu. Bawa koper, buru-buru. Saya tanya mau ke mana, dia cuma bilang… mau lihat Jam Gadang lagi sebelum tua"
        "Beliau benar tinggal di sini?":
            tetangga "Iya, tapi sudah pergi, tiga hari lalu. Bawa koper, buru-buru. Saya tanya mau ke mana, dia cuma bilang… mau lihat Jam Gadang lagi sebelum tua"

    menu:  
        "Jam Gadang?":
            tetangga "Iya, katanya punya kenangan di sana. Nggak ngerti juga maksudnya"

    # 1: Breaking the silence: 3
    raka "Baiklah, kalau begitu aku harus bergegas menuju ke kota dimana Jam Gadang berada!"

    #1: pindah kota
    "Pilih kota yang harus dituju Raka"
    menu:
        "menuju ke Kota Bukittinggi":
            jump Bukittinggi
        "menuju ke Kota Medan":
            raka "permisi pak, bapak tau Jam Gadang ada di mana?"
            mystery "waduh dik, jam gadang mana yag ada di medan"
            scene bg_kalah with Dissolve(15.0)
        "menuju ke Kota Palembang":
            "belajar geografi lagi ya dik"
            scene bg_kalah with Dissolve(15.0)

    # This ends the game.
    return

# LEVEL 1 ----------
label Bukittinggi:
    scene bg_kage2 with Dissolve(5.0)
    # 2: deskripsi bukittinggi
    scene bg_bukittinggi

    # 2: looking for a clue
    scene bg_jamGadang
    "Setelah melakukan perjalanan selama 2 hari, dengan punggung pegal, Raka tiba. Berdiri di pelataran Jam Gadang, menatap menara putih yang kokoh, jarumnya menunjuk waktu yang tak peduli pada keributan manusia di sekitarnya."
    scene bg_notebook
    "Raka membuka buku catatannya yang berisikan ciri-ciri pak ardi. Umur sekitar 50-an, rambut sedikit beruban dan klimis, sering pakai kemeja batik warna gelap, nada bicara halus, suka membawa tas jinjing kulit."

    # 2: looking for a clue #2


    # 2: asking local

    # 2: pindah kota
    menu:
        "Pergi ke Malang":
            jump Malang
        "Pergi ke Blitar":
            scene bg_kalah with Dissolve(15.0)
        "Pergi ke Magelang":
            scene bg_kalah with Dissolve(15.0)
    

    return

label Malang:
    scene bg_kage3 with Dissolve(5.0)


    return

label Jayapura:
    return

label Pamekasan:
    return

# LEVEL 2 ----------
label Palembang:
    return

label Magelang:
    return

label Surabaya:
    return 

label Yogyakarta:
    return 

# LEVEL 3 ----------
label Batam:
    return 

label Balikpapan:
    return 

label Manado:
    return

#FINALE
label Jakarta:
    return