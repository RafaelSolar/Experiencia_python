import math as mt

class Vector2D():
    def __init__(self,corx=0,cory=0):
        self.x = corx
        self.y = cory
    
    @property
    def module(self):
        return mt.sqrt(self.x**2 + self.y**2)
    
    
    def scalar_prod(self,scalar=1.):
        if scalar ==1:
            scalar = float(input("Introduce el escalar: "))
        #vector = np.array(self.x,self.y)
        self.x = self.x*scalar
        self.y = self.y*scalar
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    
    @classmethod
    def sum(cls,vec1,vec2):
        return cls(vec1.x + vec2.x , vec1.y + vec2.y)
    
    @classmethod
    def subtrack(cls,vec1,vec2):
        return cls(vec2.x-vec1.x, vec2.y - vec1.y)
    
    @staticmethod
    def dot_product(vec1,vec2):
        return vec1.x*vec2.x + vec1.y*vec2.y
    
    @classmethod
    def distance(cls, vec1,vec2):
        return mt.sqrt((vec1.x - vec2.x)**2+(vec1.y - vec2.y)**2)
    
    def extend_to_3D(self, z=0):
        valorZ = float(input("Introduce el valor de z: "))
        newvector = Vector3D(self.x, self.y,valorZ)
        return newvector

class Vector3D(Vector2D):
    def __init__(self,x,y,z = 0):
        super().__init__(x,y)
        self.z = z
    
    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)
    
    @property
    def module(self):
        return mt.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def scalar_prod(self,scalar = 1):
        if scalar == 1:
            scalar = float(input("Introduce el escalar: "))
        super().scalar_prod(scalar)
        self.z = self.z*scalar
        #vector = np.array(self.x,self.y,self.z)
        
        
    @classmethod
    def sum(cls, vec1, vec2):
        return cls(super().sum(vec1,vec2).x, super().sum(vec1,vec2).y, vec1.z + vec2.z)
    
    @classmethod
    def subtrack(cls, vec1, vec2):
        return cls(super().subtrack(vec1,vec2).x, super().subtrack(vec1,vec2).y , vec2.z-vec1.z)
    
    @staticmethod
    def dot_product(vec1, vec2):
        return super().dot_product(vec1, vec2) + vec1.z*vec2.z
    
    @classmethod
    def distance(cls, vec1, vec2):
        return mt.sqrt((vec1.x - vec2.x)+(vec1.y-vec2.y) + (vec1.z-vec2.z))
    
    @classmethod
    def zero(cls):
        return cls(0,0,0)
    
    @classmethod
    def horizontal(cls):
        return cls(1,0,0)
    @classmethod
    def vertical(cls):
        return cls(0,1,0)
    
    @classmethod
    def forward(cls):
        return cls(0,0,1)