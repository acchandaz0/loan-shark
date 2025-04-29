# The script of the game goes in this file.
# The game starts here.

# LEVEL 1 ----------
label start:
    # 1:World Building #1
    play music "opening.mp3"
    scene bg_chp1 with Dissolve(5.0)
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
    "Rumah kontrakan yang kosong dan berantakan, seolah penghuninya melarikan diri dengan terburu-buru" #(bg reveal)
    
    # 1: Anxious #3
    scene bg_rumah1
    "Ia terdiam, hingga heningnya dipecahkan"

    # 1: Perbincangan Awal: 1
    show tetangga at right with moveinright 
    stop music fadeout(2.0)
    play music "conversation.mp3" fadein(1.0) loop
    mystery_cewe "Mas...."

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
    stop music fadeout(2.0)
    #1: pindah kota
    "Pilih kota yang harus dituju Raka"
    menu:
        "menuju ke Kota Bukittinggi":
            jump Bukittinggi
        "menuju ke Kota Medan":
            scene black
            raka "permisi pak, bapak tau Jam Gadang ada di mana?"
            mystery_cowo "waduh dik, jam gadang mana yag ada di medan"
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)
        "menuju ke Kota Palembang":
            scene black
            "belajar geografi lagi ya dik"
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)

    # This ends the game.
    return

label Bukittinggi:
    scene bg_chp2 with Dissolve(5.0)

    # 2: deskripsi bukittinggi
    play music "cinematic.mp3" loop
    scene 17 with dissolve
    "Bukittinggi adalah sebuah kota di provinsi Sumatera Barat, yang terletak di Dataran Tinggi Minangkabau. Dikenal dengan iklimnya yang sejuk dan pemandangan alamnya yang menakjubkan"
    "Bukittinggi terkenal dengan arsitekturnya yang unik, terutama rumah-rumah tradisional Minangkabau dengan atapnya yang berbentuk tanduk kerbau. Jam Gadang (Menara Jam Gadang) di kota ini adalah landmark yang terkenal." 
    "Bukittinggi juga merupakan pusat budaya bagi masyarakat Minangkabau, dengan warisan tarian, musik, dan kuliner tradisional yang kaya. "

    # 2: looking for a clue
    scene 13 with dissolve
    "Setelah melakukan perjalanan selama 2 hari, dengan punggung pegal, Raka tiba."
    show raka bahagia belakang
    raka "YEY AKHIRNYA SAMPAI"

    # 2: looking for a clue #2
    scene 14 with dissolve
    "Raka membuka buku catatannya yang berisikan ciri-ciri pak ardi. Umur sekitar 50-an, rambut sedikit beruban dan klimis, sering pakai kemeja batik warna gelap, nada bicara halus, suka membawa tas jinjing kulit."

    scene 15 with dissolve
    show raka bingung depan
    "Raka menyusuri area sekitar menara, memperhatikan pedagang dan pengunjung. Matanya berhenti pada seorang pedagang yang menjual banyak jenis souvenir. Banyaknya jenis souvenir bisa-bisa membuatmu pusing hanya dengan berada di sana."

    stop music fadeout(0.5)
    # 2: asking local
    scene 16 with dissolve
    play music "conversation.mp3" fadein(1.0) loop
    show raka normal depan at left
    menu:
        "Permisi bu..":
            show penjual souvenir at right with moveinright
            penjual_souvenir "cari apa bang? murah nyo disini"

    show penjual souvenir at right

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
    stop music fadeout(0.5)
    
    # 2: pindah kota
    menu:
        "Pergi ke Malang":
            jump Malang
        "Pergi ke Blitar":
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Magelang":
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)
    
    return

