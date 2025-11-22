class Distance:
    CONVERT_TO_M = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.CONVERT_TO_M[self.unit]

    @staticmethod
    def from_meters(meters_value, unit):
        reverse = {
            "cm": meters_value * 100,
            "m": meters_value,
            "km": meters_value / 1000
        }
        return Distance(reverse[unit], unit)

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        return Distance.from_meters(total_meters, self.unit)

d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(150, "cm")

print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)

print("\n=== Сложение ===")
print("10 m + 2 km =", d1 + d2)
print("150 cm + 10 m =", d3 + d1)
