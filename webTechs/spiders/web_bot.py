import scrapy
from ..items import WebtechsItem
from datetime import datetime
from scrapy_selenium import SeleniumRequest
import os
from selenium import webdriver
from scrapy.utils.project import get_project_settings

class WebBotSpider(scrapy.Spider):
    name = 'web_bot'
    
    def start_requests(self):
        list_cate = ["Advertising","Analytics","Tracker","JavaScript","Domain Parking","Blog","Feedback and Surveys","Polls and Quizzes","Call Tracking","Login Provider","Site Search","Multilingual","Push Notifications","Cryptocurrency","Information Technology","API","Marketing","Widget","Privacy","Content Delivery Network","Audio Video Media","Live Chat","Customer Communication","Customer Relationship Management","Booking","Trading Platforms","Social","Business Solutions","Advocacy","Other","Document Standard","ECommerce","Recruitment","Security","Content Management System","Finance","Comments System","Server","Online Forms","Email Services","Mobile","Tutorials and Onboarding"]
        list_url = []
        for item in list_cate:
            url = 'https://www.similartech.com/categories/' + str(item).replace(" ", "-")
            list_url.append(url)
        for item in list_url:
            count = 0
            settings= get_project_settings()
            driver_path = 'E:\Data-web-technologies\chromedriver.exe'
            options= webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(driver_path, options=options)
            driver.get(item)
            link_elements = driver.find_elements_by_xpath('//*[@class="table-list"]//a[text()]')
            for link in link_elements:
                if count<100:
                    count+=1
                    link = link.get_attribute('href')
                    yield SeleniumRequest(
                        url = link,
                        wait_time = 2,
                        callback = self.parse
                    )
                else:
                    continue
            driver.quit()

    def parse(self, response):
        now = datetime.now()
        # Ngày lấy dữ liệu
        Date = now.strftime("%d/%m/%Y")

        
        """ Chuyển đến thư mục Result """
        path = os.getcwd()
        if "Result" not in path:
            path = path + "\Result"
            os.chdir(path)

        check = str(response.xpath("//div[@class='row'][2]/div[2]/h1/text()").get()).strip()
        namefile = check.strip().replace(" ", "-") + ".csv"
        check_file = str(os.listdir())
        if ("None.csv"!=namefile) or (namefile not in check_file):

            """ Crawl dữ liệu """
            ##### Thông tin cơ bản
            # Tên
            NameTechnology = check
            # Số lượng websites
            Websites = str(response.xpath("//div[@class='kpi-cell'][1]/div/strong/span/text()").get()).strip().replace("\n", "").replace(" ", "").replace(",", "")
            # Sự thay đổi trong 1 tháng
            P1month = str(response.xpath("//div[@class='kpi-cell'][1]/div/strong/span[2]/span/text()").get()).strip().replace("\n", "").replace(" ", "").replace(",", "") + "%"
            # domain
            UniqueDomains = str(response.xpath("//div[@class='kpi-cell'][2]/div/strong/text()").get()).strip().replace("\n", "").replace(" ", "").replace(",", "")
            # Thể loại của web
            TechCategory = response.xpath('//div[@class="col-md-12"][1]/div/ol/li[3]/a/span/text()').get()
            ##### Mở rộng
            # Các ngành hàng đầu ( iv = Industry Vertical )
            try:
                iv1 = str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[2]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[2]/td[2]/em/text()').get()).replace(",", "")
                try:
                    if len(iv1)<2:
                        iv1 = str(response.xpath('//div[@class="cmp-legend"]/table/tr[2]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tr[2]/td[2]/em/text()').get()).replace(",", "")
                except:
                    pass
            except:
                iv1 = ""
            try:
                iv2 = str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[3]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[3]/td[2]/em/text()').get()).replace(",", "")
                try:
                    if len(iv2)<2:
                        iv2 = str(response.xpath('//div[@class="cmp-legend"]/table/tr[3]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tr[3]/td[2]/em/text()').get()).replace(",", "")
                except:
                    pass
            except:
                iv2 = ""
            try:
                iv3 = str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[4]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[4]/td[2]/em/text()').get()).replace(",", "")
                try:
                    if len(iv3)<2:
                        iv3 = str(response.xpath('//div[@class="cmp-legend"]/table/tr[4]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tr[4]/td[2]/em/text()').get()).replace(",", "")
                except:
                    pass
            except:
                iv3 = ""
            try:
                iv4 = str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[5]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[5]/td[2]/em/text()').get()).replace(",", "")
                try:
                    if len(iv4)<2:
                        iv4 = str(response.xpath('//div[@class="cmp-legend"]/table/tr[5]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tr[5]/td[2]/em/text()').get()).replace(",", "")
                except:
                    pass
            except:
                iv4 = ""
            try:
                iv5 = str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[6]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tbody/tr[6]/td[2]/em/text()').get()).replace(",", "")
                try:
                    if len(iv5)<2:
                        iv5 = str(response.xpath('//div[@class="cmp-legend"]/table/tr[6]/td[1]/label/text()').get()) + ",,," + str(response.xpath('//div[@class="cmp-legend"]/table/tr[6]/td[2]/em/text()').get()).replace(",", "")
                except:
                    pass
            except:
                iv5 = ""
            # Công nghệ liên quan ( rt = Related Technologies )
            RelatedTechnologiesInfo = response.xpath('//div[@class="col-md-5 cmp-leaders-list"]/div/div/p/text()').get()
            rt1 = str(response.xpath('//table[@class="legend alt-rows large"]/tbody/tr[1]/td/a/span/text()').get())
            rt2 = str(response.xpath('//table[@class="legend alt-rows large"]/tbody/tr[2]/td/a/span/text()').get())
            rt3 = str(response.xpath('//table[@class="legend alt-rows large"]/tbody/tr[3]/td/a/span/text()').get())
            rt4 = str(response.xpath('//table[@class="legend alt-rows large"]/tbody/tr[4]/td/a/span/text()').get())
            rt5 = str(response.xpath('//table[@class="legend alt-rows large"]/tbody/tr[5]/td/a/span/text()').get())
            # Những trang web sửa dụng nhiều
            count_web_using_tech = response.xpath('//div[@class="col-md-12 list-group condensed"]').extract()
            count_web_using_tech = str(count_web_using_tech)
            count_web_using_tech = count_web_using_tech.replace('row list-item-block',"~")
            count = 0
            for item in count_web_using_tech:
                if item == "~":
                    count+=1
            topweb = []
            for x in range(1,count):
                web = str(response.xpath(f'//div[@class="col-md-12 list-group condensed"]/div[{x}]/div/h4/a/span/text()').get())+",,Monthly visits ->,,"+str(response.xpath(f'//div[@class="col-md-12 list-group condensed"]/div[{x}]/div[3]/em/text()').get())+"\n"
                topweb.append(web)
            # Những quốc gia sử dụng nhiều
            count_countries_using_tech = response.xpath('//div[@class="cmp-legend geo-legend"]').extract()
            count_countries_using_tech = str(count_countries_using_tech)
            count_countries_using_tech = count_countries_using_tech.replace('<tr>',"~")
            count = 0
            for item in count_countries_using_tech:
                if item == "~":
                    count+=1
            topcountries = []
            for x in range(2,count+1):
                country = str(response.xpath(f'//div[@class="cmp-legend geo-legend"]/table/tbody/tr[{x}]/td[1]/label/text()').get()) + ",,,"+str(response.xpath(f'//div[@class="cmp-legend geo-legend"]/table/tbody/tr[{x}]/td[2]/em/text()').get()).replace(",", "")+"\n"
                topcountries.append(country)

            """ Dữ liệu ghi vào file kết quả """
            # Thông tin cơ bản
            info = f"- Basic Information about Technology -\nCrawl date,,{Date}\nTechnology,,{NameTechnology}\nLast month's change,,{P1month}\nWebsites,,{Websites}\nUnique Domains,,{UniqueDomains}\n" + "-"*38 + "\n\n"
            # Các ngành hàng đầu
            TopIndustryVerticals = f"\n- Top Industry Verticals -\nIndustry verticals where {NameTechnology} is being used\n{iv1}\n{iv2}\n{iv3}\n{iv4}\n{iv5}\n\n"
            # Công nghệ liên quan
            RelatedTechnologies = f"\n- Related Technologies -\n{RelatedTechnologiesInfo}\n{rt1}\n{rt2}\n{rt3}\n{rt4}\n{rt5}\n\n"
            # Các trang web sử dụng công nghệ
            TopWebsitesUsingTechnology = f"\n- Top Websites Using {NameTechnology} -\n"
            for item in topweb:
                TopWebsitesUsingTechnology = TopWebsitesUsingTechnology + item
            # Các quốc gia sử dụng nhiều nhất
            MostUsedCountries = f'\n- Geography -\n{NameTechnology} usage by websites across the globe\nLeading Countries,,,Websites\n'
            for item in topcountries:
                MostUsedCountries = MostUsedCountries + item
            
            
            """ Tạo file chứa toàn bộ dữ liệu """
            file = open(namefile, 'w', encoding='UTF-8')
            file.write(info)
            file.write(TopIndustryVerticals)
            file.write(RelatedTechnologies)
            file.write(TopWebsitesUsingTechnology)
            file.write(MostUsedCountries)
            file.close()  

            item = WebtechsItem()
            item["Date"] = Date
            item["NameTechnology"] = NameTechnology
            item["Websites"] = Websites
            item["P1month"] = P1month
            item["UniqueDomains"] = UniqueDomains
            item["TechCategory"] = TechCategory
            yield item