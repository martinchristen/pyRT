import math

G_EPSILON = 1E-24

class Vec3:
    """Class representing a 3D-Vector
    params:
       x,y,z Component of vector (float or int)
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        :param x: x-component 
        :param y: y-component
        :param z: z-component
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """Convert vector to string
        """
        return "Vec3(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __add__(self, other):
        """add two vectors
        other: vector to add"""
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """subtract two vectors
        other: vector to subtract"""
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x * s.x, self.y * s.y, self.z * s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x * s, self.y * s, self.z * s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0.,0.,0.)

    def __rmul__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x * s.x, self.y * s.y, self.z * s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x * s, self.y * s, self.z * s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __div__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x / s.x, self.y / s.y, self.z / s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x / s, self.y / s, self.z / s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __rdiv__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x / s.x, self.y / s.y, self.z / s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x / s, self.y / s, self.z / s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def isZero(self):
        return math.fabs(self.x) < G_EPSILON and math.fabs(self.y) < G_EPSILON and math.fabs(self.z) < G_EPSILON

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        l = self.length()
        if l != 0:
            self.x /= l
            self.y /= l
            self.z /= l

    def set(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z


# Vector operations:
# ------------------

def cross(v1, v2):
    """Calculates cross product
    v1: vector
    v2: vector
    """
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vec3(x, y, z)

def dot(a,b):
    """calculates the dot product"""
    return a.x * b.x + a.y * b.y + a.z * b.z


def normalize(v):
    """Returns the normalized vector without modifying the original vector"""
    l = v.length()
    if l != 0:
        return Vec3(v.x / l, v.y / l, v.z / l)
    else:
        return Vec3(0.0, 0.0, 0.0)


def reflect(N, I):
    """Reflects a vector
    N: Normal
    I: Incdient vector"""
    return I + N * (-2.0 * dot(N, I))


def faceforward(N, I):
    '''
    faceforward operation
    N: Normal vector
    I: Incident vector
    '''
    if dot(N, I) < 0:
        return N
    else:
        return -N


def refract(N, I, eta):
    '''
    refract operation
    N: Normal vector
    I: Incident vector
    eta: Refraction koefficient
    '''
    d = dot(I, N)
    k = 1 - eta * eta * (1 - d * d)
    if k < 0:
        return I
    else:
        return I * eta - N * (eta * d + math.sqrt(k))



def sign(v):
    def fsign(f):
        if f < 0:
            return -1
        if f > 0:
            return 1
        else:
            return 0

    Vec3(fsign(v.x), fsign(v.y), fsign(v.z))


def vec3copy(v):
    return Vec3(v.x, v.y, v.z)
