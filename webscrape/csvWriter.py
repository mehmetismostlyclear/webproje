from ast import Try
from codecs import ignore_errors
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import requests
import pandas as pd

class csvWriter:
    def __init__(self, bundlelinks=None,bbclinks=None,hurriyetlinks=None,donanimlinks=None,ekonomimlinks=None,gazeteoksijenlinks=None
                 ,bloomberghtlinks=None,kayiprihtimlinks=None,getmidaslinks=None,ntvlinks=None,haberturklinks=None, milliyetlinks=None):
        self.bundlelinks = bundlelinks
        self.bbclinks = bbclinks
        self.hurriyetlinks = hurriyetlinks
        self.donanimlinks = donanimlinks
        self.ekonomimlinks = ekonomimlinks
        self.gazeteoksijenlinks = gazeteoksijenlinks
        self.bloomberghtlinks=bloomberghtlinks
        self.kayiprihtimlinks=kayiprihtimlinks
        self.getmidaslinks=getmidaslinks
        self.haberturklinks=haberturklinks    
        self.ntvlinks=ntvlinks
        self.milliyetlinks=milliyetlinks
        self.sourcelist = []
        self.df = pd.DataFrame(columns=['source', 'content'])
    def bundletextGenerate(self):
        for link in self.bundlelinks:

            try:
                response = requests.get(link)
                response.raise_for_status()  # Yanıt durumu 4xx veya 5xx ise istisna fırlatılır.
                html = response.text
                soup = BeautifulSoup(html , 'html.parser')
                #icergi al
                divisionText = soup.findChild('div', {'class': 'bundleXPathBody'})
                try:
                    divisionText = divisionText.get_text()
                except:
                    divisionText = soup.findChild('div', {'class': 'bundleRssBody'})
                    try:
                        divisionText = divisionText.get_text()
                    except:
                        divisionText="sonuc yok"
                
                #kaynag� al
                sourceText = soup.findChild('p', {'class': 'detailNewsReadText'})
            
                try:
                    source = sourceText.find('a')
                    source = source['href']
                    sonuc = re.search(r'(www|tr)?\.(.*?)\.com', source).group(2)

                except AttributeError:
                    parsed_url = urlparse(source)
                    sonuc = parsed_url.netloc
                    print("Eslesme domain ile bulundu.")
                    print(link)
                self.df = pd.concat([self.df, pd.DataFrame({'source': [sonuc], 'content': [str(divisionText)]})])

                
                # İşlem başarılı olduysa burada istediğiniz işlemleri gerçekleştirebilirsiniz.
    
            except requests.exceptions.RequestException as e:
            # Talep sırasında bir hata oluştuğunda bu blok çalışır.
                print("Hata oluştu:", e)
                print(link)


    def bbctextGenerate(self):
        for link in self.bbclinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChildren('div',{'class':"bbc-19j92fr ebmt73l0"})
            alltext=""
            for text in divisionText:
                ptext=text.findChildren('p',{'class':'bbc-hhl7in e17g058b0'})
                for i in ptext:
                    text=i.get_text()
                    alltext+=text
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['bbcturk'], 'content': [alltext]})])

            
    def hurriyettextGenerate(self):
        for link in self.hurriyetlinks:
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':"news-content readingTime"})
            try:
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                alltext="sonucyok"
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['hurriyet'], 'content': [alltext]})])

                
    def donanimtextGenerate(self):
        for link in self.donanimlinks: 
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('section',{'class':"kolon yazi"})
            try:
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text() 
                    alltext+=text
            except:
                divisionText="sonuç yok"
                alltext="veri yok"

            self.df = pd.concat([self.df, pd.DataFrame({'source': ['donanimhaber'], 'content': [alltext]})])          
    def ekonomimtextGenerate(self):
        for link in self.ekonomimlinks:
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':"content-text"})
            try:
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                divisionText="sonuc bulunamadı"

            self.df = pd.concat([self.df, pd.DataFrame({'source': ['ekonomim.haber'], 'content': [alltext]})])
                
     
    def gazeteoksijentextGenerator(self):
        for link in self.gazeteoksijenlinks:
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            link = link.split('?')[0]
            divisionText=soup.findChild('div',{'data-url':link})
            try:
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                divisionText="sonuc yok"
                alltext="sonucyok"

            self.df = pd.concat([self.df, pd.DataFrame({'source': ['gazetoksijen'], 'content': [alltext]})])
    def bloomberghttextGenerator(self):
        for link in self.bloomberghtlinks:
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            match = re.search(r'(//)([^?]+)', link)
            match=match.group(2)
            match=re.search(r'\/([^/]+)$', match)
            match=match.group(1)
            divisionText=soup.findChild('div',{'data-url':'/'+match})
            try:
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                divisionText="sonucyok"
                alltext="sonucyok"
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['bloomberght'], 'content': [alltext]})])
    def kayiprihtimtextGenerator(self):
        for link in self.kayiprihtimlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':'entry-inner'})
            try:
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                alltext="veri yok"

    def getmidastextGenerator(self):
        for link in self.getmidaslinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('article',{'class':'blog-detail-content'})
            divisionText=divisionText.find_all('p')
            for i in divisionText:
                text=i.get_text()
                alltext+=text
            
    def haberturktextGenerator(self):
        for link in self.haberturklinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':'wrapper px-5 overflow-hidden'})
            divisionText=divisionText.find_all('p')
            for i in divisionText:
                text=i.get_text()
                alltext+=text
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['haberturk'], 'content': [alltext]})])
            
    def ntvtextGenerator(self):
        for link in self.ntvlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':'content-news-tag-selector'})
            divisionText=divisionText.find_all('p')
            for i in divisionText:
                text=i.get_text()
                alltext+=text
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['NTV'], 'content': [alltext]})])
    def milliyettextGenerator(self):
        for link in self.ntvlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChild('div',{'class':'news-content news-content readingTime'})
            divisionText=divisionText.find_all('p')
            for i in divisionText:
                text=i.get_text()
                alltext+=text
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['NTV'], 'content': [alltext]})])


    def write_list_to_csv(self):
        self.df.to_csv('11-3-2023.csv', index=False)
        