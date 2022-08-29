import streamlit as st
import requests
from PIL import Image
from bs4 import BeautifulSoup 
from requests_html import HTMLSession
#janes logo
image = Image.open("C:\\Users\\vedant\\Desktop\\Programs\\GMV NEWS\\pages\\df.png")
#beautiful soup code
l = []
std_url = 'https://www.defensenews.com/'
link = ''
s = HTMLSession()
url = 'https://www.defensenews.com/global/'
def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_heading(soup):
    page = soup.find('a', {'class' : 'ArticleLink-sc-1f35nm6-0 jckchf o-articleCard__link'})
    return page.text
soup = getdata(url)
heading = get_heading(soup)


def get_link(soup):
    page = soup.find('a', {'class' : 'ArticleLink-sc-1f35nm6-0 jckchf o-articleCard__link'})
    return page['href']
get_link(soup)
url2 = std_url+get_link(soup)


def getarticle(url):
    r = s.get(url2)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_content(soup):
    page = soup.findAll('p', {'class' : 'Paragraph-sc-1tqpf5s-0 kEzXdV body-paragraph body-paragraph'})
    for i in page:
        l.append(i.text)
    s = ' '.join(l)
    return s
soup2 = getarticle(url2)

content = get_content(soup2)
##
st.set_page_config("GMV NEWS LIVE-LM", "✈")
col1, col2 = st.columns(2)

with col1:
    st.image(image)
    st.header("LOCKHEED MARTIN LATEST NEWS")


st.subheader(heading)
st.write(content.replace('$', ''))
st.text("")
st.button("TEXT TO SPEECH",)
st.text("")


st.button("TRANSLATE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("SAVE ARTICLE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("DISPLAY KEYWORDS",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")