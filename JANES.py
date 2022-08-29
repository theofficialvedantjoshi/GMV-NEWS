import streamlit as st
import requests
from PIL import Image
from bs4 import BeautifulSoup 
from requests_html import HTMLSession
#janes logo
image = Image.open("C:\\Users\\vedant\\Desktop\\Programs\\GMV NEWS\\pages\\janes.png")
#beautiful soup code
l = []
link = ''
s = HTMLSession()
url = 'https://www.janes.com/defence-news/'
def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_heading(soup):
    page = soup.find('div', {'class' : 'list-content'})
    c = page.find('h2')
    return c.text
soup = getdata(url)
heading = get_heading(soup)

def get_link(soup):
    page = soup.find('section', {'id' : 'Contentplaceholder1_C030_Col00'})
    c = page.find('a')
    return c['href']
get_link(soup)
url2 = get_link(soup)


def getarticle(url):
    r = s.get(url2)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_content(soup):
    page = soup.find('div', {'class' : 'read-more-p'})
    c = page.find_all('p')
    for i in c:
        l.append(i.text)
    s = ' '.join(l)
    return s
soup2 = getarticle(url2)

content = get_content(soup2)
##
st.set_page_config("GMV NEWS LIVE-JANES", "✈")
col1, col2 = st.columns(2)

with col1:
    st.image(image)
    st.header("JANES LATEST NEWS")


st.subheader(heading)
raw_s = r'{}'.format(content)
st.markdown(raw_s)
st.text("")
st.button("TEXT TO SPEECH",)
st.text("")


st.button("TRANSLATE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("SAVE ARTICLE",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("DISPLAY KEYWORDS",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")