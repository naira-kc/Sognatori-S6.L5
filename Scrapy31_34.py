### Utilizzo di Scrapy

#31. Scrivi uno spider Scrapy che estragga i titoli da una pagina web.

import scrapy

class DigiChampsSpider(scrapy.Spider):
    name = 'DigiChamps'
    start_urls = ['https://www.campus-digitale.it/digichamps/']

    def parse(self, response):
        new_titles = response.css('h3').getall()
        # Il resto del tuo codice qui
        DigiChamps_data = {'titles': new_titles}
        

#32. Estrai tutti i link da una pagina web utilizzando Scrapy.

import scrapy

class LinksSpider(scrapy.Spider):
    name = "Wiki32"
    start_urls = ["https://it.wikipedia.org/wiki/India"]

    def parse(self,response):
        links = response.css("a").getall()
        for link in links:
            yield{
                "url":link
                }
        for next_page in links:
            yield response.follow(next_page, callback = self.parse)
            

#33. Crea uno spider Scrapy che pagini attraverso un sito di e-commerce.

import scrapy

class LinksSpider(scrapy.Spider):
    name = "ebaylinks"
    start_urls = ["https://www.ebay.it/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=roma&_sacat=0&_odkw=41"]

    def parse(self,response):
        links = response.css("a::attr(href)").getall()
        for link in links:
            yield{
                "url":link
                }
        for next_page in links:
            yield response.follow(next_page, callback = self.parse)
            



#34. Estrai e salva in un file JSON i dati estratti da uno spider Scrapy.

import scrapy
import json

class HeavenSpider(scrapy.Spider):
    name = 'Heaven_spider'
    start_urls = ['https://heavengroup.it/']

    def parse(self, response):

        new_titles = response.css('h2').getall()

        json_data = {'titles': new_titles}
        with open('Heaven.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=2)

        for title in new_titles:
            self.log(title)

            