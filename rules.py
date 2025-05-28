from datetime import datetime

def get_time_based_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Selamat pagi"
    elif 12 <= hour < 17:
        return "Selamat siang"
    elif 17 <= hour < 21:
        return "Selamat sore"
    else:
        return "Selamat malam"

def chatbot_response(message):
    message = message.lower()

    # Salam Sapaan untuk user
    if any(greeting in message for greeting in ["halo", "hai", "haii", "haloo", "hello", "halo tapin", "hallo tapin", 
                                                "hai tapin", "haii tapin", "helo tapin", "hello tapin"]):
        return f"{get_time_based_greeting()}, halo juga! Ada yang bisa saya bantu seputar PT Pindad?"

    elif "selamat pagi" in message:
        return "Selamat pagi juga! Semoga harimu menyenangkan. Ada yang bisa saya bantu seputar PT Pindad?"
    elif "selamat siang" in message:
        return "Selamat siang juga! Semoga harimu lancar ya. Ada yang bisa saya bantu seputar PT Pindad?"
    elif "selamat malam" in message:
        return "Selamat malam juga! Ada yang ingin ditanyakan sebelum istirahat?"
    
    # Perusahaan PT Pindad
    elif "perusahaan" in message and "pindad" in message:
        return (
            "PT Pindad adalah anak usaha Len Industri yang bergerak di bidang produksi Kendaraan dan peralatan pertahanan."
            "Perusahaan ini memiliki dua pabrik, yakni di Bandung (tempat produksi senjata, kendaraan khusus, dan mesin industrial) dan di Turen (tempat produksi munisi dan bahan peledak komersial)."
            "Untuk mendukung kegiatan bisnisnya, perusahaan ini pun memiliki dua kantor perwakilan di Jakarta."
            "Perusahaan ini merupakan salah satu perusahaan tertua di Indonesia (menurut keberlanjutan usaha) yang masih tetap berdiri sampai sekarang dan merupakan satu-satunya perusahaan manufaktur pertahanan di Indonesia."
        )

    # Sejarah PT Pindad
    elif "sejarah" in message and "pindad" in message:
        return (
            "Sejarah PT Pindad dimulai pada tahun 1808 ketika Gubernur Jenderal Hindia Belanda, Herman Willem Daendels,"
            "mendirikan bengkel senjata bernama Constructie Winkel (CW) di Surabaya. CW kemudian berkembang dan berubah nama menjadi Artilerie Constructie Winkel (ACW) pada 1851,"
            "yang mencakup produksi senjata, munisi, dan laboratorium penelitian. Pada masa Perang Dunia I, pemerintah Hindia Belanda memindahkan unit-unit penting ACW ke Bandung karena dinilai lebih aman dan strategis.\n\n"
            "Setelah relokasi selesai antara tahun 1918 hingga 1932, unit-unit tersebut digabung menjadi Artilerie Inrichtingen (AI)."
            "Saat pendudukan Jepang, nama-nama unitnya diubah ke dalam bahasa Jepang. Setelah kemerdekaan Indonesia, pada 9 Oktober 1945, AI diambil alih oleh para pejuang Indonesia dan diubah namanya menjadi Pabrik Senjata Kiaracondong.\n\n"
            "Pada masa Agresi Militer Belanda, pabrik ini dibagi menjadi dua bagian: Leger Produktie Bedrijven (LPB) dan Central Reparatie Werkplaats."
            "Setelah Konferensi Meja Bundar tahun 1949, LPB diserahkan ke pemerintah Indonesia dan menjadi Pabrik Senjata dan Mesiu (PSM) di bawah pengelolaan TNI AD."
            "PSM berhasil memproduksi laras senjata dan terus berkembang meski kekurangan tenaga ahli. Pada tahun 1958, namanya diubah menjadi Pabal AD, lalu pada tahun 1962 menjadi Perindustrian Angkatan Darat (Pindad)."
            "Pindad mulai memproduksi senjata secara massal dan menjadi pemasok utama senjata TNI. Pada 1972, perusahaan ini berubah lagi menjadi Kopindad,\n\n"
            "namun setelah beberapa kendala dalam Operasi Seroja, Kopindad kembali menjadi Pindad pada tahun 1976."
            "Karena keterbatasan sebagai bagian dari TNI, pada 1983 status Pindad diubah menjadi perseroan terbatas agar lebih fleksibel."
            "Terakhir, pada 12 Januari 2022, pemerintah menyerahkan mayoritas saham Pindad ke Len Industri sebagai bagian dari pembentukan holding BUMN pertahanan."
        )
    
    # Alamat & Kontak Rumah Sakit Pindad – letakkan ini lebih atas
    elif ("alamat" in message or "kontak" in message) and ("rsu" in message or "rumah sakit" in message or "sakit" in message):
        return (
            "Alamat dan Kontak Rumah Sakit Umum (RSU) Pindad Bandung:\n"
            "PT Pindad Medika Utama RSU Pindad Bandung, Jl. Gatot Subroto No.517, Sukapura, Kec. Kiaracondong, Kota Bandung, Jawa Barat 40285 "
            "Informasi : (022) 732-2877 IGD : (022) 77322877 EXT Whatsapp : +6282115796951 humas@rsupindad.com"
        )
    
    # Lokasi PT Pindad
    elif "lokasi" in message and "pt" in message or "alamat" in message and "pindad" in message:
        return (
            "PT Pindad memiliki dua lokasi pabrik utama. Pabrik pertama berada di Bandung, Jawa Barat, untuk produksi senjata, "
            "kendaraan khusus, dan mesin industrial. Pabrik kedua berada di Turen, Malang, Jawa Timur, "
            "yang khusus memproduksi munisi dan bahan peledak komersial. Selain itu, PT Pindad juga memiliki kantor cabang bersama "
            "(NDHI Group) di Jakarta Selatan, Menara MTH lantai 7. Berikut rincian lebih lanjut:\n"
            "- Bandung: Gatot Subroto, No. 517, Bandung, Indonesia.\n"
            "- Turen, Malang: Bromo No. 5, Turen, Malang, Indonesia.\n"
            "- Jakarta: Jalan MT. Haryono Kav 23, Menara MTH lantai 7, Jakarta Selatan."
        )

    # Produk PT Pindad
    elif "produk" in message and "pindad" in message or "hasil" in message and "pindad" in message:
        return (
            "PT Pindad memproduksi berbagai alat utama sistem pertahanan seperti:\n"
            "- Senjata ringan (SS1, SS2, SPR),\n"
            "- Amunisi berbagai kaliber,\n"
            "- Kendaraan taktis seperti Maung, Komodo, dan Anoa,\n"
            "- Alat berat seperti ekskavator dan traktor untuk sektor sipil dan militer."
        )

    # Mobil Maung PT Pindad
    elif "maung" in message or ("kendaraan" in message and "taktis" in message):
        return (
            "Maung adalah kendaraan taktis ringan buatan PT Pindad yang dirancang untuk operasi militer dan mobilitas tinggi."
            "Diperkenalkan pertama kali tahun 2020, Maung digunakan oleh TNI dan juga tersedia versi sipil terbatas."
            "Dilengkapi dengan kemampuan off-road, modular, dan bisa dipasangi senjata ringan.\n\n"
            "Kecepatan mobil Maung 120 km/jam, transmisi manual 6 speed dan mampu menjangkau jarak tempuh hingga 800 km, "
            "menjadikan Maung memiliki manuver yang gesit dan handal. Maung dapat dilengkapi dengan braket senjata 7,62 mm, "
            "konsol senjata SS2-V4, GPS navigasi, tracker dan perlengkapan lainnya."
        )

    # Berkunjung PT Pindad
    elif "berkunjung" in message or ("mengunjungi" in message and "pt pindad" in message):
        return (
            "Jika anda ingin berkunjung dan melihat produksi PT Pindad secara langsung, maka terdapat peraturan berkunjung seperti:\n\n"
            "- Pengunjung tidak diperkenankan membawa senjata tajam, senjata api, dan barang barang berbahaya lainnya.\n\n"
            "- Pengunjung tidak diizinkan untuk mendokumentasikan proses produksi dengan menggunakan kamera, handycam, telepon genggam & gawai fotografi lainnya, kecuali di area yang sudah ditentukan/diperbolehkan.\n\n"
            "- Untuk alasan keselamatan, para pengunjung diwajibkan mengikuti peraturan dan ketentuan perusahaan.\n\n"
            "- Jika saat berkunjung terdengar suara sirine yang terputus-putus, pengunjung harus waspada, pertanda terjadinya kondisi tidak aman.\n\n"
            "- Pada kondisi tersebut, pengunjung diharapkan tetap tenang dan jangan panik. Ikuti petunjuk arah 'EXIT'.\n\n"
            "- Pengunjung wajib mengikuti instruksi keselamatan saat mencoba produk.\n\n"
            "- Pengunjung yang merasa kurang sehat bisa menuju kotak P3K, poliklinik, atau dirujuk ke RS Pindad.\n\n"
            "- Selalu berjalan di jalur pejalan kaki dan tidak melewati garis kuning di area produksi."
        )

    # Melamar Kerja PT Pindad
    elif "melamar" in message or ("kerja" in message and "pindad" in message):
        return (
            "Untuk melamar ke PT Pindad, Anda perlu mendaftar melalui website resmi mereka di www.pindad.com dan e-career.pindad.com. "
            "Anda perlu mengisi formulir pendaftaran, melampirkan pas foto, ijazah, transkrip, sertifikat TOEFL (jika ada), dan fotokopi KTP. "
            "Pastikan untuk mengikuti prosedur rekrutmen yang resmi dan berhati-hati terhadap penipuan yang mengatasnamakan PT Pindad. Berikut langkah-langkah lebih detail:\n\n"
            "1. Kunjungi Website Resmi:\n"
            "- Buka website PT Pindad di www.pindad.com.\n" 
            "- Cari bagian rekrutmen atau 'Career'.\n" 
            "- Biasanya, ada tautan untuk pendaftaran atau formulir lamaran online.\n\n" 
            "2. Daftar dan Isi Formulir:\n"
            "- Jika ada formulir online, isi dengan data diri Anda yang lengkap dan benar.\n"
            "- Pastikan untuk melampirkan semua dokumen yang diperlukan, seperti pas foto berwarna, ijazah, transkrip, sertifikat TOEFL (jika ada), dan fotokopi KTP.\n\n"
            "3. Periksa Syarat dan Ketentuan:\n"
            "- Periksa persyaratan khusus untuk setiap posisi yang dilamar.\n"
            "- Pastikan Anda memenuhi kualifikasi yang diminta.\n\n"
            "4. Simpan dan Kirim:\n"
            "- Setelah mengisi formulir dan melampirkan semua dokumen, simpan lamaran Anda.\n"
            "- Kirimkan lamaran melalui saluran yang ditentukan di website resmi.\n\n"
            "5. Waspada Penipuan:\n"
            "- PT Pindad mengingatkan masyarakat untuk berhati-hati terhadap penipuan rekrutmen yang mengatasnamakan perusahaan.\n"
            "- Jangan pernah membayar biaya atau memberikan informasi pribadi kepada pihak yang tidak resmi.\n\n"
            "6. Pantau Pengumuman:\n"
            "Setelah melamar, pantau pengumuman di website resmi PT Pindad untuk mengetahui hasil seleksi."
        )

    # Rumah Sakit PT Pindad
    elif "rumah" in message or ("sakit" in message and "pindad" in message):
        return (
            "Rumah Sakit Umun (RSU) Pindad Bandung, rumah sakit berafiliasi dengan PT Pindad Medika Utama, menawarkan layanan kesehatan berkualitas tinggi."
            " Ada beberapa pelayanan yang terdapat di Rumah Sakit Umun (RSU) Pindad, yaitu:\n"
            "- Pelayanan IGD (Instalasi Gawat Darurat).\n"
            "- Pelayanan POLIKLINIK SPESIALIS.\n"
            "- Pelayanan RADIOLOGI.\n"
            "- Pelayanan POLIKLINIK GIGI.\n"
            "- Pelayanan RAWAT INAP.\n"
            "- Pelayanan KAMAR OPERASI.\n"
            "- Pelayanan HEMODIALISA.\n"
            "- Pelayanan LABORATORIUM.\n"
            "- Pelayanan FARMASI.\n"
            "- Pelayanan POLI EKSEKUTIF.\n"
            "- Pelayanan POLIKLINIK UMUM.\n\n"
            "Jam Buka Pelayanan Rumah Sakit Umum (RSU) Pindad Bandung:\n"
            "Senin - Juma'at : 06:00 - 16:00 WIB.\n"
            "Sabtu : 06:00 - 12:00 WIB.\n"
            "Minggu : Tutup.\n\n"
            "Alamat dan Kontak Rumah Sakit Umum (RSU) Pindad Bandung:\n"
            "PT Pindad Medika Utama RSU Pindad Bandung, Jl. Gatot Subroto No.517, Sukapura, Kec. Kiaracondong, Kota Bandung, Jawa Barat 40285 "
            "Informasi : (022) 732-2877 IGD : (022) 77322877 EXT Whatsapp : +6282115796951 humas@rsupindad.com"
        )

    # Layanan Rumah Sakit Pindad
    elif "layanan" in message or ("pelayanan" in message and "rsu" in message):
        return (
            "Pelayanan yang terdapat di Rumah Sakit Umum (RSU) Pindad Bandung, yaitu:\n" \
            "- Pelayanan IGD (Instalasi Gawat Darurat).\n"
            "- Pelayanan POLIKLINIK SPESIALIS.\n"
            "- Pelayanan RADIOLOGI.\n"
            "- Pelayanan POLIKLINIK GIGI.\n"
            "- Pelayanan RAWAT INAP.\n"
            "- Pelayanan KAMAR OPERASI.\n"
            "- Pelayanan HEMODIALISA.\n"
            "- Pelayanan LABORATORIUM.\n"
            "- Pelayanan FARMASI.\n"
            "- Pelayanan POLI EKSEKUTIF.\n"
            "- Pelayanan POLIKLINIK UMUM.\n"
        )
    
    # Jam Buka Rumah Sakit Pindad
    elif "jam" in message or ("buka" in message and "tutup" in message):
        return (
            "Jam Buka Pelayanan Rumah Sakit Umum (RSU) Pindad Bandung:\n"
            "Senin - Jum'at : 06:00 - 16:00 WIB.\n"
            "Sabtu : 06:00 - 12:00 WIB.\n"
            "Minggu : Tutup."
        )

    elif "kendaraan" in message and ("tidak nyala" in message or "ga nyala" in message or "tidak bisa nyala" in message):
        return "Periksa aki kendaraan, starter, dan bahan bakar."

    elif "perawatan" in message or "servis" in message or "maintenance" in message:
        return "Perawatan berkala meliputi pembersihan, pengecekan pelumas, dan penggantian suku cadang aus."

    elif "kalibrasi" in message:
        return "Kalibrasi harus dilakukan minimal setiap 6 bulan untuk alat optik dan radio."

    elif "senjata" in message and ("karat" in message or "berkarat" in message):
        return "Segera bersihkan bagian yang berkarat dan aplikasikan pelumas anti-karat."

    else:
        return "Maaf, saya belum memahami pertanyaan Anda. Coba tanyakan dengan kata kunci lain yang berkaitan dengan PT Pindad."
