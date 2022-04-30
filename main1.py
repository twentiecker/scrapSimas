from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os.path
import reading
import scraping
import writing


def full_action(url):
    print("===== Start Initialize =====")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(f"{url}")
    time.sleep(2)  # Allow 2 seconds for the web page to open

    # Get the last pagination
    last_button = driver.find_element(By.XPATH, "/html/body/section[2]/div[2]/div/nav/ul/li[5]/span/a")
    last_button.click()
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    x = page_soup.find("li", {"class": "page-item active"})
    last_pagination = int(x.text.replace("(current)", "").strip())
    print(last_pagination)
    driver.close()

    print("===== Finish Initialize =====")

    print("===== Start Scraping Pagination =====")
    scrap.scrap_pagination(url, last_pagination)
    print("===== Finish Scraping Pagination =====")
    print("===== Start Writing Pagination =====")
    write.write_url(file_name_link_pagination, "w+", scrap.list_pagination)
    print("===== Finish Writing Pagination =====")
    print("===== Start Reading Pagination =====")
    read.read_pagination(file_name_link_pagination)
    print("===== Finish Reading Pagination =====")

    list_pagination = tuple(read.list_pagination)
    for x in list_pagination:
        print("===== Start Scraping Profil =====")
        scrap.scrap_profil(x)
        print("===== Finish Scraping Profil =====")
        print("===== Start Writing Profil =====")
        write.write_url(file_name_link_profil, "a+", scrap.list_profil)
        print("===== Finish Writing Profil =====")

        # Remove url that has been scraped from the list_remainder
        for url in list_pagination:
            if url == x:
                read.list_pagination.remove(url)
                break

        print("===== Start Writing Remainder Pagination =====")
        write.write_url(file_name_link_remainder_pagination, "w+", read.list_pagination)
        print("===== Finish Writing Remainder Pagination =====")

    # Check whether file remainder still usefull or not
    print("===== START CHECKING FILE REMAINDER PAGINATION =====")
    read.read_pagination(file_name_link_remainder_pagination)
    if not read.list_pagination:
        os.remove(f"{file_name_link_pagination}.csv")
        os.remove(f"{file_name_link_remainder_pagination}.csv")
    print("===== ALL REMAINDER PAGINATION HAS BEEN SCRAPED =====")
    print("===== FINISH CHECKING FILE REMAINDER PAGINATION =====")

    print("===== Start Reading Profil =====")
    read.read_profil(file_name_link_profil)
    print("===== Finish Reading Profil =====")

    list_profil = tuple(read.list_profil)
    for y in list_profil:
        print("===== Start Scraping Detail =====")
        scrap.scrap_detail(y)
        print("===== Finish Scraping Detail =====")
        print("===== Start Writing Detail =====")
        # cek file_name_detail is exist or not
        file_exist_detail = os.path.isfile(f"{file_name_detail}.csv")
        write.write_detail(file_name_detail, file_exist_detail, scrap.times, scrap.x0_a, scrap.x0_b,
                           scrap.x1, scrap.x2,
                           scrap.x3, scrap.x4_phone, scrap.x4_email, scrap.x4_website, scrap.x5, scrap.x6,
                           scrap.x7,
                           scrap.x8, scrap.x9, scrap.x10_tanah, scrap.x10_status, scrap.x10_bangunan,
                           scrap.x10_tampung,
                           scrap.x11_fix, scrap.x12_fix, scrap.x13, scrap.x14, scrap.x15_fix, scrap.x16_fix,
                           scrap.x17,
                           scrap.x18_fix, scrap.url_detail)
        print("===== Finish Writing Detail =====")

        # Remove url that has been scraped from the list_remainder
        for url in list_profil:
            if url == y:
                read.list_profil.remove(url)
                break

        print("===== Start Writing Remainder Profil =====")
        write.write_url(file_name_link_remainder_profil, "w+", read.list_profil)
        print("===== Finish Writing Remainder Profil =====")

    # Check whether file remainder still usefull or not
    print("===== START CHECKING FILE REMAINDER PROFIL =====")
    read.read_profil(file_name_link_remainder_profil)
    if not read.list_profil:
        os.remove(f"{file_name_link_profil}.csv")
        os.remove(f"{file_name_link_remainder_profil}.csv")
    print("===== ALL REMAINDER PROFIL HAS BEEN SCRAPED =====")
    print("===== FINISH CHECKING FILE REMAINDER PROFIL =====")