label Malang:
    scene bg_chp3 with Dissolve(5.0)

    # 3: deskripsi malang
    play music "cinematic.mp3" loop
    scene 18 with dissolve
    "Malang adalah kota yang menawan di Jawa Timur, Indonesia, yang terkenal dengan iklimnya yang sejuk, arsitektur era kolonial, dan lingkungan pegunungan yang indah. "
    "Kota ini merupakan tujuan populer bagi pecinta alam dan penggemar sejarah, dan juga merupakan rumah bagi beberapa universitas terkemuka, sehingga memberikan suasana pelajar yang hidup."
    "Kuliner lokal Malang terkenal dengan Bakso Malang, yang menjadikannya makanan favorit di kalangan penduduk lokal dan pengunjung."

    # 3: After the rain
    scene 19 with dissolve
    "Hujan baru saja reda saat Raka turun dari angkot terakhirnya. Kabut tipis masih menggantung rendah di atas aspal, meninggalkan aroma tanah basah yang bercampur dengan wangi bensin."
    "Jalanan utama cukup ramai, motor, mobil, dan ojek berseliweran seperti parade tak resmi."

    # 3: after the rain #2
    scene 20 with dissolve
    "Begitu Raka berbelok memasuki jalan pintas, suara klakson memudar, digantikan suara sepatu menapak genangan dan desau angin yang menyusup lewat sela ranting."
    
    # 3: topeng
    scene 21 with dissolve
    "Di jalan, Raka menemui posko dengan beberapa topeng yang bergantung di dinding anyaman."

    # 3: asking local
    scene 22 with dissolve
    "Gerobak bakso terlihat di ujung jalan. Asap mengepul, suara kuah mendidih bersahutan dengan obrolan pelanggan."
    stop music fadeout(0.5)
    play music "conversation.mp3" fadein(1.0) loop
    show raka normal depan at left with moveinleft
    show penjual bakso at right with dissolve
    menu:
        "bakso 1 porsi pak":
            penjual_bakso "disini ga dijual per porsi mas… masnya pilih aja nanti tak itung e berapa"
        "tumbas pak":
            penjual_bakso "monggoo"

    menu:
        "pentol kasar 1, pentol alus 2, tahu 1, bihun 1":
            penjual_bakso "ga nambah pentol jumbo a mas?"
        "gorengan 1, bihun 1":
            penjual_bakso "ga nambah pentol jumbo a mas?"

    menu:
        "ga dulu pak, kolesterol hehe":
            penjual_bakso "yowala jaman sekarang anak muda pada suka diet yo.."
            raka "oiya pak, pernah lihat bapak2 agak tua yang udah beruban dan rambutnya klimis?"
        "hehe":
            raka "oiya pak, pernah lihat bapak2 agak tua yang udah beruban dan rambutnya klimis?"

    penjual_bakso "Iya! Dia datang waktu hujan, duduk di situ."
    penjual_bakso "Dia makan pelan sekali, terus bilang, \"Bakso ini, rasanya kurang kenyal\" terus saya balas, \"ya kan ini ga ada pengawetnya!\" gitu"

    menu:
        "Bapak tau ke mana dia pergi setelah itu?":
            penjual_bakso "Nggak bilang jelas. Tapi sebelum pergi, dia minta maaf dan bilang kalau kata-katanya tadi yang dia maksud itu papeda"

    raka "papeda?...."
    stop music fadeout(0.5)
    menu:
        "Pergi ke Samarinda":
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Jayapura":
            jump Jayapura
        "Pergi ke Bogor":
            play music "kalah.mp3"
            scene bg_kalah with Dissolve(25.0)

    return

label Jayapura:
    scene bg_chp4 with Dissolve(5.0)

    # 4: deskripsi jayapura
    play music "cinematic.mp3" loop
    scene 23 with dissolve
    "Jayapura adalah ibu kota Provinsi Papua yang terletak di bagian paling timur Indonesia. "
    "Terletak di antara perbukitan dan garis pantai Pasifik, Jayapura dikenal dengan keindahan alamnya yang memukau, dengan panorama laut dan lanskap hijau yang subur. "
    "Sebagai pintu gerbang ke Papua, kota ini memadukan tradisi lokal Papua dengan pembangunan modern. Jayapura memainkan peran penting dalam pemerintahan daerah dan pendidikan,"
    "dan berfungsi sebagai jembatan budaya antara masyarakat asli Papua dan daerah lain di Indonesia. Hidangan lokal yang terkenal adalah Papeda, bubur sagu lengket yang biasanya disajikan "

    # 4: explore
    scene 24 with dissolve
    "Kota ini cukup ramai, namun tidak sampai membuat suasana terasa sesak. Lalu lintas berjalan padat namun teratur. Bunyi klakson terdengar sesekali, namun tidak mendominasi." 
    "Raka duduk di sebuah bangku beton di dekat taman kecil. Ia melepas tas dari bahunya dan menyandarkan tubuh, mencoba mengusir lelah yang mulai menumpuk setelah perjalanan yang tidak sebentar."

    "Ia mencium aroma yang asing namun familiar. Sebuah campuran gurih dan asam yang menggoda selera. Saat menoleh, ia melihat sebuah gerobak sederhana dengan panci besar berisi papeda."
    "Di belakang gerobak, berdiri seorang pria sibuk menuangkan sagu ke dalam mangkuk."

    # 4: asking local
    scene 25 with dissolve
    stop music fadeout(0.5)
    play music "conversation.mp3" fadein(1.0) loop
    "Raka menghampiri dan duduk di kursi plastik yang tersedia."

    show raka normal depan at left with moveinleft
    raka "Papeda satu, Pak."

    menu:
        "Bapak pernah lihat orang dengan umur sekitar 50-an, rambut klimis, kemeja batik gelap, suka manggil \"Mas\" ke semua orang?":
            "Pedagang itu mengerutkan dahi sejenak, lalu mengangguk."

    show penjual papeda at right with moveinright
    penjual_papeda "Iya. Dia makan di sini minggu lalu."
    penjual_papeda "Saya sempat bingung apa ada acara di dekat sini ya? Orang itu pakai baju rapi"

    menu:
        "Dia sempat bilang mau kemana tidak pak?":
            "Sebelum pergi, dia bilang satu hal yang buat saya bingung. Dia cerita banyak tentang wayang lalu tiba tiba bilang ingin lihat karapan sape itu"

    raka "karapan sapi ya pak?"
    penjual_papeda "iya dek"
    stop music fadeout(0.5)

    menu:
        "Pergi ke Pamekasan":
            jump Pamekasan
        "Pergi ke Ponorogo":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Jambi":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)

    return

