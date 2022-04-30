from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
import datetime


class Scraping:
    def __init__(self):
        self.list_pagination = []
        self.list_profil = []
        self.times = ""
        self.x0_a = ""
        self.x0_b = ""
        self.x1 = ""
        self.x2 = ""
        self.x3 = ""
        self.x4_phone = ""
        self.x4_email = ""
        self.x4_website = ""
        self.x5 = ""
        self.x6 = ""
        self.x7 = ""
        self.x8 = ""
        self.x9 = ""
        self.x10_tanah = ""
        self.x10_status = ""
        self.x10_bangunan = ""
        self.x10_tampung = ""
        self.x11_fix = ""
        self.x12_fix = ""
        self.x13 = ""
        self.x14 = ""
        self.x15_fix = ""
        self.x16_fix = ""
        self.x17 = ""
        self.x18_fix = "Foto Masjid tidak ditemukan."
        self.url_detail = ""

    def scrap_pagination(self, base, pagination):
        page = 0
        self.list_pagination = []
        for i in range(pagination):
            if page == 0:
                url_page = f"none"
            else:
                url_page = f"none/{page}"
            url = urljoin(base, url_page)
            # print(url)
            self.list_pagination.append(url)
            page = page + 20

    def scrap_profil(self, url):
        self.list_profil = []
        url_client = urlopen(url)
        page_html = url_client.read()
        url_client.close()

        # melakukan parse html
        page_soup = Soup(page_html, "html.parser")

        # menemukan element article pada html yang sudah di parse sebelumnya
        containers = page_soup.findAll("a", class_="btn btn-sm btn-info")

        # mendapatkan semua link yang ada di setiap artikel pada halaman berita dan menyimpannya pada list_profil
        for container in containers:
            link = container["href"]
            self.list_profil.append(link)

    def scrap_detail(self, url):
        # initiate variable
        x11 = ""
        x12 = ""
        x15 = ""
        x16 = ""
        x18 = ""

        url_client = urlopen(url)
        page_html = url_client.read()
        url_client.close()

        # melakukan parse html
        page_soup = Soup(page_html, "html.parser")

        # timestamp scraping
        self.times = datetime.datetime.now().strftime("%d/%m/%Y")
        print(self.times)

        # nama masjid
        masjid = page_soup.find("h1", class_="masjid-title")
        self.x0_a = masjid.text.strip()
        print(self.x0_a)

        # id masjid
        id_masjid = page_soup.find("div", class_="masjid-card")
        self.x0_b = id_masjid.a.text.strip()
        print(self.x0_b)

        # keterangan umum masjid
        kategori = page_soup.find("span", class_="badge badge-info")
        self.x1 = kategori.text.strip()
        print(self.x1)

        # tahun berdirinya masjid
        tahun = page_soup.find("div", class_="masjid-alamat-calendar")
        self.x2 = tahun.text.strip().replace("Didirikan pada tahun ", "")
        print(self.x2)

        # alamat masjid
        alamat = page_soup.find("div", class_="masjid-alamat-location").p
        self.x3 = " ".join(alamat.text.split())
        print(self.x3)

        # kontak masjid
        kontak_container = page_soup.find_all("div", class_="masjid-alamat-phone")
        for data in kontak_container:
            kontak = data.find("p")
            # nomor telephone
            phone = data.find("i", {"class": "ti-mobile"})
            if phone:
                self.x4_phone = "'" + kontak.text.strip()
            # alamat email
            email = data.find("i", {"class": "ti-email"})
            if email:
                self.x4_email = "'" + kontak.text.strip()
            # alamat website
            website = data.find("i", {"class": "ti-email"})
            if website:
                self.x4_website = "'" + kontak.text.strip()
        print(self.x4_phone)
        print(self.x4_email)
        print(self.x4_website)

        # pengurus masjid
        pengurus = page_soup.find("div", class_="summary-item pengurus").p
        self.x5 = pengurus.text.strip()
        print(self.x5)

        # imam masjid
        imam = page_soup.find("div", class_="summary-item imam").p
        self.x6 = imam.text.strip()
        print(self.x6)

        # khatib masjid
        khatib = page_soup.find("div", class_="summary-item khatib").p
        self.x7 = khatib.text.strip()
        print(self.x7)

        # muazin masjid
        muazin = page_soup.find("div", class_="summary-item muazin").p
        self.x8 = muazin.text.strip()
        print(self.x8)

        # remas
        remas = page_soup.find("div", class_="summary-item remas").p
        self.x9 = remas.text.strip()
        print(self.x9)

        # profil masjid
        container_profil = page_soup.find_all("div", class_="row")
        for data in container_profil:
            kategori = data.find("div", class_="label col-md-6 col-7")
            content_kategori = data.find("div", class_="label col-md-6 col-5")
            if kategori:
                # luas tanah
                if kategori.text.strip() == "Luas Tanah":
                    self.x10_tanah = content_kategori.text.replace(".", "").strip()
                # status tanah
                if kategori.text.strip() == "Status Tanah":
                    self.x10_status = content_kategori.text.replace(".", "").strip()
                # luas bangunan
                if kategori.text.strip() == "Luas Bangunan":
                    self.x10_bangunan = content_kategori.text.replace(".", "").strip()
                # Daya tampung jamaah
                if kategori.text.strip() == "Daya Tampung Jamaah":
                    self.x10_tampung = content_kategori.text.replace(".", "").strip()
        print(self.x10_tanah)
        print(self.x10_status)
        print(self.x10_bangunan)
        print(self.x10_tampung)

        # fasilitas umum
        parent = page_soup.find_all("div", class_="col-md-6 col-12")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Fasilitas Umum":
                    fasil = child.find_all("div", class_="col-6 masjid-item")
                    temp = ""
                    for data in fasil:
                        temp = data.text.strip() + ", " + temp
                    x11 = temp
            except AttributeError:
                pass
        self.x11_fix = x11.strip().strip(",")
        print(self.x11_fix)

        # kegiatan
        parent = page_soup.find_all("div", class_="col-md-6 col-12")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Kegiatan":
                    fasil = child.find_all("div", class_="col-6 masjid-item")
                    temp = ""
                    for data in fasil:
                        temp = data.text.strip().replace(",", "") + ", " + temp
                    x12 = temp
            except AttributeError:
                pass
        self.x12_fix = x12.strip().strip(",")
        print(self.x12_fix)

        # fasilitas ramah anak
        parent = page_soup.find_all("div", class_="col-md-6 col-12")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Fasilitas Ramah Anak":
                    fasil = child.find_all("div", class_="col-6 masjid-item")
                    temp = ""
                    for data in fasil:
                        temp = temp + data.text.strip() + ", "
                    if temp == "":
                        self.x13 = "Fasilitas ramah anak tidak ditemukan"
                        print(self.x13)
                    else:
                        self.x13 = temp
                        print(self.x13)
            except AttributeError:
                pass

        # fasilitas disabilitas
        parent = page_soup.find_all("div", class_="col-md-6 col-12")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Fasilitas Disabilitas":
                    fasil = child.find_all("div", class_="col-6 masjid-item")
                    temp = ""
                    for data in fasil:
                        temp = temp + data.text.strip() + ", "
                    if temp == "":
                        self.x14 = "Fasilitas disabilitas tidak ditemukan"
                        print(self.x14)
                    else:
                        self.x14 = temp
                        print(self.x14)
            except AttributeError:
                pass

        # fasilitas Perpustakaan
        parent = page_soup.find_all("div", class_="col-md-6 col-12")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Fasilitas Perpustakaan":
                    fasil = child.find_all("div", class_="label col-6")
                    temp = ""
                    for data in fasil:
                        if (data.text.strip() == "Kondisi" or
                                data.text.strip() == "Luas Perpustakaan" or
                                data.text.strip() == "Jumlah Pengurus"):
                            temp = temp + data.text.strip() + ": "
                        else:
                            temp = temp + data.text.strip() + ", "
                    fasil1 = child.find("div", class_="label col-md-9 col-6")
                    if fasil1.text.strip() != "-":
                        fasil1 = child.find_all("div", class_="col-6 masjid-item")
                        temp1 = ""
                        for x in fasil1:
                            y = " ".join(x.text.strip().split())
                            temp1 = temp1 + y + " | "
                        temp = temp + "Jenis Buku : " + temp1 + ", "
                        x15 = temp
                    else:
                        temp = temp + "Jenis Buku : " + fasil1.text.strip() + ", "
                        x15 = temp
            except AttributeError:
                pass
        self.x15_fix = x15.strip().strip(",")
        print(self.x15_fix)

        # Dokumen
        parent = page_soup.find_all("div", class_="col")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Dokumen":
                    fasil = child.find("p")
                    temp = ""
                    if " ".join(fasil.text.split()) != "Dokumen tidak ditemukan atau belum diunggah":
                        fasil = child.find_all("a", class_="a-pdf")
                        for x in fasil:
                            temp = temp + x["href"] + ", "
                        x16 = temp
                    else:
                        x16 = " ".join(fasil.text.split())
            except AttributeError:
                pass
        self.x16_fix = x16.strip().strip(",")
        print(self.x16_fix)

        # Sejarah Masjid
        parent = page_soup.find_all("div", class_="col")
        for child in parent:
            try:
                cek = child.find("h4").text
                if cek == "Sejarah Masjid":
                    try:
                        fasil = child.find("div", class_="col-md-12")
                        self.x17 = fasil.text.strip().replace("-", "~")
                        print(self.x17)
                    except AttributeError:
                        fasil = child.find("div", class_="masjid-sejarah show-less")
                        self.x17 = " ".join(fasil.text.split()).replace("-", "~")
                        print(self.x17)
            except AttributeError:
                pass

        # Foto Masjid
        try:
            try:
                parent = page_soup.find("div", class_="profil-masjid-photos")
                child = parent.find_all("a", href=True)
                temp = ""
                for x in child:
                    temp = temp + x["href"] + ", "
                x18 = temp

            except AttributeError:
                parent = page_soup.find_all("div", class_="section-content-info-wrapper")
                for child in parent:
                    try:
                        cek = child.find("h4").text
                        if cek == "Foto Masjid":
                            try:
                                fasil = child.find("div", class_="col")
                                x18 = fasil.text.strip()
                            except AttributeError:
                                pass
                    except AttributeError:
                        pass
        except AttributeError:
            pass
        self.x18_fix = x18.strip().strip(",")
        print(self.x18_fix)

        # url for page detail
        self.url_detail = url
        print(self.url_detail)