url_base = f"https://simas.kemenag.go.id/page/profilmasjid/index/0/0/0/0/1/"

file_name_link_pagination = "link_pagination_masjid"
file_name_link_remainder_pagination = "link_remainder_pagination_masjid"
file_name_link_profil = "link_profil_masjid"
file_name_link_remainder_profil = "link_remainder_profil_masjid"
file_name_detail = "detail_masjid"

scrap = scraping.Scraping()
write = writing.Writing()
read = reading.Reading()

if os.path.isfile(f"{file_name_link_remainder_profil}.csv"):
    print("===== Start Reading Profil Remainder =====")
    read.read_profil(file_name_link_remainder_profil)
    print("===== Finish Reading Profil Remainder =====")

    list_profil = tuple(read.list_profil)
    for y in list_profil:
        print("===== Start Scraping Detail =====")
        scrap.scrap_detail(y)
        print("===== Finish Scraping Detail =====")
        print("===== Start Writing Detail =====")
        # cek file_name_detail is exist or not
        file_exist_detail = os.path.isfile(f"{file_name_detail}.csv")
        write.write_detail(file_name_detail, file_exist_detail, scrap.times, scrap.x0_a, scrap.x0_b, scrap.x1,
                           scrap.x2,
                           scrap.x3, scrap.x4_phone, scrap.x4_email, scrap.x4_website, scrap.x5, scrap.x6,
                           scrap.x7,
                           scrap.x8, scrap.x9, scrap.x10_tanah, scrap.x10_status, scrap.x10_bangunan,
                           scrap.x10_tampung,
                           scrap.x11_fix, scrap.x12_fix, scrap.x13, scrap.x14, scrap.x15_fix, scrap.x16_fix,
                           scrap.x17,
                           scrap.x18_fix, scrap.url_detail)
        print("===== Finish Writing Detail =====")

        # Remove url that has been scraped from the list_remainder
        for url in list_profil:
            if url == y:
                read.list_profil.remove(url)
                break

        print("===== Start Writing Remainder Profil =====")
        write.write_url(file_name_link_remainder_profil, "w+", read.list_profil)
        print("===== Finish Writing Remainder Profil =====")

    # Check whether file remainder still usefull or not
    print("===== START CHECKING FILE REMAINDER PROFIL =====")
    read.read_profil(file_name_link_remainder_profil)
    if not read.list_profil:
        os.remove(f"{file_name_link_profil}.csv")
        os.remove(f"{file_name_link_remainder_profil}.csv")
    print("===== ALL REMAINDER PROFIL HAS BEEN SCRAPED =====")
    print("===== FINISH CHECKING FILE REMAINDER PROFIL =====")

