

class car(object):
    def __init__(self, company, details):
        self.company = company
        self.details = details
    def __str__(self): # 프린트문으로 문자열을 출력하는 사용자 입장에선 __str__을 하고
        return f'str : {self.company} - {self.details}'
    def __repr__(self): # 예는 개발자 레벨에서 객체값을 엄격하게 규정하여 반환할 때에 사용한다.
        return f'repr : {self.company} - {self.details}'