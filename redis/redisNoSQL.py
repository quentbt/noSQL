import redis
import json

# Connexion à Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def create(key, value):
    """Crée une entrée dans Redis."""
    r.set(key, json.dumps(value))
    return f"Donnée ajoutée avec la clé: {key}"

def read(key):
    """Lit une entrée depuis Redis."""
    data = r.get(key)
    return json.loads(data) if data else None

def update(key, new_value):
    """Met à jour une entrée existante."""
    if r.exists(key):
        r.set(key, json.dumps(new_value))
        return f"Donnée mise à jour pour la clé: {key}"
    return "Clé inexistante."

def delete(key):
    """Supprime une entrée."""
    if r.delete(key):
        return f"Donnée supprimée pour la clé: {key}"
    return "Clé inexistante."

# Exemple d'utilisation
data = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(create("user:1", data))
print(read("user:1"))
print(update("user:1", {"nom": "Alice", "age": 26, "ville": "Lyon"}))
print(read("user:1"))
print(delete("user:1"))
print(read("user:1"))