else:
    if os.path.isfile(f"{file_name_link_remainder_pagination}.csv"):
        print("===== Start Reading Pagination =====")
        read.read_pagination(file_name_link_remainder_pagination)
        print("===== Finish Reading Pagination =====")

        list_pagination = tuple(read.list_pagination)
        for x in list_pagination:
            print("===== Start Scraping Profil =====")
            scrap.scrap_profil(x)
            print("===== Finish Scraping Profil =====")
            print("===== Start Writing Profil =====")
            write.write_url(file_name_link_profil, "a+", scrap.list_profil)
            print("===== Finish Writing Profil =====")

            # Remove url that has been scraped from the list_remainder
            for url in list_pagination:
                if url == x:
                    read.list_pagination.remove(url)
                    break

            print("===== Start Writing Remainder Pagination =====")
            write.write_url(file_name_link_remainder_pagination, "w+", read.list_pagination)
            print("===== Finish Writing Remainder Pagination =====")

        # Check whether file remainder still usefull or not
        print("===== START CHECKING FILE REMAINDER PAGINATION =====")
        read.read_pagination(file_name_link_remainder_pagination)
        if not read.list_pagination:
            os.remove(f"{file_name_link_pagination}.csv")
            os.remove(f"{file_name_link_remainder_pagination}.csv")
        print("===== ALL REMAINDER PAGINATION HAS BEEN SCRAPED =====")
        print("===== FINISH CHECKING FILE REMAINDER PAGINATION =====")

        print("===== Start Reading Profil =====")
        read.read_profil(file_name_link_profil)
        print("===== Finish Reading Profil =====")

        list_profil = tuple(read.list_profil)
        for y in list_profil:
            print("===== Start Scraping Detail =====")
            scrap.scrap_detail(y)
            print("===== Finish Scraping Detail =====")
            print("===== Start Writing Detail =====")
            # cek file_name_detail is exist or not
            file_exist_detail = os.path.isfile(f"{file_name_detail}.csv")
            write.write_detail(file_name_detail, file_exist_detail, scrap.times, scrap.x0_a, scrap.x0_b,
                               scrap.x1,
                               scrap.x2,
                               scrap.x3, scrap.x4_phone, scrap.x4_email, scrap.x4_website, scrap.x5, scrap.x6,
                               scrap.x7,
                               scrap.x8, scrap.x9, scrap.x10_tanah, scrap.x10_status, scrap.x10_bangunan,
                               scrap.x10_tampung,
                               scrap.x11_fix, scrap.x12_fix, scrap.x13, scrap.x14, scrap.x15_fix, scrap.x16_fix,
                               scrap.x17,
                               scrap.x18_fix, scrap.url_detail)
            print("===== Finish Writing Detail =====")

            # Remove url that has been scraped from the list_remainder
            for url in list_profil:
                if url == y:
                    read.list_profil.remove(url)
                    break

            print("===== Start Writing Remainder Profil =====")
            write.write_url(file_name_link_remainder_profil, "w+", read.list_profil)
            print("===== Finish Writing Remainder Profil =====")

        # Check whether file remainder still usefull or not
        print("===== START CHECKING FILE REMAINDER PROFIL =====")
        read.read_profil(file_name_link_remainder_profil)
        if not read.list_profil:
            os.remove(f"{file_name_link_profil}.csv")
            os.remove(f"{file_name_link_remainder_profil}.csv")
        print("===== ALL REMAINDER PROFIL HAS BEEN SCRAPED =====")
        print("===== FINISH CHECKING FILE REMAINDER PROFIL =====")

    else:
        if os.path.isfile(f"{file_name_link_profil}.csv"):
            print("===== Start Reading Profil =====")
            read.read_profil(file_name_link_profil)
            print("===== Finish Reading Profil =====")

            list_profil = tuple(read.list_profil)
            for y in list_profil:
                print("===== Start Scraping Detail =====")
                scrap.scrap_detail(y)
                print("===== Finish Scraping Detail =====")
                print("===== Start Writing Detail =====")
                # cek file_name_detail is exist or not
                file_exist_detail = os.path.isfile(f"{file_name_detail}.csv")
                write.write_detail(file_name_detail, file_exist_detail, scrap.times, scrap.x0_a, scrap.x0_b,
                                   scrap.x1, scrap.x2,
                                   scrap.x3, scrap.x4_phone, scrap.x4_email, scrap.x4_website, scrap.x5, scrap.x6,
                                   scrap.x7,
                                   scrap.x8, scrap.x9, scrap.x10_tanah, scrap.x10_status, scrap.x10_bangunan,
                                   scrap.x10_tampung,
                                   scrap.x11_fix, scrap.x12_fix, scrap.x13, scrap.x14, scrap.x15_fix, scrap.x16_fix,
                                   scrap.x17,
                                   scrap.x18_fix, scrap.url_detail)
                print("===== Finish Writing Detail =====")

                # Remove url that has been scraped from the list_remainder
                for url in list_profil:
                    if url == y:
                        read.list_profil.remove(url)
                        break

                print("===== Start Writing Remainder Profil =====")
                write.write_url(file_name_link_remainder_profil, "w+", read.list_profil)
                print("===== Finish Writing Remainder Profil =====")

            # Check whether file remainder still usefull or not
            print("===== START CHECKING FILE REMAINDER PROFIL =====")
            read.read_profil(file_name_link_remainder_profil)
            if not read.list_profil:
                os.remove(f"{file_name_link_profil}.csv")
                os.remove(f"{file_name_link_remainder_profil}.csv")
            print("===== ALL REMAINDER PROFIL HAS BEEN SCRAPED =====")
            print("===== FINISH CHECKING FILE REMAINDER PROFIL =====")

        else:
            full_action(url_base)
