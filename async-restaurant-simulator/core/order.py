from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Order:
    order_id: int
    customer_name: str
    item: str
    served_at: None
    amount: float = 0.0
    attempts: int = 0
    item_prep_time: int = 0
    waiter_name: str = ""
    status: str = "Pending"
    placed_at: datetime = field(default_factory=datetime.now)

    def duration(self):
        if self.served_at:
            return (self.served_at - self.placed_at).total_seconds()
        return None
