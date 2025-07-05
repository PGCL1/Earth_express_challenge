class KPI:
    def __init__(self, name: str, value: int, variation: int):
        self.name = name
        self.value = value
        self.variation = f"{variation} + %"
        # self.df_references = df_references // not sure how to access df for getVariation

    def show(self):
        print(f"KPI {self.name}: {self.value} varied by\
                {self.variation} compared to last year")


# KPI can be constructed like so
# KPI("Value Engineering Emissions", 10, 0.1)
# or like so, if you want the result to be actualized when change in value or variation
# KPI("Testing", lambda: getValue(col_name), lambda: getVariation(col_name))

def get_kpi_variation(kpi: object):
    pass
