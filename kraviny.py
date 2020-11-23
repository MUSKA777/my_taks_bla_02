import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])


# { kraviny [{ body }]}

myList = [
    {
        'foo': 12,
        'bar': 14,
    },
    {
        'moo': 52,
        'car': 641,
    },
    {
        'doo': 6,
        'tar': 84,
    }
]



print(myList[0])
print(myList[0]['bar'])

data = {
    'name': 'linux',
    'first_name': 'mana',
    'data': [
        {
            'kraj': 'r452',
            'okres': 'j456',
            'pocet': 58,
            'dalsi': 485,
        }
    ]
}
hodnoty = data.pop('data')
print(hodnoty)

"""
ku_hodnota = KU[0]
kz_hodnota = KZ[0]
kn_hodnota = KN[0]
a_hodnota = A[0]

print('ku', ku_hodnota.keys())
print('kz', kz_hodnota.keys())
print('kn', kn_hodnota.keys())
print('a', a_hodnota.keys())"""