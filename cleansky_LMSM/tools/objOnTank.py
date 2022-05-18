class ObjOnTank:
    def __init__(self, tp, loc=None, co=(0, 0, 0), me=((0, 0, 0), (0, 0, 0), (0, 0, 0))):
        self.tp = tp
        self.location = loc
        self.coord = co
        self.metric = me

    def is_coating(self) -> bool:
        return self.tp == 'Coating'


class TankConfig:
    def __init__(self, tank_type: str, tank_number: str, name: str, s: set):
        self.tp = tank_type
        self.tn = tank_number
        self.name = name
        self.obj_set = s

    def add_obj(self, obj: ObjOnTank):
        self.obj_set.add(obj)

    def rm_obj(self, obj: ObjOnTank):
        if obj in self.obj_set:
            self.obj_set.remove(obj)

    def is_exist_obj(self, obj: ObjOnTank) -> bool:
        return obj in self.obj_set
