
class CountFromBy:

    def __init__(self, val: int = 0, step: int = 1) -> None:
        """Initialized the CountFromBy class"""
        self.val = val
        self.step = step

    def increase(self) -> None:
        """Increments the counter"""
        self.val += self.step

    def __repr__(self) -> str:
        """Returns string representation of the object"""
        return str(self.val)


c1 = CountFromBy()
c2 = CountFromBy(100)
c3 = CountFromBy(1000, 500)

print(c1)
print(c2)
print(c3)

for i in range(10):
    c1.increase()
    c2.increase()
    c3.increase()

print('After.....')
print(c1)
print(c2)
print(c3)