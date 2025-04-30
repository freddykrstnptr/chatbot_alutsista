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

    if any(greeting in message for greeting in ["halo", "hai", "haii", "haloo", "hello", "halo tapin", "hallo tapin", 
                                                "hai tapin", "haii tapin", "helo tapin", "hello tapin"]):
        return f"{get_time_based_greeting()}, halo juga! Ada yang bisa saya bantu seputar PT Pindad?"

    elif "selamat pagi" in message:
        return "Selamat pagi juga! Semoga harimu menyenangkan. Ada yang bisa saya bantu seputar PT Pindad?"
    elif "selamat siang" in message:
        return "Selamat siang juga! Semoga harimu lancar ya. Ada yang bisa saya bantu seputar PT Pindad?"
    elif "selamat malam" in message:
        return "Selamat malam juga! Ada yang ingin ditanyakan sebelum istirahat?"
    
    elif "perusahaan" in message and "pindad" in message:
        return (
            "PT Pindad adalah anak usaha Len Industri yang bergerak di bidang produksi Kendaraan dan peralatan pertahanan.\n"
            "Perusahaan ini memiliki dua pabrik, yakni di Bandung (tempat produksi senjata, kendaraan khusus, dan mesin industrial) dan di Turen (tempat produksi munisi dan bahan peledak komersial).\n"
            "Untuk mendukung kegiatan bisnisnya, perusahaan ini pun memiliki dua kantor perwakilan di Jakarta.\n"
            "Perusahaan ini merupakan salah satu perusahaan tertua di Indonesia (menurut keberlanjutan usaha) yang masih tetap berdiri sampai sekarang dan merupakan satu-satunya perusahaan manufaktur pertahanan di Indonesia."
        )

    elif "sejarah" in message and "pindad" in message:
        return (
            "Sejarah PT Pindad dimulai pada tahun 1808 ketika Gubernur Jenderal Hindia Belanda, Herman Willem Daendels,\n"
            "mendirikan bengkel senjata bernama Constructie Winkel (CW) di Surabaya. CW kemudian berkembang dan berubah nama menjadi Artilerie Constructie Winkel (ACW) pada 1851,\n"
            "yang mencakup produksi senjata, munisi, dan laboratorium penelitian. Pada masa Perang Dunia I, pemerintah Hindia Belanda memindahkan unit-unit penting ACW ke Bandung karena dinilai lebih aman dan strategis.\n"
            "Setelah relokasi selesai antara tahun 1918 hingga 1932, unit-unit tersebut digabung menjadi Artilerie Inrichtingen (AI).\n"
            "Saat pendudukan Jepang, nama-nama unitnya diubah ke dalam bahasa Jepang. Setelah kemerdekaan Indonesia, pada 9 Oktober 1945, AI diambil alih oleh para pejuang Indonesia dan diubah namanya menjadi Pabrik Senjata Kiaracondong.\n"
            "Pada masa Agresi Militer Belanda, pabrik ini dibagi menjadi dua bagian: Leger Produktie Bedrijven (LPB) dan Central Reparatie Werkplaats.\n"
            "Setelah Konferensi Meja Bundar tahun 1949, LPB diserahkan ke pemerintah Indonesia dan menjadi Pabrik Senjata dan Mesiu (PSM) di bawah pengelolaan TNI AD.\n"
            "PSM berhasil memproduksi laras senjata dan terus berkembang meski kekurangan tenaga ahli. Pada tahun 1958, namanya diubah menjadi Pabal AD, lalu pada tahun 1962 menjadi Perindustrian Angkatan Darat (Pindad).\n"
            "Pindad mulai memproduksi senjata secara massal dan menjadi pemasok utama senjata TNI. Pada 1972, perusahaan ini berubah lagi menjadi Kopindad,\n"
            "namun setelah beberapa kendala dalam Operasi Seroja, Kopindad kembali menjadi Pindad pada tahun 1976.\n"
            "Karena keterbatasan sebagai bagian dari TNI, pada 1983 status Pindad diubah menjadi perseroan terbatas agar lebih fleksibel.\n"
            "Terakhir, pada 12 Januari 2022, pemerintah menyerahkan mayoritas saham Pindad ke Len Industri sebagai bagian dari pembentukan holding BUMN pertahanan."
        )
    
    elif "lokasi" in message and "pindad" in message or "alamat" in message and "pindad" in message:
        return (
            "PT Pindad memiliki kantor pusat dan pabrik utama di **Bandung, Jawa Barat**.\n"
            "Selain itu, Pindad juga memiliki fasilitas produksi munisi di **Turen, Kabupaten Malang, Jawa Timur**."
        )

    elif "produk" in message and "pindad" in message or "hasil" in message and "pindad" in message:
        return (
            "PT Pindad memproduksi berbagai alat utama sistem pertahanan seperti:\n"
            "- Senjata ringan (SS1, SS2, SPR),\n"
            "- Amunisi berbagai kaliber,\n"
            "- Kendaraan taktis seperti **Maung**, **Komodo**, dan **Anoa**,\n"
            "- Alat berat seperti ekskavator dan traktor untuk sektor sipil dan militer."
        )

    elif "maung" in message or ("kendaraan" in message and "taktis" in message):
        return (
            "**Maung** adalah kendaraan taktis ringan buatan PT Pindad yang dirancang untuk operasi militer dan mobilitas tinggi.\n"
            "Diperkenalkan pertama kali tahun 2020, Maung digunakan oleh TNI dan juga tersedia versi sipil terbatas.\n"
            "Dilengkapi dengan kemampuan off-road, modular, dan bisa dipasangi senjata ringan."
        )

    elif "radio" in message and ("tidak nyala" in message or "mati" in message or "ga nyala" in message):
        return "Cek koneksi antena, periksa baterai, dan pastikan frekuensi benar."

    elif "senapan" in message and "macet" in message:
        return "Bersihkan laras senapan, cek pelumas, dan pastikan amunisi tidak rusak."

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
