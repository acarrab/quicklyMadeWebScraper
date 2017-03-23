import requests, re, pexpect
defaultHeaders = { 'Host' : 'danrudin.net', \
                   'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' }

#follow link
def follow(href, directory):
    pexpect.run('mkdir ' + directory)
    headers = {}
    for key, val in defaultHeaders.items(): headers[key] = val
    headers['Referer'] = href
    #get the current webpage
    r = requests.get(href)
    k = re.findall(r'href="(http://[\w\./=\-?&;]+.pdf)', r.text)
    for f in k:
        r = requests.get(f, headers=headers)
        if (r.status_code == 200):
            open(directory + '/' + re.findall(r'file=(.*\.pdf)', f)[0], 'wb').write(r.content)
        else:
            print(f + ' was not found....')



def start():
    link = 'http://schematic.danrudin.com/index.php?dir='
    r = requests.get(link)
    directories = re.findall(r'/index.php\?dir=(\w+/)', r.text)
    for d in directories:
        follow(link + d, d)

start()
