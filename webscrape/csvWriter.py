from bs4 import BeautifulSoup
import re
import requests
class csvWriter:
    def __init__(self, linklist):
        self.linklist = linklist
        self.sourcelist = []
    def bundletextGenerate(self):
        for link in self.linklist:
            response = requests.get(link)

            html = response.text
            soup = BeautifulSoup(html , 'html.parser')
            #icergi al
            divisonText = soup.findChild('div', {'class': 'bundleXPathBody'})
            #kaynag� al
            sourceText = soup.findChild('p', {'class': 'detailNewsReadText'})
            
            try:
                source = sourceText.find('a')
                source = source['href']
                sonuc = re.search(r'(www|tr)\.(.*?)\.com', source).group(2)
                
            except AttributeError:
                print("Eslesme bulunamadi.")
                

            self.sourcelist.append(sonuc)
        print(set(self.sourcelist))     
    #def write_list_to_csv(self, data):
        