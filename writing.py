class Writing:
    def write_url(self, file_name, mode, list_url):
        f = open(f"{file_name}.csv", mode, encoding="utf-8")  # create/overwrite file (w+)
        for i in range(len(list_url)):
            f.write(f"{list_url[i]}\n")
        f.close()

    def write_detail(self, file_name, file_exist, scrap_date, nama_masjid, id_masjid, kategori_masjid, tahun_berdiri,
                     alamat, telp, email, website, pengurus, imam, khatib, muazin, remas, luas_tanah, status_tanah,
                     luas_bangunan, daya_tampung, fasil_umum, kegiatan, fasil_ramah_anak, fasil_dis, fasil_perpus,
                     dokumen, sejarah, foto_masjid, url):

        # membuka file csv dengan memberikan atribut "w" yang berarti inisiasi untuk melakukan write pada file tsb
        f = open(f"{file_name}.csv", "a+", encoding="utf-8")

        # menuliskan judul (headers) pada baris pertama file csv
        if not file_exist:
            headers = "scrap_date;nama_masjid;id_masjid;kategori_masjid;tahun_berdiri;alamat;telp;email;website;" \
                      "pengurus;imam;khatib;muazin;remas;luas_tanah;status_tanah;luas_bangunan;daya_tampung;" \
                      "fasil_umum;kegiatan;fasil_ramah_anak;fasil_dis;fasil_perpus;dokumen;sejarah;foto_masjid;url\n"
            f.write(headers)

        # menulis data pada file csv
        f.write(
            scrap_date + ";" + nama_masjid + ";" + id_masjid + ";" + kategori_masjid + ";" + tahun_berdiri + ";" +
            alamat + ";" + telp + ";" + email + ";" + website + ";" + pengurus + ";" + imam + ";" + khatib + ";" +
            muazin + ";" + remas + ";" + luas_tanah + ";" + status_tanah + ";" + luas_bangunan + ";" +
            daya_tampung + ";" + fasil_umum + ";" + kegiatan + ";" + fasil_ramah_anak + ";" + fasil_dis + ";" +
            fasil_perpus + ";" + dokumen + ";" + sejarah + ";" + foto_masjid + ";" + url + "\n")

        f.close()
