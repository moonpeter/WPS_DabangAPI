import json
import os
import re
import time
import urllib

import requests
from django.core.files import File
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException

from config import settings
from config.settings import MEDIA_ROOT
from members.models import SocialLogin
from posts.crawling.find_urls import find_apartment_urls, find_urls

from ..models import SalesForm, PostAddress, SecuritySafetyFacilities, OptionItem, \
    MaintenanceFee, RoomOption, RoomSecurity, PostRoom, Broker, PostImage, AdministrativeDetail, ComplexInformation, \
    ComplexImage, RecommendComplex

KAKAO_APP_ID = settings.KAKAO_APP_ID


def postFind():
    POSTS_DIR = os.path.join(MEDIA_ROOT, '.posts')

    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR, exist_ok=True)

    driver = webdriver.Chrome('/Users/mac/projects/ChromeWebDriver/chromedriver')
    # driver = webdriver.Chrome('/Users/moonpeter/Desktop/Selenium/chromedriver')
    SocialLogin.start()
    # 다방 성수동 매물 url
    # url_all_list = find_apartment_urls()
    # print('아파트 단지 url', url_all_list)
    # officetels = find_urls()
    # url_all_list += officetels
    # print('오피스텔 매물', officetels)
    url_all_list = [
        # 'https://www.dabangapp.com/room/5e992d31d9d3a15c88491696',
        # 'https://www.dabangapp.com/room/5e9fd1f1a639766eb587c9fc',
        # 'https://www.dabangapp.com/room/5e992d30f30bdb6390449f94',
        # 'https://www.dabangapp.com/room/5e9efb251e60da5787550276',
        # 'https://www.dabangapp.com/room/5e9efb20350ca26a1cb134db',
        # 'https://www.dabangapp.com/room/5e9e60010f85d2751c0ff977',
        # 'https://www.dabangapp.com/room/5e9a6dbe897ecf1ff2965b20',
        # 'https://www.dabangapp.com/room/5ea3e2d43a5041776f9098a3',
        # 'https://www.dabangapp.com/room/5ea66533484ba56e2620860f',
        # 'https://www.dabangapp.com/room/5ea667d022bf735eb278c521',
        # 'https://www.dabangapp.com/room/5e8ae5d9ff822c19ad4d0911',
        # 'https://www.dabangapp.com/room/5ea109a2bcb6b164ec1a2691',
        # 'https://www.dabangapp.com/room/5e8ab2d3e5b96224197411d8',
        # 'https://www.dabangapp.com/room/5e868a4369367f4ba04cbd9a',
        # 'https://www.dabangapp.com/room/5ea66ab89e79b85eb2fdda04',
        # 'https://www.dabangapp.com/room/5ea65099c09f1446b20f3fe8',
        # 'https://www.dabangapp.com/room/5ea12d58a0489228291ef92a',
        # 'https://www.dabangapp.com/room/5e9e81dad2c65a036b6485a2',
        # 'https://www.dabangapp.com/room/5ea6660c65a9c97e26801afa',
        # 'https://www.dabangapp.com/room/5ea63b1fd829bd07c1cff5f3',
        # 'https://www.dabangapp.com/room/5e9d0e86d83b1c575d03a3a2',
        # 'https://www.dabangapp.com/room/5ea1445d636ba07f16d4646c',
        # 'https://www.dabangapp.com/room/5ea11d665478006b87d097a9',
        'https://www.dabangapp.com/room/5e95402d89c3f624a200b096',
        'https://www.dabangapp.com/room/5ea66483ea35ba62288bc44d',
        'https://www.dabangapp.com/room/5e990448a2d17027c7d5a1be',
        'https://www.dabangapp.com/room/5ea6438d3df14f40108de38f',
        'https://www.dabangapp.com/room/5e9e4be7a2089e2a1ea40848',
        'https://www.dabangapp.com/room/5e8ab2a116fdf52419a4663e',
        'https://www.dabangapp.com/room/5e8c62242dca726fb8181a93',
        'https://www.dabangapp.com/room/5e8ac6d37f0d924616315449',
        'https://www.dabangapp.com/room/5e982559ec85df024d33c6ff',
        'https://www.dabangapp.com/room/5e980174c176a611a8c08e2a',
        'https://www.dabangapp.com/room/5ea11daa6ad99a6b87825030',
        'https://www.dabangapp.com/room/5e8e87131a056b7de982d60c',
        'https://www.dabangapp.com/room/5ea659fffa7e393cdb855095',
        'https://www.dabangapp.com/room/5e9a6d46240f921ded23c612',
        'https://www.dabangapp.com/room/5ea6719df30e4906b9b5d1b0',
        'https://www.dabangapp.com/room/5e82935402a1f77695464902',
        'https://www.dabangapp.com/room/5e9001d9004a6b46f8e283bc',
        'https://www.dabangapp.com/room/5ea107a769d22940bb6dfb00',
        'https://www.dabangapp.com/room/5ea669b687ca6b5eb288ae1d',
        'https://www.dabangapp.com/room/5ea64e310d2d041fb17a3b86',
        'https://www.dabangapp.com/room/5e8be7742fa6cd03e13c708b',
        'https://www.dabangapp.com/room/5ea108010bc55f40bb3205d7',
        'https://www.dabangapp.com/room/5ea650aa144e15508f79bb92',
        'https://www.dabangapp.com/room/5ea254ea23e2d246388705c9',
        'https://www.dabangapp.com/room/5e81beab3da96b3251ddf7eb',
        'https://www.dabangapp.com/room/5e991254697bff521708eeb6',
        'https://www.dabangapp.com/room/5ea14e016addd145b3ec8dc3',
        'https://www.dabangapp.com/room/5e901025f3ff9d77d2ee73f7',
        'https://www.dabangapp.com/room/5e857bc1b4e0795b8a572512',
        'https://www.dabangapp.com/room/5ea6646d0d41656228f921e9',
        'https://www.dabangapp.com/room/5ea12196911aae727274516c',
        'https://www.dabangapp.com/room/5ea6658f73f5247e2527ee16',
        'https://www.dabangapp.com/room/5e9d9148b9fe4f38991401fa',
        'https://www.dabangapp.com/room/5e9d5e4e42d946527da08d99',
        'https://www.dabangapp.com/room/5ea669b2ffedbb5eb231d886',
        'https://www.dabangapp.com/room/5ea67a1edf2d2f21d37dfee0',
        'https://www.dabangapp.com/room/5ea65779eebf365243aab68d',
        'https://www.dabangapp.com/room/5e967dbc5448c97f566410e9',
        'https://www.dabangapp.com/room/5ea65e7b44582461ecf71471',
        'https://www.dabangapp.com/room/5e919ebcf6898d237c673810',
        'https://www.dabangapp.com/room/5ea15bec9e83bd1cd30c0dd7',
        'https://www.dabangapp.com/room/5e9f966d5bff6f69c8e5269a',
        'https://www.dabangapp.com/room/5e9a801126b6362ef9643304',
        'https://www.dabangapp.com/room/5e959ed59d092d2d947a6e82',
        'https://www.dabangapp.com/room/5ea13a4941df6448833e550f',
        'https://www.dabangapp.com/room/5e9a8085ec0d5e2ef92ba4b0',
        'https://www.dabangapp.com/room/5e990650191cf83bfeb9b2ff',
        'https://www.dabangapp.com/room/5ea692c73da7ca490ff20de4',
        'https://www.dabangapp.com/room/5e8ac3f8d5f8af65d9d3516d',
        'https://www.dabangapp.com/room/5e9830b9b663983579c58766',
        'https://www.dabangapp.com/room/5ea123f5b5044172720f27c4',
        'https://www.dabangapp.com/room/5ea68bcf4b33eb37381dd93d',
        'https://www.dabangapp.com/room/5e9579612464e04ad27f0f71',
        'https://www.dabangapp.com/room/5e950f7d8464a8139b87e2f9',
        'https://www.dabangapp.com/room/5e98255d2d3292024de08380',
        'https://www.dabangapp.com/room/5e991207f8626e52174025fa',
        'https://www.dabangapp.com/room/5e9a9d28f3c5cc720adcf372',
        'https://www.dabangapp.com/room/5ea65531035fce4362f5493d',
        'https://www.dabangapp.com/room/5ea24657aaba051a6a2daad9',
        'https://www.dabangapp.com/room/5ea68e4fe8ed5447ab747158',
        'https://www.dabangapp.com/room/5ea679fb8eb3a7263907cd20',
        'https://www.dabangapp.com/room/5ea66aa69675995eb26a6960',
        'https://www.dabangapp.com/room/5ea681128a6ab33164610bc3',
        'https://www.dabangapp.com/room/5e9e84a82813302220568899',
        'https://www.dabangapp.com/room/5ea153fc23360a602a5b3dff',
        'https://www.dabangapp.com/room/5e993faad404b13eebefc07c',
        'https://www.dabangapp.com/room/5ea65513f54e13436201dba6',
        'https://www.dabangapp.com/room/5e8c2e7efbefce1fe5167abd',
        'https://www.dabangapp.com/room/5e8293bb31c88476954f7213',
        'https://www.dabangapp.com/room/5ea14be8a66c1345b3284e41',
        'https://www.dabangapp.com/room/5ea64e09937bb91fb128f28a',
        'https://www.dabangapp.com/room/5e8d77eec22836604787ccb7',
        'https://www.dabangapp.com/room/5e8aa4778e97eb10a32212da',
        'https://www.dabangapp.com/room/5e9cf255b8b9d54ecb127b6d',
        'https://www.dabangapp.com/room/5ea11e5b142e92049163a55e',
        'https://www.dabangapp.com/room/5ea664de11ee63694bbac546',
        'https://www.dabangapp.com/room/5ea664be6d685d694ba15fdf',
        'https://www.dabangapp.com/room/5e9a93546f87913df7e9a3c8',
        'https://www.dabangapp.com/room/5e8fed22182fb750ac3ed90c',
        'https://www.dabangapp.com/room/5ea659efb36f513cdb7eecb4',
        'https://www.dabangapp.com/room/5ea64bb161dad4786008e4e5',
        'https://www.dabangapp.com/room/5e9e67899c67b66a65db2727',
        'https://www.dabangapp.com/room/5e9a9586f8d6c15542e17680',
        'https://www.dabangapp.com/room/5ea14e14caceac45b3db6f09',
        'https://www.dabangapp.com/room/5ea66086393fbb26ee468081',
        'https://www.dabangapp.com/room/5ea109f0d044dc64ec9e83c4',
        'https://www.dabangapp.com/room/5ea15bed9b68f41cd31be68f',
        'https://www.dabangapp.com/room/5ea100f97e378c2fd6bcf605',
        'https://www.dabangapp.com/room/5e8ae5dd2a140b19ad1152a0',
        'https://www.dabangapp.com/room/5e9818a86240cf50e9caced0',
        'https://www.dabangapp.com/room/5ea686a3d5d5e31f117ea693',
        'https://www.dabangapp.com/room/5ea14ef101a9a858d050e301',
        'https://www.dabangapp.com/room/5e81aed624e07a1c823c3867',
        'https://www.dabangapp.com/room/5e96749059ccda73850bed67',
        'https://www.dabangapp.com/room/5e941f861343d9304c095c33',
        'https://www.dabangapp.com/room/5e84665fdec4512c8b64192a',
        'https://www.dabangapp.com/room/5e819e0e2ce1b126d9c88027',
        'https://www.dabangapp.com/room/5e9e7a6676b64676929b5a19',
        'https://www.dabangapp.com/room/5ea66d43fd4c941c8c5ae5ff',
        'https://www.dabangapp.com/room/5e9d631a9ed0543d07893449',
        'https://www.dabangapp.com/room/5e8d636cdc19e6397ec46d1e',
        'https://www.dabangapp.com/room/5e9e7a1a3275bd3dedfbadbf',
        'https://www.dabangapp.com/room/5ea6858ba6f3942fc7d93400',
        'https://www.dabangapp.com/room/5e8ff5dc57abf65d42b86d86',
        'https://www.dabangapp.com/room/5e82b22081a85e73e67a5dda',
        'https://www.dabangapp.com/room/5e8e76abab03dd31e56dcb71',
        'https://www.dabangapp.com/room/5e8830b78321b32902cade76',
        'https://www.dabangapp.com/room/5e9a828f0d68674507df2f6f',
        'https://www.dabangapp.com/room/5e81610280554a6b432242ca',
        'https://www.dabangapp.com/room/5ea285b0ed7cc42bf9d6e68b',
        'https://www.dabangapp.com/room/5ea6885d490e5f4178850216',
        'https://www.dabangapp.com/room/5e82b23608fecc73e61f4d63',
        'https://www.dabangapp.com/room/5e9900c05b96152a30f1836c',
        'https://www.dabangapp.com/room/5e85790803871a2aa7b0afdb',
        'https://www.dabangapp.com/room/5e856698c18a88387dfe7d10',
        'https://www.dabangapp.com/room/5e8edff144048f63141f001c',
        'https://www.dabangapp.com/room/5ea678fc7cc1f313a06db646',
        'https://www.dabangapp.com/room/5e86a3c6c3bafd57a1dd6a77',
        'https://www.dabangapp.com/room/5e940cdd1ce2ec3178760a38',
        'https://www.dabangapp.com/room/5e9d77fa86a7380414e4fe0f',
        'https://www.dabangapp.com/room/5e8aac2b54de271a14e4c32e',
        'https://www.dabangapp.com/room/5e8ae5ed851dda19ad8b717d',
        'https://www.dabangapp.com/room/5e93d59f0d890e350fde4db7',
        'https://www.dabangapp.com/room/5e86f4b7e302b11c09fae313',
        'https://www.dabangapp.com/room/5e9146a83fb2521b2c49ecee',
        'https://www.dabangapp.com/room/5e8154e74cd9607c21f9d10c',
        'https://www.dabangapp.com/room/5e942123724aac304cd16dc8',
        'https://www.dabangapp.com/room/5e8550aabea97b7a22578734',
        'https://www.dabangapp.com/room/5ea662693c9e104f5334b9e8',
        'https://www.dabangapp.com/room/5ea65c1e2ac2a83cdb7db18d',
        'https://www.dabangapp.com/room/5e7ed445b9ca165a0abe5c37',
        'https://www.dabangapp.com/room/5e814fd64039fb0ab049a6d8',
        'https://www.dabangapp.com/room/5e97d58eaef5dd36e7d0546c',
        'https://www.dabangapp.com/room/5ea672bc6da2bc06b9096894',
        'https://www.dabangapp.com/room/5ea655ca5a16fd43625a5361',
        'https://www.dabangapp.com/room/5e95779ac7ba0c4ad2ccf748',
        'https://www.dabangapp.com/room/5ea6624f028aa74f53fa95e4',
        'https://www.dabangapp.com/room/5e82d5bb15e93834534e5f52',
        'https://www.dabangapp.com/room/5e81884c1e326a0478fe722b',
        'https://www.dabangapp.com/room/5ea126699cd5531b825459c0']

    # 각 게시글 조회 시작
    for post_index, dabang_url in enumerate(url_all_list):
        print('############################################# 다음 url \n')
        print('url 입니다.', dabang_url, '\n')
        driver.get(dabang_url)
        time.sleep(2)

        post_type = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[1]/p/span')
        post_type = post_type.get_attribute('innerText')

        # 상세 더보기 클릭
        try:
            button = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/button')
            driver.execute_script("arguments[0].click();", button)
        except NoSuchElementException:
            pass
        # 방 정보 설명
        description = driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div/div")
        description = description[0].get_attribute("innerText")
        description.replace("\n", "")
        try:
            if '접기' in description:
                description = description.split('접기')

        except IndexError:
            pass

        # 매물 형식
        unrefined_salesform = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[1]/div')
        salesForm = unrefined_salesform[0].get_attribute("innerText")
        salesForm = salesForm.replace('/', ' ')
        salesForm = salesForm.replace('\n', '')
        salesForm = salesForm.split()
        salesType = salesForm[0]  # sales type

        print(salesType)
        print(post_type)
        if salesType == '매매':

            try:
                btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[3]/button')
                driver.execute_script("arguments[0].click();", btn)

                href = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/a')
                href = href.get_attribute('href')
                print(href)
                driver.get(href)
                time.sleep(1)
                # 중개소 정보 더 보기
                companyName = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div')
                print(companyName)
                companyName = companyName.get_attribute('innerText')
                print(companyName)

                address = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[8]/div')
                address = address.get_attribute('innerText')
                print(address)
                managerName = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[2]/div')
                managerName = managerName.get_attribute('innerText')
                print(managerName)
                tel = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[3]/div')
                tel = tel.get_attribute('innerText')
                print(tel)
                companyNumber = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[4]/div')
                companyNumber = companyNumber.get_attribute('innerText')
                print(companyNumber)
                brokerage = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[5]/div')
                brokerage = brokerage.get_attribute('innerText')
                print(brokerage)
                dabangCreated_at = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[6]/div')
                dabangCreated_at = dabangCreated_at.get_attribute('innerText')
                print(dabangCreated_at)
                successCount = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[7]/div')
                successCount = successCount.get_attribute('innerText')
                print(successCount)
                image = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div')
                image = image.get_attribute('class')
                image = image.split(' ')
                image = image[1]
                print(image)
                photo = driver.execute_script(
                    f'return window.getComputedStyle(document.querySelector(".{image}"),":after").getPropertyValue("background")')
                print(photo)
                test_url = re.findall(r'"(.*?)"', photo)
                test_url = test_url[0]
                print(test_url)

            except NoSuchElementException:
                managerName = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/p[1]')
                managerName = managerName.get_attribute('innerText')
                if '(' in managerName:
                    managerName = managerName.split('(')
                    managerName = managerName[0]
                tel = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/p[2]')
                tel = tel.get_attribute('innerText')
                if '-' in tel:
                    tel = tel.replace('-', '')
                companyName = None
                address = None
                test_url = None
                companyNumber = None
                brokerage = None
                dabangCreated_at = None
                successCount = None


        else:

            try:
                btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[4]/button')
                driver.execute_script("arguments[0].click();", btn)

                href = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/a')
                href = href.get_attribute('href')
                print(href)
                driver.get(href)
                time.sleep(1)
                # 중개소 정보 더 보기
                companyName = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div')
                print(companyName)
                companyName = companyName.get_attribute('innerText')
                print(companyName)

                address = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[8]/div')
                address = address.get_attribute('innerText')
                print(address)
                managerName = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[2]/div')
                managerName = managerName.get_attribute('innerText')
                print(managerName)
                tel = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[3]/div')
                tel = tel.get_attribute('innerText')
                print(tel)
                companyNumber = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[4]/div')
                companyNumber = companyNumber.get_attribute('innerText')
                print(companyNumber)
                brokerage = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[5]/div')
                brokerage = brokerage.get_attribute('innerText')
                print(brokerage)
                dabangCreated_at = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[6]/div')
                dabangCreated_at = dabangCreated_at.get_attribute('innerText')
                print(dabangCreated_at)
                successCount = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[7]/div')
                successCount = successCount.get_attribute('innerText')
                print(successCount)
                image = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div')
                image = image.get_attribute('class')
                image = image.split(' ')
                image = image[1]
                print(image)
                photo = driver.execute_script(
                    f'return window.getComputedStyle(document.querySelector(".{image}"),":after").getPropertyValue("background")')
                print(photo)
                test_url = re.findall(r'"(.*?)"', photo)
                test_url = test_url[0]
                print(test_url)

            except NoSuchElementException:
                managerName = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/p[1]')
                managerName = managerName.get_attribute('innerText')
                if '(' in managerName:
                    managerName = managerName.split('(')
                    managerName = managerName[0]
                tel = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/p[2]')
                tel = tel.get_attribute('innerText')
                if '-' in tel:
                    tel = tel.replace('-', '')
                companyName = None
                address = None
                test_url = None
                companyNumber = None
                brokerage = None
                dabangCreated_at = None
                successCount = None
        # button = driver.find_element_by_xpath("/html/body/div[4]/div/div/header/button")
        # driver.execute_script("arguments[0].click();", button)

        broker_ins = Broker.objects.get_or_create(
            companyName=companyName,
            address=address,
            managerName=managerName,
            tel=tel,
            image=test_url,
            companyNumber=companyNumber,
            brokerage=brokerage,
            dabangCreated_at=dabangCreated_at,
            successCount=successCount,
        )
        print(broker_ins)
        # 상세 설명 보기
        driver.get(dabang_url)
        print('--')
        try:
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/button")
            driver.execute_script("arguments[0].click();", button)
        except NoSuchElementException:
            pass

        # 매물 형태
        time.sleep(2)
        print('--')
        salesDepositChar = salesForm[1]
        if salesDepositChar.find('원'):
            salesDepositChar = salesDepositChar.replace('원', '')

        salesdepositInt = salesDepositChar.replace('억', '00000000')
        if salesdepositInt.find('만'):
            salesdepositInt = salesdepositInt.replace('만', '')
        salesdepositInt = int(salesdepositInt)

        try:
            salesmonthlyChar = salesForm[2]

            salesmonthlyInt = salesmonthlyChar.replace('만원', '')
            salesmonthlyInt = int(salesmonthlyInt)

            if salesType == '전세':
                # 전세는 금액이 억, 만원이 붙어 있는 경우가 있어서 이렇게 처리.
                salesdepositInt = salesdepositInt + salesmonthlyInt
                salesDepositChar = salesDepositChar + salesmonthlyChar
        except IndexError:
            salesmonthlyInt = 0
            salesmonthlyChar = ''

        salesform_ins = SalesForm.objects.create(
            type=salesType,
            depositChar=salesDepositChar,
            monthlyChar=salesmonthlyChar,
            depositInt=salesdepositInt,
            monthlyInt=salesmonthlyInt,
        )

        if post_type == "아파트":
            if salesType == "매매":
                address = driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div[3]/div/p')
            else:
                address = driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div[5]/div/p')
        else:
            address = driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div[4]/div/p')
        if not address:
            address = driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div/div/p')

        try:
            address = address[0].get_attribute('innerText')
            if '※' in address:
                address = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[4]/div/p')

                address = address.get_attribute('innerText')
            print('address >>>>>>>>>>>>', address)
        except NoSuchElementException:
            address = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[5]/div/p')
            address = address.get_attribute('innerText')

        # kakao Local API
        url = f'https://dapi.kakao.com/v2/local/search/address.json?query={address}'
        res = requests.get(url, headers={'Authorization': f'KakaoAK {KAKAO_APP_ID}'})
        str_data = res.text
        json_data = json.loads(str_data)
        lat = json_data['documents'][0]['x']
        lng = json_data['documents'][0]['y']
        print(f'lat, lng >>  {lat} {lng}')
        address_ins, __ = PostAddress.objects.get_or_create(
            loadAddress=address,
        )
        print('address_ins', address_ins)

        unrefined_floor = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[1]/div')
        total_floor = unrefined_floor[0].get_attribute('innerText')
        total_floor = total_floor.split('/')
        floor = total_floor[0]

        totalFloor = total_floor[1]
        totalFloor = totalFloor.replace(' ', '')

        areaChar = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[2]/div/span')
        areaChar = areaChar[0].get_attribute('innerText')

        # 평수로 변환하는 버
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[2]/div/button').click()

        unrefined_area = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[2]/div/span')
        supplyAreaChar = unrefined_area[0].get_attribute('innerText')

        supplyAreaInt = supplyAreaChar.split('/')
        supplyAreaInt = supplyAreaInt[1].replace('평', '')

        supplyAreaInt = supplyAreaInt.strip()

        supplyAreaInt = int(supplyAreaInt)

        if post_type == '아파트':
            if salesType == '매매':
                shortRent = False
            else:
                shortRent = driver.find_elements_by_xpath(
                    '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[5]/p')
                shortRent = shortRent[0].get_attribute('innerText')
        else:
            if salesType == '매매':
                shortRent = False
            else:
                shortRent = driver.find_elements_by_xpath(
                    '/html/body/div[1]/div/div[5]/div[2]/div/table/tbody/tr/td[5]/p')
                if not shortRent:
                    shortRent = driver.find_elements_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[4]/p')
                shortRent = shortRent[0].get_attribute('innerText')
        print('shortRent is >>', shortRent)

        if shortRent == '불가능':
            shortRent = False
        else:
            shortRent = True

        # 관리비 클래스
        try:
            if post_type == "아파트":
                management = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[3]')
            else:
                if salesType == "매매":
                    management = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[2]/div/table/tbody/tr/td[2]')
                else:
                    management = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[2]/div/table/tbody/tr/td[3]')
        except NoSuchElementException:
            management = None

        try:
            management = management.get_attribute('innerText')
            management = management.replace('\n', '')
            management = management.replace(' ', '')
            management = management.replace('(', ' ')
            management = management.replace(')', ' ')
            management = management.replace(',', ' ')
            management = management.strip(' ')
            management = management.split(' ')

        except AttributeError:
            pass

        try:
            managementPay = management.pop(0)
            if managementPay.find('만원'):
                managementPay = managementPay.replace('만원', ' ')
                if managementPay == '없음':
                    managementPay = 0
                elif managementPay == '문의':
                    managementPay = 0
                managementPay = float(managementPay)
            else:
                managementPay = 0
            totalFee = managementPay

        except IndexError:
            pass
        except AttributeError:
            pass
        except NameError:
            pass

        # 관리비 마무리

        parkingPay = None
        # 주차비 관련
        try:
            if post_type == "아파트":
                if salesType == "매매":
                    parkingDetail = '가능(무료)'
                    parkingTF = True
                else:
                    parkingDetail = driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[4]/p')
                    parkingDetail = parkingDetail.get_attribute('innerText')
            else:
                if salesType == "매매":
                    try:
                        parkingDetail = driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div[5]/div[2]/div/table/tbody/tr/td[3]")
                    except NoSuchElementException:
                        parkingDetail = driver.find_element_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[3]/p')
                    except IndexError:
                        parkingDetail = driver.find_element_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[3]/p')
                    parkingDetail = parkingDetail.get_attribute('innerText')

                else:
                    try:
                        parkingDetail = driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div[5]/div[2]/div/table/tbody/tr/td[4]/p")
                        parkingDetail = parkingDetail.get_attribute('innerText')
                    except NoSuchElementException:
                        parkingDetail = driver.find_element_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[4]/p')
                        parkingDetail = parkingDetail.get_attribute('innerText')

        except IndexError:
            unrefined_parking = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[4]/p'
            )
            parkingDetail = unrefined_parking[0].get_attribute('innerText')

        except TypeError:
            parkingDetail = '불가'
        if '만' in parkingDetail:
            parkingDetail = parkingDetail.split('만')
            parkingDetail = parkingDetail[0]
            parkingPay = float(parkingDetail)
            parkingDetail = '문의'

        # parking Tf
        if parkingDetail == '가능(무료)':
            parkingTF = True
        elif parkingDetail == '문의':
            parkingTF = True
        else:
            parkingTF = False
        print('parking >>>>>>>>>>>>>', parkingDetail, parkingTF, parkingPay)
        try:
            if not salesType == "매매":
                if post_type == "아파트":
                    unrefined_living_expenses = driver.find_elements_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[3]/div/div/div/label')
                    unrefined_living_expenses_detail = driver.find_elements_by_xpath(
                        '/html/body/div[1]/div/div[5]/div[3]/div/div/div/span')
                else:
                    try:
                        unrefined_living_expenses = driver.find_elements_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[2]/div/div/div/label')
                        unrefined_living_expenses_detail = driver.find_elements_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[2]/div/div/div/span')
                    except NoSuchElementException:
                        unrefined_living_expenses = driver.find_elements_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[3]/div/div/div/label')
                        unrefined_living_expenses_detail = driver.find_elements_by_xpath(
                            '/html/body/div[1]/div/div[5]/div[3]/div/table/tbody/tr/td[3]/p[2]/span')
            else:
                living_expenses = None
                living_expenses_detail = None
        except NoSuchElementException:
            pass

        # 생활비 , 생활비 항목들
        try:
            unrefined_living_expenses = unrefined_living_expenses[0].get_attribute('innerText')
            living_expenses = unrefined_living_expenses.replace(' ', '')
            living_expenses_detail = unrefined_living_expenses_detail[0].get_attribute('innerText')

        except IndexError:
            unrefined_living_expenses = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[3]/div/div/div/label'
            )
            unrefined_living_expenses_detail = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[3]/div/div/div/span')
            unrefined_living_expenses = unrefined_living_expenses[0].get_attribute('innerText')
            living_expenses = unrefined_living_expenses.replace(' ', '')
            living_expenses_detail = unrefined_living_expenses_detail[0].get_attribute('innerText')
        except TypeError:
            print('생활비 항목 타입 에러')
        except NameError:
            print('생활비 항목 이름 에러')
        except AttributeError:
            print(unrefined_living_expenses, "가 없")

        if salesType == "매매":
            if post_type == "아파트":
                moveInChar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[7]/div')
            else:
                moveInChar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[7]/div')
        else:
            if post_type == "아파트":
                moveInChar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[9]/div')
            else:
                moveInChar = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[9]/div')

        moveInChar = moveInChar.get_attribute('innerText')
        moveInDate = None
        if '날짜' in moveInChar:
            pass
        elif '즉시' in moveInChar:
            pass
        elif '2' in moveInChar:
            moveInChar = moveInChar.replace('.', '-')
            moveInDate = moveInChar
            moveInChar = '날짜 협의'
        else:
            moveInChar = '날짜 협의'

        print(moveInChar)

        # option & sceurity
        try:
            option_tag = driver.find_element_by_name('option')
            option_tag = option_tag.get_attribute('innerText')
            option_tag = option_tag.split('보안/안전시설')
            print('option tag >> ', option_tag)
            option = option_tag[0]
            option = option.split('\n\n')
            print(option)
            del option[0]
            del option[-1]
            print(option)

            print('result option', option)

            security = option_tag[1]
            security = security.split('\n\n')
            del security[-1]
            del security[0]
            print('result security', security)
        except IndexError:
            print('안전 시설 없음.')
            security = None
        except NoSuchElementException:
            print('옵션, 안전시설 없음', url)
            option = None
            security = None

        # Room option instance create
        if option is not None:
            option_list = []
            # POSTS_IMAGE_DIR = os.path.join(MEDIA_ROOT, f'.posts/.option/')
            for option_name in option:
                # f = open(os.path.join(POSTS_IMAGE_DIR, f'{option_name}.png'), 'rb')
                ins = OptionItem.objects.get_or_create(
                    name=option_name,
                    # image=File(f),
                )
                # f.close()

                option_list.append(ins[0])

        # Security option instance create
        if security is not None:
            # POSTS_IMAGE_DIR = os.path.join(MEDIA_ROOT, f'.posts/.security/')
            security_list = []
            print('안전 시설은 ', security)

            for security_name in security:
                # f = open(os.path.join(POSTS_IMAGE_DIR, f'{security_name}.png'), 'rb')
                ins = SecuritySafetyFacilities.objects.get_or_create(
                    name=security_name,
                    # image=File(f),
                )
                # f.close()

                security_list.append(ins[0])
                print('security >>>', ins[0])

        heatingType = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[3]/div')
        heatingType = heatingType.get_attribute('innerText')

        if salesType == "매매":
            if post_type == "아파트":
                pet = True
            else:
                pet = True
        else:
            if post_type == "아파트":
                pet = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[7]/div')
            else:
                pet = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[6]/div')
            pet = pet.get_attribute('innerText')
            if pet == "불가능":
                pet = False
            else:
                pet = True

        if post_type == "아파트":
            elevator = True
        else:
            elevator = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[5]/div')
            elevator = elevator.get_attribute('innerText')
            if elevator == "있음":
                elevator = True
            else:
                elevator = False

        if post_type == "아파트":
            builtIn = True
        else:
            builtIn = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[4]/div')
            builtIn = builtIn.get_attribute('innerText')
            if builtIn == "아님":
                builtIn = False
            else:
                builtIn = True
        # 베란다
        if post_type == "아파트":
            veranda = True
        else:
            if salesType == '매매':
                veranda = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[6]/div')
                veranda = veranda.get_attribute('innerText')
                if veranda == "있음":
                    veranda = True
                else:
                    veranda = False
            else:
                veranda = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[7]/div')
                veranda = veranda.get_attribute('innerText')
                if veranda == '있음':
                    veranda = True
                else:
                    veranda = False
        # depositLoan 전세 대출 자금
        if post_type == '아파트':
            if salesType == '매매':
                depositLoan = True
            else:
                depositLoan = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[8]/div')
                depositLoan = depositLoan.get_attribute('innerText')
                if depositLoan == '가능':
                    depositLoan = True
                else:
                    depositLoan = False
        else:
            if salesType == '매매':
                depositLoan = True
            else:
                depositLoan = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[8]/div')
                depositLoan = depositLoan.get_attribute('innerText')
                if depositLoan == '가능':
                    depositLoan = True
                else:
                    depositLoan = False

        # totalCitizen
        if post_type == '아파트':
            totalCitizen = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[5]/div')
            totalCitizen = totalCitizen.get_attribute('innerText')
        else:
            totalCitizen = None

        if post_type == "아파트":
            totalPark = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[6]/div')
            totalPark = totalPark.get_attribute('innerText')
        else:
            totalPark = None

        if post_type == "아파트":
            totalPark = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[6]/div')
            totalPark = totalPark.get_attribute('innerText')
        else:
            totalPark = None

        # 준공 완료일
        if post_type == '아파트':
            complete = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[4]/div')
            complete = complete.get_attribute('innerText')
        else:
            complete = None

        # 아파트 단지정보 크롤링 시작
        if post_type == '아파트':
            complex_detail_url = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[2]/div/a')
            complex_detail_url = complex_detail_url.get_attribute('href')
            driver.get(complex_detail_url)
            time.sleep(2)
            apart_name = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/h1')
            apart_name = apart_name.get_attribute('innerText')
            print('apart_name', apart_name)

            made = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[1]/p[2]')
            made = made.get_attribute('innerText')
            print('made', made)

            total_citizen = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[2]/p[2]')
            total_citizen = total_citizen.get_attribute('innerText')
            print('total_citizen', total_citizen)

            personal_park = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[3]/p[2]')
            personal_park = personal_park.get_attribute('innerText')
            if ' ' in personal_park:
                personal_park = personal_park.split(' ')
                personal_park = personal_park[1]
            print('personal_park', personal_park)

            # 총 동 수
            total_number = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[4]/p[2]')
            total_number = total_number.get_attribute('innerText')
            print('total_number', total_number)

            heating_system = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[5]/p[2]')
            heating_system = heating_system.get_attribute('innerText')
            print('heating_system', heating_system)

            min_max_floor = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[6]/p[2]')
            min_max_floor = min_max_floor.get_attribute('innerText')
            print('min_max_floor', min_max_floor)

            buildingType = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]')
            buildingType = buildingType.get_attribute('innerText')
            print('buildingType', buildingType)

            constructionCompany = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[2]/div/table/tbody/tr[1]/td[2]')
            constructionCompany = constructionCompany.get_attribute('innerText')
            print('constructionCompany', constructionCompany)

            fuel = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[1]/td[4]')
            fuel = fuel.get_attribute('innerText')
            print('fuel', fuel)

            complex_type = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[2]/td[1]')
            complex_type = complex_type.get_attribute('innerText')
            print('complex_type', complex_type)

            # 용적률
            floorAreaRatio = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[2]/td[2]')
            floorAreaRatio = floorAreaRatio.get_attribute('innerText')
            print('floorAreaRatio', floorAreaRatio)

            # 건폐율
            dryWasteRate = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr[2]/td[3]')
            dryWasteRate = dryWasteRate.get_attribute('innerText')
            print('dryWasteRate', dryWasteRate)

            # 단지평당가 매매
            complexSale = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[1]/div/div/div/div[1]/p[3]')
            complexSale = complexSale.get_attribute('innerText')
            print('complexSale', complexSale)

            # 단지평당가 전세
            complexPrice = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[1]/div/div/div/div[1]/p[5]')
            complexPrice = complexPrice.get_attribute('innerText')
            print('complexPrice', complexPrice)

            areaSale = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[1]/div/div/div/div[2]/p[3]')
            areaSale = areaSale.get_attribute('innerText')
            print('areaSale', areaSale)

            areaPrice = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[1]/div/div/div/div[2]/p[5]')
            areaPrice = areaPrice.get_attribute('innerText')
            print('areaPrice', areaPrice)

            div_list = driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div/div')

            complex_image_list = []

            for i, url in enumerate(div_list):
                try:
                    cls_name = url.get_attribute('class')
                    cls_name = cls_name.split(' ')
                    cls_name = cls_name[1]
                    photo = driver.execute_script(
                        f'return window.getComputedStyle(document.querySelector(".{cls_name}"),":after").getPropertyValue("background")')
                    recommend_image = re.findall(r'"(.*?)"', photo)
                    complex_image_list.append(recommend_image[0])
                except IndexError:
                    pass

            print('complex_image_list >>', complex_image_list)
            complex_obj, __ = ComplexInformation.objects.get_or_create(
                complexName=apart_name,
                buildDate=made,
                totalCitizen=total_citizen,
                personalPark=personal_park,
                totalNumber=total_number,
                heatingSystem=heating_system,
                minMaxFloor=min_max_floor,
                buildingType=buildingType,
                constructionCompany=constructionCompany,
                fuel=fuel,
                complexType=complex_type,
                floorAreaRatio=floorAreaRatio,
                dryWasteRate=dryWasteRate,
                complexSale=complexSale,
                complexPrice=complexPrice,
                areaSale=areaSale,
                areaPrice=areaPrice,
            )
            print(complex_obj)
            for index, image in enumerate(complex_image_list):
                try:
                    COMPLEX_IMAGE_DIR = os.path.join(MEDIA_ROOT, f'.posts/complex{complex_obj.pk}/')
                    if not os.path.exists(COMPLEX_IMAGE_DIR):
                        os.makedirs(COMPLEX_IMAGE_DIR, exist_ok=True)

                    # 이미지 생성
                    image_save_name = os.path.join(COMPLEX_IMAGE_DIR, f'{index}.jpg')
                    urllib.request.urlretrieve(image, image_save_name)
                    f = open(os.path.join(COMPLEX_IMAGE_DIR, f'{index}.jpg'), 'rb')
                    ComplexImage.objects.create(
                        image=File(f),
                        complex=complex_obj,
                    )
                    f.close()
                except FileExistsError:
                    print('이미 존재하는 파일')
            time.sleep(1)
            # 추천 단지 시작
            # 아파트 단지 이미지 div
            recommend_div_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/div')
            # 추천 단지 아파트 이름
            recommend_apat_name_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/p[1]')
            # 추천 단지 아파트
            recommend_apat_type_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/p[2]/span[1]')
            # 추천 단지 총 세대 수
            recommend_apat_total_citizen_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/p[2]/span[2]')
            # 추천 단지 설립일자 리스트
            recommend_apat_build_date_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/p[2]/span[3]')
            # 추천 단지 주소 리스트
            recommend_apat_address_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/div/a/p[3]')
            # 추천 단지 정보 링크 리스트
            recommend_apat_link_list = driver.find_elements_by_xpath(
                '/html/body/div[1]/div/div[5]/div[8]/div/ul/li/ul/li/a')

            for i, url in enumerate(recommend_div_list):
                cls_name = url.get_attribute('class')
                cls_name = cls_name.split(' ')
                cls_name = cls_name[1]

                photo = driver.execute_script(
                    f'return window.getComputedStyle(document.querySelector(".{cls_name}"),":before").getPropertyValue("background")')
                recommend_image_url = re.findall(r'"(.*?)"', photo)
                print('추천단지 이미지', recommend_image_url[0])
                recommend_apat_name = recommend_apat_name_list[i].get_attribute('innerText')
                print('추천단지 아파트 이름', recommend_apat_name)
                recommend_apat_type = recommend_apat_type_list[i].get_attribute('innerText')
                print('추천단지 아파트 타입', recommend_apat_type)
                recommend_apat_total_citizen = recommend_apat_total_citizen_list[i].get_attribute('innerText')
                print('추천 단지 총 세대 수', recommend_apat_total_citizen)
                recommend_apat_build_date = recommend_apat_build_date_list[i].get_attribute('innerText')
                print('추천 단지 설립 일자', recommend_apat_build_date)
                recommend_apat_address = recommend_apat_address_list[i].get_attribute('innerText')
                print('추천 단지 주소', recommend_apat_address)
                recommend_apat_link = recommend_apat_link_list[i].get_attribute('href')
                print('추천 단지 해당 링크', recommend_apat_link)

                # 이미지 생성
                try:
                    RECOMMEND_IMAGE_DIR = os.path.join(MEDIA_ROOT,
                                                       f'.posts/{apart_name}/')
                    if not os.path.exists(RECOMMEND_IMAGE_DIR):
                        os.makedirs(RECOMMEND_IMAGE_DIR, exist_ok=True)

                    # 이미지 생성
                    image_save_name = os.path.join(RECOMMEND_IMAGE_DIR, f'{recommend_apat_name}.jpg')
                    urllib.request.urlretrieve(recommend_image_url[0], image_save_name)
                    f = open(os.path.join(RECOMMEND_IMAGE_DIR, f'{recommend_apat_name}.jpg'), 'rb')
                    RecommendComplex.objects.get_or_create(
                        complex=complex_obj,
                        image=File(f),
                        name=recommend_apat_name,
                        type=recommend_apat_type,
                        totalCitizen=recommend_apat_total_citizen,
                        buildDate=recommend_apat_build_date,
                        address=recommend_apat_address,
                        link=recommend_apat_link,
                    )
                    f.close()

                except FileExistsError:
                    print('이미 존재하는 파일')
                #

                print('\n')
        driver.get(dabang_url)
        time.sleep(1)
        # 아파트 단지 정보 종료.

        post = PostRoom.objects.get_or_create(
            broker=broker_ins[0],
            complex=complex_obj,
            type=post_type,
            description=description,
            address=address_ins,
            salesForm=salesform_ins,
            lat=lat,
            lng=lng,
            floor=floor,
            totalFloor=totalFloor,
            areaChar=areaChar,
            supplyAreaChar=supplyAreaChar,
            supplyAreaInt=supplyAreaInt,
            shortRent=shortRent,
            parkingDetail=parkingDetail,
            parkingTF=parkingTF,
            parkingPay=parkingPay,
            living_expenses=living_expenses,
            living_expenses_detail=living_expenses_detail,
            moveInChar=moveInChar,
            moveInDate=moveInDate,
            heatingType=heatingType,
            pet=pet,
            elevator=elevator,
            builtIn=builtIn,
            veranda=veranda,
            depositLoan=depositLoan,
            totalCitizen=totalCitizen,
            totalPark=totalPark,
            complete=complete,
        )
        if management is not None:
            admin_instance_list = []
            for obj in management:
                admin_ins = AdministrativeDetail.objects.get_or_create(
                    name=obj,
                )
                admin_instance_list.append(admin_ins[0])
        else:
            admin_instance_list = None

        if admin_instance_list is not None:
            for ins in admin_instance_list:
                print('admin_instance_list : ins >>', ins)
                MaintenanceFee.objects.create(
                    postRoom=post[0],
                    totalFee=totalFee,
                    admin=ins,
                )

        if option is not None:
            for ins in option_list:
                RoomOption.objects.create(
                    postRoom=post[0],
                    option=ins,

                )
                print(ins)
        if security is not None:
            for ins in security_list:
                RoomSecurity.objects.create(
                    postRoom=post[0],
                    security=ins,

                )

        div_list = driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div')

        image_list = []

        for i, url in enumerate(div_list):
            cls_name = url.get_attribute('class')
            cls_name = cls_name.split(' ')
            cls_name = cls_name[1]
            photo = driver.execute_script(
                f'return window.getComputedStyle(document.querySelector(".{cls_name}"),":after").getPropertyValue("background")')

            test_url = re.findall(r'"(.*?)"', photo)

            # 이미지 파일이 아닌 url를 뺀 새로운 url list
            if test_url:
                if 'dabang' in test_url[0]:
                    pass
                else:
                    image_list.append(test_url[0])
            else:
                print('빈 리스트')

        if image_list:
            for index, image_url in enumerate(image_list):
                print('image_url>> ', image_url)
                try:
                    POSTS_IMAGE_DIR = os.path.join(MEDIA_ROOT, f'.posts/postroom{post[0].pk}/')
                    if not os.path.exists(POSTS_IMAGE_DIR):
                        os.makedirs(POSTS_IMAGE_DIR, exist_ok=True)

                    # 이미지 생성
                    image_save_name = os.path.join(POSTS_IMAGE_DIR, f'{index}.jpg')
                    urllib.request.urlretrieve(image_url, image_save_name)
                    f = open(os.path.join(POSTS_IMAGE_DIR, f'{index}.jpg'), 'rb')
                    PostImage.objects.get_or_create(
                        image=File(f),
                        post=post[0],
                    )
                    f.close()
                except FileExistsError:
                    print('이미 존재하는 파일')

        # print('이미지 업로드 끝')
        print('게시글 하나 크롤링 완성 pk:', post_index, '-========================================== \n ')

    driver.close()
