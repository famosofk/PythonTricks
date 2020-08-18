import xml.etree.ElementTree as ET

data = '''

<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 3034456</phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print("Name: ", tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))


#Para achar algo lá, no sentido de tag de dentro de tag, como na estrutura abaixo

'''
<users>
<user>data</user>
<user>data2</user>
<user>data</user>
</users>
'''
#list = stuff.findall('users/user')
#then we can len(list) and to print the data from users, we can use
'''
for itens in list:
    print('Name', item.find('Name').text)
    print('Id', item.find('Id').text)
    print('Age', item.find('Age').text)