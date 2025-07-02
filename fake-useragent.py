'''
# store the IP as a string in a variable
proxy = '00.00.000.000:0000'
response = requests.get('https://books.toscrape.com/',
                         proxies={"http": proxy, "https": proxy})

This will route your request through the proxy IP, to the URL. In this case I’m just using a dummy IP. There are free proxies available online, just be aware that there is no guarantee that data going through them is private, as the proxy will have full access to the data that goes through it.


The above type of get-request is a headless request. Some servers will require the browser to have a head or user-agent, so that only users with a browser can view the content. This can be simulated in the Python environment with the fake_useragent library


from fake_useragent import UserAgent
# create a UserAgent type object
ua = UserAgent()
# call on the UserAgent object to create a random browser useragent
fake_chrome_browser = ua.chrome
# print the response
print(fake_chrome_browser)
 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36'


To implement the user-agent into our get-request, simply pass it as a parameter in the header. While we are at it, go ahead and store the base url just to clean up the inputs.

# store the user-agent in a dictionary to pass to the get-request
useragent_header = {'User-Agent': fake_chrome_browser}
url_base = 'https://books.toscrape.com/'
response = requests.get('url_base,
                         headers = useragent_header, 
                         proxies={"http": proxy, "https": proxy})

                         
Now it is possible to bypass that pesky IP timeout by using a proxy, and further convolution is possible by randomizing the user-agent each request by with UserAgent().random . Putting everything together:

# import libraries
import requests
from fake_useragent import UserAgent
# declare variables
url_base = 'https://books.toscrape.com/'
proxy = '00.00.000.000:0000'
ua = UserAgent()
fake_browser = ua.random
useragent_header = {'User-Agent': fake_browser}
response = requests.get('url_base,
                         headers = useragent_header, 
                         proxies={"http": proxy, "https": proxy})
print(response.content)



'''