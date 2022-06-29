class QueryBuilder:
    def __init__(self) -> None:
        self.select_value = ""
        self.from_value = ""
        self.where_value = ""
        self.group_by_value = ""

    def select(self, value):
        self.select_value = value
        return self

    def from_table(self, value):
        self.from_value = value
        return self

    def where(self, value):
        self.where_value = value
        return self

    def group_by(self, value):
        self.group_by_value = value
        return self

    def build(self):
        return f"""
        SELECT {self.select_value}
        FROM {self.from_value}
        WHERE {self.where_value}
        GROUP BY {self.group_by_value}
        """
