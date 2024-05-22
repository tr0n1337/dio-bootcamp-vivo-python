# CLEAR
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "8002-8922"},
  "souza@gmail.com": {"name": "Souza", "telephone": "5642-4000"},
  "fernandes@gmail.com": {"name": "Fernandes", "telephone": "1234-5678"},
}

contacts_clear = contacts.clear()
print(f"CONTACTS CLEAR: {contacts_clear}")

# COPY
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "1234-5678"}
}

copy = contacts.copy()
print(f"COPY: {copy}")

copy["thiago@gmail.com"] = {"name": "Thiago"}
print(f"COPY: {copy}")

print(f"CONTACTS: {contacts['thiago@gmail.com']}")

print(f"COPY: {copy['thiago@gmail.com']}")

# FROMKEYS
from_keys_a = dict.fromkeys(["name", "telephone"])
from_keys_b = dict.fromkeys(["name", "telephone"], "vazio")
print(f"FROMKEYS A: {from_keys_a}")
print(f"FROMKEYS B: {from_keys_b}")

# GET
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "1234-5678"}
}

# print(f"CONTACTS: {[contacts['chave']]}") error

get_a = contacts.get("chave")
get_b = contacts.get("chave", {})
get_c = contacts.get("thiago@gmail.com", {})
print(f"GET A: {get_a}")
print(f"GET B: {get_b}")
print(f"GET C: {get_c}")

# ITEMS
contacts = {
  "thiago@gmail.com": {
    "name": "Thiago",
    "telephone": "1234-1234"
  }
}

items = contacts.items()
print(f"CONTACT ITEMS: {items}")

# KEYS
contacts = {
  "thiago@gmail.com": {
    "name": "Thiago",
    "telephone": "1234-1234"
  }
}

print(f"CONTACT KEYS: {contacts.keys()}")

# POP
contacts_a = {
  "thiago@gmail.com": {
    "name": "Thiago",
    "telephone": "1234-1234"
  }
}


contacts_pop_a = contacts_a.pop("thiago@gmail.com")
contacts_pop_b = contacts_a.pop("thiago@gmail.com", {})
print(f"CONTACTS POP: {contacts_pop_a}")
print(f"CONTACTS POP: {contacts_pop_b}")

# POPITEM
contacts_a = {
  "thiago@gmail.com": {
    "name": "Thiago",
    "telephone": "1234-1234"
  }
}


contacts_pop_item_a = contacts_a.popitem()
print(f"CONTACTS POPITEM: {contacts_pop_item_a}")

# SETDEFAULT
contacts = {
    "name": "Thiago",
    "age": 21
}

contacts_set_default_a = contacts.setdefault("name", "Fernandes")
print(f"CONTACTS SETDEFAULT A: {contacts_set_default_a}")

contacts_set_default_b = contacts.setdefault("age", 18)
print(f"CONTACTS SETDEFAULT B: {contacts_set_default_b}")

# UPDATE
contacts = {
  "thiago@gmail.com": {
    "name": "Thiago",
    "telephone": "1234-1234"
  }
}


contacts.update(
  {"thiago@gmail.com": {"name": "Fernandes"}})
print(f"CONTACTS UPDATE A: {contacts}")

contacts.update({
  "thiago@gmail.com": {
    "name": "Souza",
    "telephone": "9999-9999"
    }
  })
print(f"CONTACTS UPDATE B: {contacts}")


# VALUES
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "8002-8922"},
  "souza@gmail.com": {"name": "Souza", "telephone": "5642-4000"},
  "fernandes@gmail.com": {"name": "Fernandes", "telephone": "1234-5678"},
}
values = contacts.values()
print(f"VALUES: {values}")

# IN
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "8002-8922"},
  "souza@gmail.com": {"name": "Souza", "telephone": "5642-4000"},
  "fernandes@gmail.com": {"name": "Fernandes", "telephone": "1234-5678"},
}

contact_in_a = "thiago@gmail.com" in contacts
contact_in_b = "a@gmail.com" in contacts
contact_in_c = "idade" in contacts["thiago@gmail.com"]
contact_in_d = "telephone" in contacts["thiago@gmail.com"]
print(f"CONTACT IN A: {contact_in_a}")
print(f"CONTACT IN B: {contact_in_b}")
print(f"CONTACT IN C: {contact_in_c}")
print(f"CONTACT IN D: {contact_in_d}")

# DEL
contacts = {
  "thiago@gmail.com": {"name": "Thiago", "telephone": "8002-8922"},
  "souza@gmail.com": {"name": "Souza", "telephone": "5642-4000"},
  "fernandes@gmail.com": {"name": "Fernandes", "telephone": "1234-5678"},
}
del contacts["thiago@gmail.com"]["telephone"]
print(f"CONTACTS DEL A: {contacts}")

del contacts["souza@gmail.com"]
print(f"CONTACTS DEL B: {contacts}")
