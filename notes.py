# Here’s an HTML document I’ll be using as an example throughout this document.
# It’s part of a story from Alice in Wonderland:
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Running the “three sisters” document through Beautiful Soup gives us a BeautifulSoup object,
# which represents the document as a nested data structure:

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')


# Here are some simple ways to navigate that data structure:
def prints():
    print(soup.title)  # <title>The Dormouse's story</title>
    print(soup.title.name)  # title
    print(soup.title.string)  # The Dormouse's story
    print(soup.head.parent.name)  # html
    print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    print(soup.p['class'])  # ['title']
    print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    print(soup.find_all('a'))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister"
    # href="http://example.com/tillie" id="link3">Tillie</a>]
    print(soup.find(id="link3"))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


def links():
    # One common task is extracting all the URLs found within a page’s <a> tags:
    for link in soup.find_all("a"):
        print(link.get("href"))

        # http://example.com/elsie
        # http://example.com/lacie
        # http://example.com/tillie


# Another common task is extracting all the text from a page:
print(soup.get_text())

# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...
