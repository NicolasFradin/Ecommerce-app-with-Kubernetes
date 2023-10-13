from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.orders import OrderModel, CustomerModel
from app.schemas.orders import Order, OrderCreate
from app.db.db import get_session

from app.services.base import BaseService

class OrderService(BaseService[OrderModel, Order, OrderCreate]):
    def __init__(self, db_session: Session):
        super(OrderService, self).__init__(OrderModel, db_session)        # It would be possible to write: super().__init__(OrderModel, db_session)


    # def create(self, obj: OrderCreate) -> OrderModel:
    #     """
    #     Get the customer for this order
    #     :param obj: OrderCreate
    #     :return: OrderModel
    #     """
    #     customer = self.db_session.get(CustomerModel, obj.customer_id)
    #     if customer is None:
    #         raise HTTPException(
    #             status_code=400,
    #             detail=f"Customer with customer_id = {obj.customer_id} not found.",
    #         )
    #     return super(OrderService, self).create(obj)


def get_order_service(db_session: Session = Depends(get_session)) -> OrderService:
    return OrderService(db_session)

