import streamlit as st
import requests
from PIL import Image
from bs4 import BeautifulSoup 
from requests_html import HTMLSession
#janes logo
image = Image.open("C:\\Users\\vedant\\Desktop\\Programs\\GMV NEWS\\pages\\ms.png")
#beautiful soup code
l = []
s = HTMLSession()
s2 = HTMLSession()
url = 'http://www.indiandefensenews.in/'
def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_heading(soup):
    page = soup.find('h1', {'class' : 'post-title'})
    return page.text
soup = getdata(url)
heading = get_heading(soup)

def get_link(soup):
    page = soup.find('a', {'class' : 'color-transition'})
    return page['href']
get_link(soup)
url2 = get_link(soup)
url2 = url2[37:]

def getarticle(url):
    r = s.get(url2)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_content(soup):
    page = soup.find('div', {'class' : 'post-content'})
    c = page.find_all('div')
    for i in c:
        l.append(i.text)
    s = ' '.join(l)
    return s
soup2 = getarticle(url2)

content = get_content(soup2)
##
st.set_page_config("GMV NEWS LIVE-DF", "✈")
col1, col2 = st.columns(2)

with col1:
    st.image(image)
    st.header("LATEST DEFENSE NEWS")


st.subheader(heading)
st.markdown(content.replace('$', ''))
st.text("")
st.button("TEXT TO SPEECH",)
st.text("")


st.button("TRANSLATE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("SAVE ARTICLE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("DISPLAY KEYWORDS",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")