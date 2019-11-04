
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]


# SentimentAnalyzer 

* This Library is Developed using WebScrapping Techiques.It Takes a String as input and output is JSON Data
* This is developed using BS4 and requests and re Modules 

## Installation

```bash
pip install SentimentAnalyzer
```
## Usage

```python
import sys
from SentimentAnalyzer.SentimentAnalyzer import Sentiment
text = """  
    Hello this is a  sample  text
    place your text here  and it should be less than 50 000 Words 
    
    """

obj = Sentiment(text=text)
data = obj.get
print(data)

```


----------------
![Screen Shot 2019-11-04 at 1 42 17 PM](https://user-images.githubusercontent.com/39345855/68147852-f2cf3d80-ff08-11e9-8fe3-d443a73e2cc3.png)




## Authors

* **Soumil Nitin Shah** 




## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


