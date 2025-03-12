class Base:
    pass


class Left(Base):
    pass

class Right(Base):
    pass


class Child(Left, Right):
    pass
cild=Child()
cild.call()