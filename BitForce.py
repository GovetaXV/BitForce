import bitcoin as bit
import requests


def create_addr():
  priv = bit.random_key()
  pub = bit.privtopub(priv)
  addr = bit.pubtoaddr(pub)
  return [addr, priv]
while 1:
    n = int(input('How Many Addresses? '))
    for i in range(0, n):
      data = create_addr()
      
      urlb = 'https://blockchain.info/address/' + data[0] + '?format=json'
      

      r = requests.get(urlb)
      json = r.json()
      
      if json['final_balance'] > 0:
        print('YOU ARE RICH, YOU GOT', json[5], 'Pub, Pri: ', data)
        break
      else:
        print('Failed: ', i, end='\r')