label Pamekasan:
    scene bg_chp5 with Dissolve(5.0)

    # 5: deskripsi Pamekasan
    play music "cinematic.mp3" loop
    scene 28 with dissolve
    "Madura adalah sebuah pulau yang terletak di lepas pantai timur laut Jawa, dan merupakan bagian dari Provinsi Jawa Timur di Indonesia. "
    "Dikenal dengan budayanya yang berbeda dan tradisi yang membanggakan, Madura sangat terkenal dengan Karapan Sapi, sebuah acara yang semarak dan kompetitif yang menarik perhatian penduduk lokal dan wisatawan. "
    "Pulau ini memiliki karakter maritim yang kuat, dengan banyak penduduknya yang terlibat dalam penangkapan ikan dan pertanian garam. Dalam hal makanan, Sate Madura adalah yang paling terkenal"

    # 5: karapan sapi
    scene 29 with dissolve
    "Langit Madura menjelang sore tampak pucat keemasan, dan tanah lapang di pinggiran kota dipenuhi teriakan penonton, deru lonceng, serta semangat yang hampir bisa disentuh. Raka berdiri di antara kerumunan, menyaksikan karapan sapi pertama dalam hidupnya." 
    "Sepasang sapi berlomba di atas lintasan lumpur, ditunggangi joki kurus bersarung yang tampak lebih seperti penari daripada pembalap."

    "Namun ketika perlombaan selesai dan lapangan mulai kosong, semangatnya mulai luntur. Tidak ada tanda-tanda Pak Ardi."
    "Raka memutuskan untuk meninggalkan kota tersebut, perlahan berjalan menuju terminal bus antarkota yang tidak jauh dari pusat kota. Angin laut terasa lebih lembut di sore hari, dan suara pelan azan magrib mulai menggema."

    
    # 5: bus stop
    scene 30 with dissolve
    "Di halte yang sunyi, Raka duduk sendiri. Ia membuka bungkus air mineral, meneguk seteguk besar, dan mencoba berdamai dengan rasa kecewa."

    stop music fadeout(0.5)
    play music "pak_ardi.mp3"
    # 5: pak ardi
    scene 31 with dissolve
    "Namun tiba-tiba—seperti sulap yang tidak lucu—seorang pria yang sangat dikenalnya muncul dari tikungan: Pak Ardi."
    "Raka membeku. Napasnya tertahan. Ia segera bangkit dan melangkah cepat."

    raka "Pak Ardi!"

    "Pak Ardi terkejut. Matanya membelalak, dan dalam sepersekian detik, ia berlari menuju bus yang baru datang. Tanpa sepatah kata pun, tanpa menoleh ke belakang."

    "Raka mengejar, namun hanya sempat mencapai pintu bus saat kendaraan itu sudah mulai melaju."
    stop music

    "Masih terengah, Raka menghampiri orang yang juga sedang menunggu bus selanjutnya."

    # 5: acceptance
    menu:
        "Pak, bus itu tujuannya ke mana?":
            "Itu bus menuju arah barat, Mas. Biasanya orang naik itu kalau mau jalan jalan ke Sungai Musi"

    menu:
        "Pergi ke Surabaya":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Banten":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Palembang":
            jump Palembang
            
    return

