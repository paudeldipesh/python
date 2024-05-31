# Hybrid Inheritance
class BaseClass:
    pass


class DerivedOne(BaseClass):
    pass


class DerivedTwo(BaseClass):
    pass


class DerivedThree(DerivedOne, DerivedTwo):
    pass


# Hierarchical Inheritance
class BaseClass:
    pass


class DerivedOne(BaseClass):
    pass


class DerivedTwo(DerivedOne):
    pass
