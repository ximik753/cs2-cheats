import pyMeow as pm
from module.offsets import Offsets

class Entity:
    def __init__(self, pointer, pawnPointer, process):
        self.pointer = pointer
        self.pawnPointer = pawnPointer
        self.process = process
        self.pos2d = None
        self.headPos2d = None

    def Health(self):
        return pm.r_int(self.process, self.pawnPointer + Offsets.m_iHealth)

    def Team(self):
        return pm.r_int(self.process, self.pawnPointer + Offsets.m_iTeamNum)

    def Pos(self):
        return pm.r_vec3(self.process, self.pawnPointer + Offsets.m_vOldOrigin)

    def EyePos(self):
        pos = pm.r_vec3(self.process, self.pawnPointer + Offsets.m_vecViewOffset)
        for k in pos:
            pos[k] = pos[k] + self.Pos().get(k)
        return pos

    def Wts(self, matrix):
        try:
            self.pos2d = pm.world_to_screen(matrix, self.Pos(), 1)
            self.headPos2d = pm.world_to_screen(matrix, self.EyePos(), 1)
        except:
            return False
        
        return True
