from ast import Try
from codecs import ignore_errors
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import requests
import pandas as pd

class csvWriter:
    def __init__(self):
        self.df = pd.DataFrame(columns=['source', 'content'])
    def htmlbeautrequest(self, link):
        response = requests.get(link)
        response.raise_for_status()  # Yanıt durumu 4xx veya 5xx ise istisna fırlatılır.
        html = response.text
        soup = BeautifulSoup(html , 'html.parser')
        return soup
    def bundletextGenerate(self,links):
        for link in links:
            

            try:
                soup=self.htmlbeautrequest(link)
                
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


    def bbctextGenerate(self,links):
        for link in links:
            soup=self.htmlbeautrequest(link)
            divisionText=soup.findChildren('div',{'class':"bbc-19j92fr ebmt73l0"})
            alltext=""
            for text in divisionText:
                ptext=text.findChildren('p',{'class':'bbc-hhl7in e17g058b0'})
                for i in ptext:
                    text=i.get_text()
                    alltext+=text
            self.df = pd.concat([self.df, pd.DataFrame({'source': ['bbcturk'], 'content': [alltext]})])

            
    def hurriyettextGenerate(self,links):
        for link in links:
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

                
    def donanimtextGenerate(self,links):
        for link in links:
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
    def ekonomimtextGenerate(self,links):
        for link in links:
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
                
     
    def gazeteoksijentextGenerator(self, links):
        for link in links:
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
    def bloomberghttextGenerator(self, links):
        for link in links:
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
    def kayiprihtimtextGenerator(self, links):
        for link in links:
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

    def getmidastextGenerator(self, links):
        for link in links:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            try:
                divisionText=soup.findChild('article',{'class':'blog-detail-content'})
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
            except:
                print("bu link çalışmadı")
            
    def haberturktextGenerator(self, links):
        for link in links:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            alltext=''
            try:
                divisionText=soup.findChildren('div',{'class':'wrapper'})
                for i in divisionText:
                    divisionText=i.find_all('p')

                    for i in divisionText:
                        text=i.get_text()
                        print(text)
                        alltext+=text
                        

                self.df = pd.concat([self.df, pd.DataFrame({'source': ['haberturk'], 'content': [alltext]})])
            except Exception as e:
                print(e, "bu link çalışmadı")
            
    def ntvtextGenerator(self, links):
        for link in links:
            response=requests.get(link, allow_redirects=True)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            alltext=''
            try:
                divisionText=soup.findChild('div',{'class':'content-news-tag-selector'})
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
                self.df = pd.concat([self.df, pd.DataFrame({'source': ['NTV'], 'content': [alltext]})])
            except Exception as e:
                print(e,"bu link calismadi" )
    def milliyettextGenerator(self, links):
        for link in links:
            response=requests.get(link, allow_redirects=True)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            alltext=''
            try:
                divisionText=soup.findChild('div',{'class':'news-content news-content readingTime'})
                divisionText=divisionText.find_all('p')
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
                self.df = pd.concat([self.df, pd.DataFrame({'source': ['Milliyet'], 'content': [alltext]})])
            except:
                print("bu link çalışmadı")
    def sabahtextGenerator(self,links):
        for link in links:
            response=requests.get(link)
            html=response.text
            alltext=""
            soup=BeautifulSoup(html,'html.parser')
            try:
                divisionText=soup.findChild('div',{'class':"newsDetailText"})
                for i in divisionText:
                    text=i.get_text()
                    alltext+=text
                self.df = pd.concat([self.df, pd.DataFrame({'source': ['SABAH'], 'content': [alltext]})])

            except:
                alltext="sonucyok"
            
    def write_list_to_csv(self,date):
        filename=f"{date}.csv"
        self.df.to_csv(filename, index=False)
        