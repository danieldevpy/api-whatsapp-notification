
class NumberController:

    @classmethod
    def check(cls, number: str):
        if len(number) != 11:
            raise Exception("O numero deve ter 11 caracters")
        
        new_number = f'+55 {number[:2]} {number[2:7]}-{number[7:]}'
        return new_number