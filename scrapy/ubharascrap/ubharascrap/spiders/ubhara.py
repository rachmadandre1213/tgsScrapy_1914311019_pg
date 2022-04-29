import scrapy


class UbharaSpider(scrapy.Spider):
    name = 'ubhara'
    start_urls = ['https://www.ubhara.ac.id/v3/p/kemahasiswaan']

    def parse(self, response):
        a = response.css('div.panel')
        judul = []
        isi = []
        for ab in a.css('div.panel-heading'):
            if ab.css('h3::text').get() != None:
                judul.append(ab.css('h3::text').get())
        for ba in a.css('ul'):
            tempo = []
            for bb in ba.css('li'):
                tempo.append(bb.css('li::text').get())
            isi.append(tempo)

        for a in range(5):
            yield{
                'judul': judul[a],
                'isi': isi[a]
            }
