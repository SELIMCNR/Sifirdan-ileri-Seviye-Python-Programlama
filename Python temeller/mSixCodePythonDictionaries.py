# key - value
# 41 => Kocaeli 34 => Istanbul

sehirler = ["Kocaeli","Istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("Istanbul")])

plakalar = {'key': 41, 'key2': 34}	

print(plakalar['key'])
print(plakalar['key2'])

plakalar['key3'] = 6
print(plakalar)

plakalar['key2'] = 35
print(plakalar)

users = {
    'kadiraykut': {
        'age' : 36,
        'roles':['user'],
        'email': 'kadir@gmail.com',
        'address': 'Kocaeli',
        'phone': '123456789'
    },
    
    'kadir2':{
        'age' : 24,
        'roles':['user','admin'],
        'email': 'f@gmail.com',
        'address': 'Istanbul',
        'phone': '987654321'
    }

    
    }

print(users['kadiraykut']['age'])
print(users['kadiraykut']['roles'][0])
print(users['kadiraykut']['email'])
print(users['kadiraykut']['address'])
print(users['kadiraykut']['phone'])