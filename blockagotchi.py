from datetime import datetime, timedelta
import logging
from typing import Dict, Optional, List
from shop import Item
from model_type import score  # Importa a função `score` gerada pelo m2cgen

logger = logging.getLogger(__name__)

def get_current_time() -> datetime:
    return datetime.utcnow()

def datetime_to_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def str_to_datetime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")

class BlockaGotchi:
    def __init__(self, owner: str, name: str, birth_time: datetime, id: int):
        self.id = id
        self.owner = owner
        self.name = name
        self.birth_time = birth_time
        self.age = self.get_age()
        self.stage = "Blob"
        self.type = None
        self.biotype = "Normal"
        self.condition = "Normal"
        self.happiness = 50
        self.last_fed_time = get_current_time()
        self.last_walk_time = get_current_time()
        self.last_bath_time = get_current_time()
        self.alive = True
        self.food_history: List[str] = []
        self.items: List[Item] = []
        self.walk_dates: List[datetime] = []
        self.overall_score = self.calculate_overall_score()

    def get_age(self) -> int:
        return (get_current_time() - self.birth_time).days

    def update_age(self) -> None:
        self.age = self.get_age()
        self.update_overall_score()

    def update_happiness(self, change: int) -> None:
        self.happiness += change
        self.update_overall_score()

    def calculate_overall_score(self) -> int:
        return self.age + self.happiness

    def update_overall_score(self) -> None:
        self.overall_score = self.calculate_overall_score()

    def feed(self, food_type: str) -> None:
        self.last_fed_time = get_current_time()
        self.food_history.append(food_type)
        self.update_happiness(10)
        self.evolve()
        logger.info(f"{self.name} was fed with {food_type}.")
        self.update_biotype()
    
    def walk(self, walk_type: str) -> None:
        current_time = get_current_time()
        self.last_walk_time = current_time
        self.walk_dates.append(current_time)
        self.update_happiness(5)
        self.evolve()
        logger.info(f"{self.name} went for a {walk_type} walk.")
        self.update_condition()

    def bathe(self, bath_type: str, is_paid: bool) -> None:
        self.last_bath_time = get_current_time()
        if is_paid:
            # TODO: Transfer tokens to DAO
            self.update_happiness(20)
        else:
            self.update_happiness(8)
        self.evolve()
        logger.info(f"{self.name} had a {bath_type} bath. Paid: {is_paid}")

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        logger.info(f"{self.name} received item {item.name}.")

    def remove_item(self, item: Item) -> None:
        self.items.remove(item)
        logger.info(f"{self.name} lost item {item.name}.")

    def list_items(self) -> List[Dict[str, any]]:
        return [item.to_dict() for item in self.items]

    def evolve(self) -> None:
        self.update_age()
        prev_stage = self.stage
        stages = {'Blob': 0, 'Child': 1, 'Teen': 2, 'Adult': 3, 'Old': 4}

        # Atualizar o estágio de acordo com a idade
        if self.stage == 'Blob' and self.age >= 7:
            self.stage = 'Child'
        elif self.stage == 'Child' and self.age >= 14:
            self.stage = 'Teen'
        elif self.stage == 'Teen' and self.age >= 21:
            self.stage = 'Adult'
        elif self.stage == 'Adult' and self.age >= 28:
            self.stage = 'Old'

        # Se houve mudança de estágio, prever o próximo tipo
        if self.stage != prev_stage:
            features = [
                self.age,
                self.food_history.count("Fish"),
                self.food_history.count("Meat"),
                self.food_history.count("Vegetal"),
                self.food_history.count("Fruta"),
                len([date for date in self.walk_dates if date >= get_current_time() - timedelta(days=30)]),
                1 if self.condition == "Muscle" else 2 if self.condition == "Normal" else 3,
                self.happiness,
                stages[prev_stage]
            ]

            types = {
                'Blob': ['Cat', 'Dog', 'Bird'],
                'Child': ['Cat', 'Dog', 'Bird'],
                'Teen': {
                    'Cat': ['Lion', 'Tiger'],
                    'Dog': ['Wolf'],
                    'Bird': ['Eagle', 'Duck', 'Pigeon']
                }
            }

            if prev_stage in ['Blob', 'Child']:
                next_type_code = score(features).index(max(score(features)))
                self.type = list(types[prev_stage])[next_type_code]
            elif prev_stage == 'Teen':
                if self.type in types['Teen']:
                    next_type_code = score(features).index(max(score(features)))
                    self.type = list(types['Teen'][self.type])[next_type_code]
                else:
                    self.type = None

            logger.info(f"{self.name} has evolved to {self.stage} stage and {self.type} type.")

    def update_biotype(self) -> None:
        feeding_frequency = len(self.food_history) / (self.get_age() + 1)
        if feeding_frequency > 2:
            self.biotype = "Fat"
        elif feeding_frequency < 1:
            self.biotype = "Skinny"
        else:
            self.biotype = "Normal"

    def update_condition(self) -> None:
        # Filter walk dates for the last 30 days
        thirty_days_ago = get_current_time() - timedelta(days=30)
        recent_walks = [date for date in self.walk_dates if date >= thirty_days_ago]

        walking_frequency = (get_current_time() - self.last_walk_time).days
        if walking_frequency <= 1 and len(recent_walks) >= 20:
            self.condition = "Muscle"
        elif walking_frequency <= 3 and len(recent_walks) >= 10:
            self.condition = "Normal"
        else:
            self.condition = "Sedentary"

    def check_status(self) -> None:
        if (get_current_time() - self.last_fed_time).days > 7:
            self.alive = False
            logger.info(f"{self.name} has died due to neglect.")

    def to_dict(self) -> Dict[str, any]:
        return {
            "id": self.id,
            "owner": self.owner,
            "name": self.name,
            "birth_time": datetime_to_str(self.birth_time),
            "age": self.age,
            "stage": self.stage,
            "type": self.type,
            "biotype": self.biotype,
            "condition": self.condition,
            "happiness": self.happiness,
            "last_fed_time": datetime_to_str(self.last_fed_time),
            "last_walk_time": datetime_to_str(self.last_walk_time),
            "last_bath_time": datetime_to_str(self.last_bath_time),
            "alive": self.alive,
            "food_history": self.food_history,
            "items": self.list_items(),
            "overall_score": self.overall_score
        }
