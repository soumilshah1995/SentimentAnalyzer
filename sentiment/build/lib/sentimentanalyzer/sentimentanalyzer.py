__Author__ = "Soumil nitin Shah"
__Email__ = "shahsoumil519@gmail.com"
__Version__ = "0.0.1"


try:
    import requests
    from bs4 import BeautifulSoup
    import  os
    import re
    import json

except Exception as e:
    print("Some modules are missing {}".format(e))


class MetaClass(type):

    """ Singleton Design Pattern  """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ if instance already exist dont create one  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Stack(object):

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):

        if self.data == []:
            return None

        else:
            return self.data.pop()

    def isEmpty(self):
        return self.data == []

    def getSize(self):
        return  self.data



class WebCrawler(object):

    def __init__(self, text=''):

        """Constructor   """

        self._header=  {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',}

        self._url = "https://text-processing.com/demo/sentiment/"
        self.text = text

        self._params= {
            'language':'english',
            'text':self.text}

        self.stack = Stack()

    def __getData(self):
        """
        PRIVATE FUNCTION

        Just Makes Raw Request and Return RAW HTML DATA
        :return: RAW HTML
        """

        r = requests.post(url=self._url,
                          headers=self._header,
                          data=self._params)
        return r

    def ProcessData(self):

        r = self.__getData()

        data = r.text

        polar= re.compile(r'polar: (\d\.\d)+')
        neutral = re.compile(r'neutral: (\d\.\d)')
        positive = re.compile(r'pos: (\d\.\d)')
        negative = re.compile(r'neg: (\d\.\d)')

        Vpolar = []
        Vneutral = []
        Vpositive = []
        Vnegative = []
        Vtext= []

        # Polar
        matchesPolar = polar.finditer(data)
        for polar_value in matchesPolar:
            d = polar_value.group(1)
            Vpolar.append(d)

        # Neutral
        matchesNeutral = neutral.finditer(data)
        for match_neutral in matchesNeutral:
            d = match_neutral.group(1)
            Vneutral.append(d)


        # Positive
        matchesPositive = positive.finditer(data)
        for match_positive in matchesPositive:
            d = match_positive.group(1)
            Vpositive.append(d)


        # Negative
        matchesNegative = negative.finditer(data)
        for match_negative in matchesNegative:
            d = match_negative.group(1)
            Vnegative.append(d)


        soup = BeautifulSoup(r.text, 'html.parser')
        for x in soup.findAll(class_='success'):
            data =x.text
            Vtext.append(data)


        return Vpolar,Vnegative, Vpositive, Vneutral, Vtext

    def createPayload(self):
        """

        Return  a json payload
        :return:
        """
        Payload = {}
        Vpolar,Vnegative, Vpositive, Vneutral, Vtext = self.ProcessData()

        Payload["Polar"] = Vpolar
        Payload["Negative"] = Vnegative
        Payload["Positive"] = Vpositive
        Payload["Neutral"] = Vneutral
        Payload["Text"] = Vtext

        self.stack.push(Payload)

        return self.stack


class Sentiment(object):

    def __init__(self,text=''):
        self.text = text
        self.webcrawler = WebCrawler(text=self.text)

    @property
    def get(self):

        """ Return the JSON DATA """

        return self.webcrawler.createPayload().pop()

#
# if __name__ == "__main__":
#
#     text = """
#     Hello this is a  sample  text
#     place your text here  and it should be less than 50 000 Words
#
#     """
#
#     obj = Sentiment(text=text)
#     data = obj.get
#     print(data)















