class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(person_dicts: list) -> list:
    persons = [Person(d["name"], d["age"]) for d in person_dicts]
    for d in person_dicts:
        person = Person.people[d["name"]]
        if "wife" in d and d["wife"]:
            person.wife = Person.people.get(d["wife"])
        elif "husband" in d and d["husband"]:
            person.husband = Person.people.get(d["husband"])
    print(Person.people)
    return persons
