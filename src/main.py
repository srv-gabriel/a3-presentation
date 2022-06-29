import numpy as np
import pandas as pd
from sklearn import linear_model

from src.builder.query_builder import QueryBuilder

if __name__ == "__main__":

    query = QueryBuilder()

    query = (
        query.select("Customer, Region, SUM(SaleValue)")
        .from_table("Sales")
        .where("DATEDIFF(day, TimeStamp, CURRENT_TIMESTAMP) < 180")
        .group_by("(Customer, Region)")
    )

    print(query.build())
