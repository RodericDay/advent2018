import json


def main(text, simple):

    def rsum(obj):
        if type(obj) == int:
            return obj

        elif type(obj) == list:
            return sum(rsum(e) for e in obj)

        elif type(obj) == dict:
            if not simple and 'red' in obj.values():
                return 0
            return sum(rsum(e) for e in obj.values())

        else:
            return 0

    print(rsum(json.loads(text)))
