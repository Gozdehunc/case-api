from flask import Flask
from selenium import webdriver
from bs4 import BeautifulSoup


app=Flask(__name__)

#options = webdriver.ChromeOptions()
#options.add_argument('headless') #dont open page with run selenium
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

@app.route("/", methods=["GET"])
def api_time():
    """
    parametre almayan, JSON donduren bir API örneği.
    
    """
    name_surname ={"firstname": "GOZDE", "lastname": "HUNC"}
    
    return name_surname

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('headless') #dont open page with run selenium
    #options.add_argument('--no-sandbox')
    #options.add_argument("--disable-setuid-sandbox")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver




@app.route("/temperature/city=<string:city>")
def api_price(city):
    """
    Bu fonksiyonun özelliği dışardan alabilir vaziyette. Değerleri URL
    üzerinden alıyor.
    """
    query=city
    def build_url(query):
        """
        https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=D%C3%BCzce
        
        """
        return f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={query}"

    def get_data_from_url(url):
        driver =get_driver()
        response=driver.get(url)
        html =driver.page_source
        #text=response.text
        return html
    

    url=build_url(query)
    text=get_data_from_url(url)
    soup=BeautifulSoup(text,'html.parser')
    #time.sleep(1)
    """
    <div class="anlik-sicaklik-deger ng-binding" ng-bind="sondurum[0].sicaklik | comma">-0,3</div>
    """
    anlikDerece=soup.find("div",{"class":"anlik-sicaklik-deger ng-binding"})
    
    dcity = {"temperature": anlikDerece.text}
    return dcity




if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')