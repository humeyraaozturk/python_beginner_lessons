import json5

person_string = '{"Name":"Ali","Languages":["python","C#"]}'
#result1 = json5.loads(person_string)
#loads ile sözlük nesneye dönüştürülür.
#print(type(result1))
#print(result1)

#with open("person.json") as f:
    #data = json5.load(f)
    #print(data["Name"])

person_dict = {"Name":"Ali","Languages":["python","C#"]}
result = json5.dumps(person_dict)
#python veri türü dumps ile json'a dönüştürülür.
print(result)
print(type(result))

