class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Микола"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Микола")
        
        if not hobby.strip():  
            raise ValueError("Хоббі не може бути порожнім")
        
        self.name = name
        self.hobby = hobby

person = Name("Микола", "")
