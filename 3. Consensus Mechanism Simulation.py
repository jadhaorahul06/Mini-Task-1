import random

validators = {
    "PoW": [{"id": 1, "power": random.randint(1, 100)} for _ in range(3)],
    "PoS": [{"id": 1, "stake": random.randint(1, 100)} for _ in range(3)],
    "DPoS": [{"id": i, "votes": random.randint(1, 5)} for i in range(1, 4)]
}

def select_validator(method):
    if method == "PoW":
        return max(validators["PoW"], key=lambda x: x["power"])
    elif method == "PoS":
        return max(validators["PoS"], key=lambda x: x["stake"])
    else:  # DPoS
        return max(validators["DPoS"], key=lambda x: x["votes"])

print("PoW Selected:", select_validator("PoW"))
print("PoS Selected:", select_validator("PoS"))
print("DPoS Selected:", select_validator("DPoS"))