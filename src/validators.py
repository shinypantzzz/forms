from abc import ABC, abstractmethod
from typing import Iterable
from datetime import date
import re

class Validator(ABC):
    def __init__(self, type_name: str):
        self.type_name = type_name

    def get_type(self) -> str:
        return self.type_name

    @abstractmethod
    def validate(self, value: str) -> bool:
        pass

class ValidatorSequence:
    def __init__(self, validators: Iterable[Validator], default: str):
        self.validators = list(validators)
        self.default = default

    def get_type(self, value: str):
        for validator in self.validators:
            if validator.validate(value):
                return validator.get_type()
        return self.default

class DateValidator(Validator):
    def validate(self, value: str) -> bool:
        if re.fullmatch(r'[0-3][0-9]\.[0-1][0-9]\.[0-9]{4}', value):
            day, month, year = map(int, value.split('.'))
        elif re.fullmatch(r'[0-9]{4}-[0-1][0-9]-[0-3][0-9]', value):
            year, month, day = map(int, value.split('-'))
        else:
            return False
        
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False
        
class PhoneValidator(Validator):
    def validate(self, value: str) -> bool:
        return bool(re.fullmatch(r'\+7 \d{3} \d{3} \d{2} \d{2}', value))

class EmailValidator(Validator):
    def validate(self, value: str) -> bool:
        return (at_idx := value.find("@")) != -1 and value.find(".", at_idx+2) not in (-1, len(value)-1)