from typing import Dict

class Repository:

    def select(self, name: str) -> Dict:
        return {"name": name, "age": 32}

    def insert(self, name: str, age: int) -> Dict:
        print('Inserting data {}, {} in table...' .format(name, age))
        return {"name": name, "age": age}