# LEVEL 2 ----------
label Palembang:
    scene bg_chp6 with Dissolve(5.0)

    # 1: deskripsi Palembang
    play music "cinematic.mp3" loop
    scene 33 with dissolve
    "Palembang adalah ibu kota Provinsi Sumatera Selatan dan salah satu kota tertua di Indonesia, dengan sejarah yang berawal dari Kerajaan Sriwijaya yang kuat. Terletak di sepanjang Sungai Musi, Palembang sering disebut sebagai “Venesia dari Timur” karena banyaknya jembatan dan jalur air."
    "Jembatan Ampera sebagai landmark yang paling ikonik. Kota ini juga merupakan pusat budaya dan warisan Melayu. Kuliner khas Palembang adalah Pempek."
   
    # 1: stroling around
    scene 34 with dissolve
    "Langit mulai terang saat Raka menjejakkan kaki di tepi Sungai Musi. Cahaya matahari makin lama makin menyilaukan, sementara Jembatan Ampera berdiri megah membelah aliran sungai yang tampak tenang namun penuh cerita."

    "Suasana kota ini terasa berbeda. Laju hidupnya tidak terburu-buru, tetapi tak pernah benar-benar diam. Deru perahu sungai bercampur dengan suara klakson, dan aroma pempek yang menguar dari warung pinggir jalan membuat perut Raka mulai memberontak."

    "Namun perhatiannya teralihkan saat ia melihat seorang pria berambut ikal sebahu, mengenakan jaket kulit lusuh dan celana kargo kuning terang—benderang, sementara di tangannya memegang kamera analog. Ia memotret kapal yang sedang melintas di bawah Ampera"
    
    "Raka mendekat"
    
    stop music fadeout(0.5)
    play music "conversation.mp3" loop

    show raka bertanya depan at left with moveinleft
    menu:
        "Motret buat majalah fashion atau buat bukti pajak, mas?":
            mas_fotografer "Wah, dua-duanya bisa. Yang penting cahaya bagus dan objeknya nggak kabur."
        "Lagi ngapain mas?":
            mas_fotografer "lagi merancang ulang UUD 1945 hehe.... (memotret)"

    "Mereka tertawa ringan. Setelah obrolan singkat soal lensa, film, dan harga cuci cetak yang makin naik, Raka menanyakan tentang Pak Ardi."

    scene 34
    show raka normal depan at left 
    show mas fotografer at right
    mas_fotografer "Hmm… Tunggu sebentar."

    "Pria itu membuka galeri kamera film yang telah dicetak, memperhatikan lembar demi lembar, hingga akhirnya menunjuk satu foto."

    mas_fotografer "Ini! Saya nggak yakin, tapi waktu itu saya jepret toko rokok pinggir jalan. Lihat tuh—di pojok kiri."

    "Raka mendekat."

    raka "Itu dia…"

    "Pak Ardi, berdiri di depan sebuah toko kecil, seperti biasa, rambut klimis dan batik lengan panjang yang tampak terlalu semangat untuk dipakai di suhu 30 derajat."

    raka "Toko ini di mana, Mas?"
    mas_fotografer "Masih di daerah sini. Dekat gang kecil arah pasar. Penjualnya nenek-nenek, jual rokok dan jajanan."

    "Raka mengucapkan terima kasih dan segera menuju tempat yang dimaksud." 

    # 1: tabakoya
    scene 35 with dissolve
    "Raka menemukan toko itu dengan mudah—sebuah warung mungil berdinding kayu, dengan deretan bungkus rokok tergantung di tali rafia."
    "Di dalamnya, seorang nenek duduk sambil membaca majalah gosip edisi 2016."

    show raka normal depan at left
    raka "Permisi, Nek. Saya sedang mencari seseorang."
    show nenek rokok at right
    tabakoya "Kalau nyari jodoh, nenek sudah pensiun, Nak."
    raka "Bukan, Nek. Orang ini... (menjelaskan ciri-ciri Pak Ardi)"
    "Nenek itu memicingkan mata, lalu tertawa kecil."
    tabakoya "Oh, yang bajunya norak itu? Iya, sempat mampir kemarin-kemarin. Beli rokok kretek dua bungkus, bilang mau cari inspirasi."
    raka "Inspirasi ke mana, Nek?"
    tabakoya "Katanya… dia ingin melihat kemegahan Borobudur. Katanya, candi itu bisa bikin siapa pun merasa kecil, termasuk ego sendiri."

    # 1: hitorigoto
    stop music fadeout(0.5)
    play music "cinematic.mp3"
    scene 36 with dissolve
    "Raka mencatat dalam hati. Satu tempat lagi, satu langkah lebih dekat."

    "Ia menunduk memberi hormat pada sang nenek, lalu berjalan keluar, melewati Jembatan Ampera yang kini mulai dipadati kendaraan. Angin dari sungai berembus lebih kencang, seakan mendorongnya untuk segera melangkah."

    
    menu:
        "Pergi ke Surabaya":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Yogyakarta":
            play music "kalah.mp3"
            scene bg_black
            "Gue kecewa sob..."
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Magelang":
            jump Magelang


    return

