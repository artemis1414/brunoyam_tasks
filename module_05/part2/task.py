import json

class Model:

    title = '1'
    text = 'Конец Вечности'
    author = 'Айзек Азимов'

    def save(self):
        attributes = list(filter(lambda x: not x.startswith('_') and x != 'save', dir(self)))
        dictionary = {}
        for attr in attributes:
            dictionary[attr] = getattr(self, attr)
        with open('db.json', mode='w') as f:
            f.write(json.dumps(dictionary))


dat = Model()
dat.save()
