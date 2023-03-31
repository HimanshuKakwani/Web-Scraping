from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    
    # header_tags = soup.find_all('h1')
    # print("The headers are:" , header_tags)

    # info_tags = soup.find_all('h2')
    # for tags in info_tags:
    #     print("The info headers are: ", tags)

    containers_class = soup.find_all('div', class_ = 'containers')
    for cont in containers_class:
        print(cont.h2.text)