label Magelang:
    scene bg_chp7 with Dissolve(5.0)

    # 2: deskripsi Magelang
    play music "cinematic.mp3" loop
    scene 38 with dissolve
    "Magelang adalah sebuah kota di Jawa Tengah, Indonesia, yang terkenal dengan suasananya yang tenang dan pemandangannya yang indah. Dikelilingi oleh perbukitan dan persawahan yang subur, kota ini juga merupakan rumah bagi Candi Borobudur, situs Warisan Dunia UNESCO dan salah satu monumen Budha paling ikonik di dunia." 
    "Magelang menawarkan perpaduan antara keindahan alam dan kedalaman sejarah, menjadikannya tujuan wisata budaya yang signifikan di wilayah ini."


    # 2: bumped
    scene 39 with dissolve
    "Sesampainya di kompleks Candi Borobudur, Raka terpaku. Di tengah riuh pengunjung yang sibuk berfoto dan mendaki, ia berdiri membeku seperti patung. Kepalanya menengadah, menatap kemegahan batu-batu tua yang tersusun membentuk cerita zaman lampau."

    "Belum sempat ia melangkah lebih jauh, tiba-tiba—"
    stop music
    "BRUAKKKKKKK"

    "Seorang anak kecil dengan kaus bergambar kartun dinosaurus menangis setelah menabrak Raka. Di tangannya, kini hanya ada cone kosong. Es krimnya sudah berpulang ke bumi."
    "Huaaaaaaaaaa eskrimku jaaaaatuuuhhhh hhuweeeeeeee!!!"
    "Waduh, maaf banget, Dek. Kakak yang kurang awas. Sini, kakak beliin lagi."

    # 2: ice cream
    scene 40 with dissolve
    play music "conversation.mp3" loop

    "Beberapa menit kemudian, setelah membeli es krim, sang anak kini lebih tenang, menjilat es krim baru dengan semangat nasionalisme yang tinggi."
    show bocil at right with dissolve
    bocil "Kakak baik deh, gak kayak bapak-bapak menyeramkan beberapa hari lalu..."
    show raka bingung depan at left
    raka "Bapak-bapak menyeramkan?"
    bocil "Iya. Temanku waktu itu nabrak dia. Terus dia marah-marah sambil ngomel aneh."
    scene 40
    show raka normal depan at left
    show bocil at right
    raka "Ngomel apa?"

    "Anak itu menirukan dengan ekspresi serius, menekankan setiap kata"

    bocil "\"Kalian kalau nakal dan suka balapan gitu, nanti ku masak jadi lontong balap, baru tahu rasa!\" gitu :("

    "Raka menahan tawa, walau dalam hati ia merasa merinding. Itu terdengar seperti sesuatu yang sangat mungkin dikatakan Pak Ardi. Apalagi jika sedang kesal dan dramatis."

    raka "Itu saja?"
    bocil "Iya!"
    "Anak itu mengangguk mantap, lalu kembali fokus pada es krimnya."

    raka "Terima kasih, ya. Es krimmu tadi... jadi petunjuk yang berharga."
    bocil "Kakak detektif ya?"
    raka "Belum tentu. Tapi yang jelas… aku sedang memburu lontong balap."

    stop music fadeout(0.5)
    menu:
        "Pergi ke Surabaya":
            jump Surabaya
        "Pergi ke Surakarta":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)
        "Pergi ke Semarang":
            play music "kalah.mp3"
            scene bg_black
            scene bg_kalah with Dissolve(25.0)

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