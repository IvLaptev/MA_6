# /app/repositories/bd_delivery_repo.py

from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.delivery import Delivery
from app.schemas.delivery import Delivery as DBDelivery


class DeliveryRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db)

    def get_deliveries(self) -> list[Delivery]:
        deliveries = []
        for d in self.db.query(DBDelivery).all():
            deliveries = Delivery.from_orm(d)
        return deliveries

    def get_delivery_by_id(self, id: UUID) -> Delivery:
        delivery = self.db \
            .query(DBDelivery) \
            .filter(DBDelivery.id == id) \
            .first()
            
        if delivery == None:
            raise KeyError

        return Delivery.from_orm(delivery)

    def create_delivery(self, delivery: Delivery) -> Delivery:
        if len([d for d in deliveries if d.id == delivery.id]) > 0:
            raise KeyError

        deliveries.append(delivery)
        return delivery

    def set_status(self, delivery: Delivery) -> Delivery:
        for d in deliveries:
            if d.id == delivery.id:
                d.status = delivery.status
                break

        return delivery

    def set_deliveryman(self, delivery: Delivery) -> Delivery:
        for d in deliveries:
            if d.id == delivery.id:
                d.deliveryman = delivery.deliveryman
                break

        return delivery
