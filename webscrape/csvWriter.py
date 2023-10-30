from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import requests
class csvWriter:
    def __init__(self, bundlelinks=None,bbclinks=None,hurriyetlinks=None,donanimlinks=None,ekonomimlinks=None,gazeteoksijenlinks=None):
        self.bundlelinks = bundlelinks
        self.bbclinks = bbclinks
        self.hurriyetlinks = hurriyetlinks
        self.donanimlinks = donanimlinks
        self.ekonomimlinks = ekonomimlinks
        self.gazeteoksijenlinks = gazeteoksijenlinks
        
        self.sourcelist = []
    def bundletextGenerate(self):
        for link in self.bundlelinks:

            try:
                response = requests.get(link)
                response.raise_for_status()  # Yanıt durumu 4xx veya 5xx ise istisna fırlatılır.
    
            # İşlem başarılı olduysa burada istediğiniz işlemleri gerçekleştirebilirsiniz.
    
            except requests.exceptions.RequestException as e:
            # Talep sırasında bir hata oluştuğunda bu blok çalışır.
                print("Hata oluştu:", e)
                print(link)
            html = response.text
            soup = BeautifulSoup(html , 'html.parser')
            #icergi al
            divisonText = soup.findChild('div', {'class': 'bundleXPathBody'})
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
                

            self.sourcelist.append(sonuc)
        print(set(self.sourcelist))  
    def bbctextGenerate(self):
        for link in self.bbclinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            divisionText=soup.findChildren('div',{'class':"bbc-19j92fr ebmt73l0"})
            alltext=""
            for text in divisionText:
                ptext=text.findChildren('p',{'class':'bbc-hhl7in e17g058b0'})
                for p in ptext:
                    text=p.get_text()
                    alltext+=text
           
            
    def hurriyettextGenerate(self):
        for link in self.hurriyetlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
                #divisionText
                #sourceText
            
    def donanimtextGenerate(self):
        for link in self.donanimlinks: 
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            # divisionText
            # sourceText
            
    def ekonomimtextGenerate(self):
        for link in self.ekonomimlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
                #divisionText
                #sourceText
     
    def gazeteoksijentextGenerator(self):
        for link in self.gazeteoksijenlinks:
            response=requests.get(link)
            html=response.text
            soup=BeautifulSoup(html,'html.parser')
            #divisionText
            # sourceText
            
            
    #def write_list_to_csv(self, data):
        