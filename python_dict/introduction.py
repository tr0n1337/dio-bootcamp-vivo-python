people = {"name": "Thiago", "age": 21}
print(f"People: {people}")

people = dict(name="Thiago", age=21)
print(f"People: {people}")

people["tel"] = "4002-8922"
print(f"People: {people}")

data = {"name": "Thiago", "age": 21, "tel": "4002-8922"}
print(f"Data: {data}")

d_name = data['name']
print(f"Data Name: {d_name}")

d_age = data['age']
print(f"Data Age: {d_age}")

d_tel = data['tel']
print(f"Data Name: {d_tel}")

data["name"] = "Fernandes"
print(f"Data: {data}")

data["age"] = 18
print(f"Data: {data}")

data["tel"] = "123-456"
print(f"Data: {data}")

contacts = {
  "thiago@gmail.com": {"name": "Thiago", "tel": "8002-8922"},
  "souza@gmail.com": {"name": "Souza", "tel": "5642-4000"},
  "fernandes@gmail.com": {"name": "Fernandes", "tel": "1234-5678"},
}

tel_th = contacts["thiago@gmail.com"]["tel"]
print(f"Tel th: {tel_th}")

for key in contacts:
    print(f"key => {key}: value => {contacts[key]}")
