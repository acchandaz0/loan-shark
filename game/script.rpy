# The script of the game goes in this file.
# The game starts here.

# LEVEL 1 ----------
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
    show raka normal depan at left
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

label Bukittinggi:
    scene bg_kage2 with Dissolve(5.0)

    # 2: deskripsi bukittinggi
    scene 17 with dissolve
    "Bukittinggi adalah sebuah kota di provinsi Sumatera Barat, yang terletak di Dataran Tinggi Minangkabau. Dikenal dengan iklimnya yang sejuk dan pemandangan alamnya yang menakjubkan"
    "Bukittinggi terkenal dengan arsitekturnya yang unik, terutama rumah-rumah tradisional Minangkabau dengan atapnya yang berbentuk tanduk kerbau. Jam Gadang (Menara Jam Gadang) di kota ini adalah landmark yang terkenal." 
    "Bukittinggi juga merupakan pusat budaya bagi masyarakat Minangkabau, dengan warisan tarian, musik, dan kuliner tradisional yang kaya. "

    # 2: looking for a clue
    scene bg_13 with dissolve
    "Setelah melakukan perjalanan selama 2 hari, dengan punggung pegal, Raka tiba."
    show raka bahagia belakang
    raka "YEY AKHIRNYA SAMPAI"
    scene 14 with dissolve
    "Raka membuka buku catatannya yang berisikan ciri-ciri pak ardi. Umur sekitar 50-an, rambut sedikit beruban dan klimis, sering pakai kemeja batik warna gelap, nada bicara halus, suka membawa tas jinjing kulit."

    # 2: looking for a clue #2
    scene 15 with dissolve
    show raka bertanya depan
    "Raka membuka buku catatannya yang berisikan ciri-ciri pak ardi. Umur sekitar 50-an, rambut sedikit beruban dan klimis, sering pakai kemeja batik warna gelap, nada bicara halus, suka membawa tas jinjing kulit."

    # 2: asking local
    scene 16 with dissolve
    show raka normal depan at left
    menu:
        "Permisi bu..":
            show penjual_souvenir at right with moveinright
            penjual_souvenir "cari apa bang? murah nyo disini"

    show penjual_souvenir at right

    menu:
        "Tas yang disitu ada warna lain bu?":
            penjual_souvenir "ndak ada warna lain do bang, sama pulak kau kyk orang aneh satutu minggu lalu ha, ndak ada yg lain tp maksa pulak dia"
            raka "orang aneh?"
            penjual_souvenir "iyo, baju cakap orang mau ke nikahan tp datangnyo ke jam gadang. Rambut klimis pake batik lengan panjang"
        "Saya mau cari orang bu...":
            penjual_souvenir "mana den ingat macam itu. Banyak orang lewat sini"
            raka "tapi orangnya eksentrik bu… rambut klimis, pakai batik juga biasanya"
            penjual_souvenir "oh bapak itu?"

    penjual_souvenir "kemarin tu orang maksa kali dia cari tas warna lain dan buat ribut pulak satu orang itu"
    menu:
        "ibu ingat tidak apa lagi yang orang itu bilang?":
            penjual_souvenir "hmm, kayaknya ada satu hal aneh yang dia ucap"

    menu:
        "itu! Ibu ingat dia bilang apa?":
            penjual_souvenir "kalau tak salah…. Bulat-bulat... Oh Bakso!"

    menu:
        "bakso?":
            penjual_souvenir "saya sudah tak ingat lagi lah bang.."
        "selain bakso, orang itu berkata apa lagi bu??":
            penjual_souvenir "sudah tak ingat lah bang"

    raka "terima kasih ya bu..."

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
    scene bg_Level1_Chapter3 with Dissolve(5.0)

    # 3: deskripsi malang
    scene 18 with dissolve
    "Malang adalah kota yang menawan di Jawa Timur, Indonesia, yang terkenal dengan iklimnya yang sejuk, arsitektur era kolonial, dan lingkungan pegunungan yang indah. "
    "Kota ini merupakan tujuan populer bagi pecinta alam dan penggemar sejarah, dan juga merupakan rumah bagi beberapa universitas terkemuka, sehingga memberikan suasana pelajar yang hidup."
    "Kuliner lokal Malang terkenal dengan Bakso Malang, yang menjadikannya makanan favorit di kalangan penduduk lokal dan pengunjung."

    return

label Jayapura:
    scene bg_Level1_Chapter4 with Dissolve(5.0)
    return

label Pamekasan:
    scene bg_Level1_Chapter5 with Dissolve(5.0)
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