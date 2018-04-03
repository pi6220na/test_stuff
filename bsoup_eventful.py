import requests
from bs4 import BeautifulSoup

def main():

    #getYelp()
    getMSPL()

def getYelp():

    result = requests.get("https://www.yelp.com/events/minneapolis/browse?c=1&start=0")
    print(result.status_code)

    # print headers
    print(result.headers)
    c = result.content

    # get web page and print the entire page
    soup = BeautifulSoup(c,"html.parser")
    #print(soup)

    #
    # #samples = soup.find_all("p", "title")
    # samples = soup.find_all("h3", "card_content-title card_content-title--linked")
    #

    samples2 = soup.find_all("div", "page-of-pages arrange_unit arrange_unit--fill")
    print()
    print('second print of samples')
    for item in samples2:
        print(item)
    print()
    print()
    myText = samples2[0].string.strip()
    print(myText)
    myNum = [int(s) for s in myText.split() if s.isdigit()]
    print(myNum)
    numPages = int(myNum[1])
    print(str(numPages))

    titlesList = []
    venueList = []
    locDateList = []
    descripList = []

    itemCount = 0

    for page in range(numPages):
        print(str(page))
        result = requests.get("https://www.yelp.com/events/minneapolis/browse?c=1&start=" + str(itemCount))
        print("https://www.yelp.com/events/minneapolis/browse?c=1&start=" + str(itemCount))
        c = result.content
        soup = BeautifulSoup(c, "html.parser")

        if result.status_code == 200:
            titles = soup.select('span[itemprop="name"]')
            titlesList.append(titles)

            venues = soup.find_all("a", 'biz-name js-analytics-click')
            venueList.append(venues)

            #locDate = soup.find_all("div", 'u-text-truncate u-space-b1')
            #soup.select('div[class^="TypeA"], div[class^="TypeB"]')

            # first_story_paragraph = soup.find("p", "story")
            # first_story_paragraph.find_next_sibling("p")


            locDate = soup.select('div[class^="card_body"] div[class^="card_content"] div[class^="u-text-truncate"]')
            locDateList.append(locDate)

            descrips = soup.find_all("p", 'card_content-text')
            descripList.append(descrips)

            itemCount += 15
        else:
            exit(-1)


    print()
    # print()
    # print(titlesList)
    # for item in titlesList:
    #     for innerItem in item:
    #         print(innerItem.get_text())
    # print()
    # print(venueList)
    # for item in venueList:
    #     for innerItem in item:
    #         print(innerItem.get_text())
    # print()
    # print(locDateList)
    # for item in locDateList:
    #     for innerItem in item:
    #         print((innerItem.get_text()).strip())
    # print()
    # print(descripList)
    # for item in descripList:
    #     for innerItem in item:
    #         print(innerItem.get_text().strip())
    # print()



    ###### clean up raw selected html, generate cleaned lists

    cleanTitlesList = []
    for item in titlesList:
        for innerItem in item:
            cleanTitlesList.append(innerItem.get_text())

    print("titles")
    for item in cleanTitlesList:
        print(item)

    print()

    cleanVenueList = []
    for item in venueList:
        for innerItem in item:
            cleanVenueList.append(innerItem.get_text())

    print("venues")
    for item in cleanVenueList:
        print(item)

    print()

    cleanLocDateList = []
    for item in locDateList:
        for innerItem in item:
            #print("innerItem " + str(innerItem))
            #print("innerItem striped " + innerItem.get_text().strip())
            print((innerItem.get_text()).strip())
            cleanLocDateList.append((innerItem.get_text()).strip())

    print("locdates")
    print(cleanLocDateList)
    for item in cleanLocDateList:
        print(item)
        print()

    cleanLocList = []
    cleanDateList = []
    for num in range(0,len(cleanLocDateList),2):
        print(num)
        cleanDateList.append(cleanLocDateList[num])
        cleanLocList.append(cleanLocDateList[num+1])

    print()
    print(cleanDateList)
    print(cleanLocList)

    print()

    cleanDescripList = []
    for item in descripList:
        for innerItem in item:
            cleanDescripList.append(innerItem.get_text().strip())

    print("descriptions")
    for item in cleanDescripList:
        print(item)

    zipAll = list(zip(cleanTitlesList, cleanVenueList, cleanLocList, cleanDateList, cleanDescripList))

    print("about to print zipped lists")

    print(zipAll)

    for tuple_num in range(len(zipAll)):
        print("Event Number: %d" % tuple_num)
        print('1: ' + zipAll[tuple_num][0])
        #print('2: ' + zipAll[tuple_num][1])
        print('2: ' + zipAll[tuple_num][2])
        print('3: ' + zipAll[tuple_num][3])
        print('4: ' + zipAll[tuple_num][4])
        print()



def getMSPL():

    result = requests.get("http://minneapolis.eventful.com/events/categories/music")
    print(result.status_code)

    print(result.headers)
    c = result.content

    soup = BeautifulSoup(c, "html.parser")
    print(soup)

    # samples = soup.find_all("p", "title")
    samples = soup.find_all("h4")

    print()
    print("First Print:")
    for item in samples:
        print(item)
    print()
    print()

    # for item in soup.find_all(attrs={'class': 'article-additional-info'}):
    #     ...:
    #     for link in item.find_all('a'):
    #         ...: print
    #         link.get('href')
    soup = BeautifulSoup(c, "html.parser")
    # samples2 = soup.find_all(itemprop="name")
    samples2 = soup.find_all("a", 'tn-frame')
    print()
    print('second print of samples')
    for item in samples2:
        myURL = item.get('href')
        #print(myURL)
        myURL = "http:" + myURL
        result = requests.get(myURL)
        #print(result.status_code)
        #print(result.headers)
        c = result.content
        minisoup = BeautifulSoup(c, "html.parser")
        # print('*********************************************************************')
        # print(minisoup)
        #
        # samples3 = minisoup.find('title')
        # print('#####################################################################')
        # myText = samples3.string.strip()
        # print(myText)
        # print('#####################################################################')
        #
        # print('*********************************************************************')
        # print('*********************************************************************')
        #print(minisoup)

        # samples3 = minisoup.select('meta[name^="description"]')                      # this works
        samples3 = minisoup.find("meta", {"name":"description"})['content']
        #print('#####################################################################')
        #myText = samples3.string.strip()
        print(samples3)
        # for item in samples3:
        #     print(item)
        #print('#####################################################################')

        #print('*********************************************************************')

    print()
    print()



main()

# https://stackoverflow.com/questions/11205386/python-beautifulsoup-get-an-attribute-value-based-on-the-name-attribute/11205758
# >>> soup = BeautifulSoup('<META NAME="City" content="Austin">')
# >>> soup.find("meta", {"name":"City"})
# <meta name="City" content="Austin" />
# >>> soup.find("meta", {"name":"City"})['content']
# u'Austin'