import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Aqui constrói o necessário para lidar com https

ctx = ssl.create_default_context()  
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#X serve para limitar a um chamado por vez
x = True

while x:

    address = 'Kokshetau Institute of Economics and Management'
    #these parms are used to build the url 
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)

    #We use the handler to create a connection with the data and add ctx as context to deal with https
    handler = urllib.request.urlopen(url, context=ctx)
    hand = handler.read().decode()

    #Here we load the data into a variable
    try: 
        js = json.loads(hand)
    except:
        js = None

    #here we see if the data collected was correct. Verifying if there's a js variable and the status if ok
    if not js or 'status' not in js or js['status'] != 'OK':
        print('failure to retrieve the data')
        print(hand)
        continue

    #Here we print the result with 4 indent
    print(json.dumps(js, indent=4))

    #Here we are gathering the data to print place id
    id = js['results'][0]['place_id']
    print('id:', id, )

    x = False