# from bs4 import BeautifulSoup
# portalTest = open("portaltest.txt", "w", encoding="utf-8")
# f = open("portal.html", "r", encoding="utf-8")
# portal = f.read()
# soup = BeautifulSoup(portal, 'html.parser')
# for string in soup.stripped_strings:
#     portalTest.write(string  + '\n')
# portalTest.close()

portalTest = open("portaltest.txt", "r", encoding="utf-8")
line = '1'
while line != '':
    line = portalTest.readline()
    line = line[:-1]
    if line.isdigit() and len(line) > 3:
        print(line)
