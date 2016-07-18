import unittest

from pyrt.math import *


# -- Testing Vec3 Class ------------------------------------------------------------------------------------------------

class Vec3Test(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------------
    def testStandardConstructor(self):
        s = Vec3(1, 2, 3)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testTupleConstructor(self):
        s = Vec3((1,2,3))
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testListConstructor(self):
        s = Vec3([1, 2, 3])
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testNamedConstructor(self):
        s = Vec3(x=1)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 0.0)

        s = Vec3(y=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 1.0)
        self.assertEqual(s.z, 0.0)

        s = Vec3(z=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 1.0)

        s = Vec3(x=1, y=2, z=3)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testAccess(self):
        a = Vec3(5,6,7)
        self.assertEqual(a.x, 5.0)
        self.assertEqual(a.y, 6.0)
        self.assertEqual(a.z, 7.0)

        self.assertEqual(a[0], 5.0)
        self.assertEqual(a[1], 6.0)
        self.assertEqual(a[2], 7.0)

        a[0] = 10
        a[1] = 11
        a[2] = 12
        self.assertEqual(a[0], 10.0)
        self.assertEqual(a[1], 11.0)
        self.assertEqual(a[2], 12.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testWrongConstructor(self):
        self.assertRaises(ValueError, Vec3, 1,2,3,x=5)

    # ------------------------------------------------------------------------------------------------------------------
    def testEqual(self):
        a = Vec3(4.5, 5.5, 6.5)
        b = Vec3(4.5, 5.5, 6.5)
        c = Vec3(5,4,3)

        self.assertEqual(a,b)
        self.assertEqual(a, (4.5, 5.5, 6.5))
        self.assertEqual(a, [4.5, 5.5, 6.5])
        self.assertNotEqual(a,c)

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        a = Vec3(1,2,3)
        b = Vec3(2,3,4)
        c = a * b
        d = 3 * b
        e = b * 3
        x = Vec3(2,2,2)
        self.assertEqual(c, (2,6,12))
        self.assertEqual(d, (6,9,12))
        self.assertEqual(a*b*x, (4,12,24))
        self.assertEqual(d,e)

    # ------------------------------------------------------------------------------------------------------------------
    def testDivision(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(4, 4, 5)
        v3 = v1 / v2
        self.assertEqual(v3, (0.25, 0.5, 0.6))

        v4 = Vec3(2,4,6)
        v5 = v4 / 2.0
        self.assertEqual(v5, (1.0, 2.0, 3.0))

        v6 = Vec3(2, 4, 8)
        v7 = 2.0 / v6
        self.assertEqual(v7, (1.0, 0.5, 0.25))

        v8 = Vec3(2, 25, 16)
        v9 = Vec3(4, 5, 8)
        v10 = v8 / v9
        self.assertEqual(v10, (0.5, 5.0, 2.0))

    # ------------------------------------------------------------------------------------------------------------------
    def testFunctions(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(3, 4, 5)
        v3 = cross(v1,v2)

        self.assertEqual(v3, (-2.0, 4.0, -2.0))

        s = normalize(v1)

        self.assertEqual(s, (0.2672612419124244, 0.5345224838248488, 0.8017837257372732))

# -- Testing Vec4 Class ------------------------------------------------------------------------------------------------

class Vec4Test(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def testStandardConstructor(self):
        s = Vec4(1, 2, 3, 4)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)
        self.assertEqual(s.w, 4.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testTupleConstructor(self):
        s = Vec4((1, 2, 3, 4))
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)
        self.assertEqual(s.w, 4.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testListConstructor(self):
        s = Vec4([1, 2, 3, 4 ])
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)
        self.assertEqual(s.w, 4.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testNamedConstructor(self):
        s = Vec4(x=1)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 0.0)
        self.assertEqual(s.w, 1.0)

        s = Vec4(y=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 1.0)
        self.assertEqual(s.z, 0.0)
        self.assertEqual(s.w, 1.0)

        s = Vec4(z=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 1.0)
        self.assertEqual(s.w, 1.0)

        s = Vec4(x=1, y=2, z=3, w=4)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)
        self.assertEqual(s.w, 4.0)

    # ------------------------------------------------------------------------------------------------------------------
    def testEqual(self):
        s = Vec4(1,2,3,4)
        self.assertEqual(s, (1,2,3,4))
        self.assertEqual(s, [1,2,3,4])

# -- Testing Mat4 Class ------------------------------------------------------------------------------------------------

class Mat4Test(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------------
    def testConstructor(self):
        # 1 - Construct Empty
        m = Mat4()
        self.assertEqual(m, (0,0,0,0,
                             0,0,0,0,
                             0,0,0,0,
                             0,0,0,0))

        # 2 - Construct as tuple
        m = Mat4((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
        self.assertEqual(m, (1, 2, 3, 4,
                             5, 6, 7, 8,
                             9, 10, 11, 12,
                             13, 14, 15, 16))

        # 2 - Construct as list
        m = Mat4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(m, (1, 2, 3, 4,
                             5, 6, 7, 8,
                             9, 10, 11, 12,
                             13, 14, 15, 16))

    # ------------------------------------------------------------------------------------------------------------------
    def testAccess(self):
        m = Mat4((1, 2, 3, 4,
                  5, 6, 7, 8,
                  9, 10, 11, 12,
                  13, 14, 15, 16))

        self.assertEqual(m[0, 0], 1.0)
        self.assertEqual(m[1, 0], 2.0)
        self.assertEqual(m[2, 0], 3.0)
        self.assertEqual(m[3, 0], 4.0)

        self.assertEqual(m[0, 1], 5.0)
        self.assertEqual(m[1, 1], 6.0)
        self.assertEqual(m[2, 1], 7.0)
        self.assertEqual(m[3, 1], 8.0)

        self.assertEqual(m[0, 2], 9.0)
        self.assertEqual(m[1, 2], 10.0)
        self.assertEqual(m[2, 2], 11.0)
        self.assertEqual(m[3, 2], 12.0)

        self.assertEqual(m[0, 3], 13.0)
        self.assertEqual(m[1, 3], 14.0)
        self.assertEqual(m[2, 3], 15.0)
        self.assertEqual(m[3, 3], 16.0)


    # ------------------------------------------------------------------------------------------------------------------
    def testAddition(self):
        m0 = Mat4([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32])
        m1 = Mat4([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

        m2 = m0 + m1

        self.assertEqual(m2,(3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33))

    # ------------------------------------------------------------------------------------------------------------------
    def testSubtraction(self):
        m0 = Mat4([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])
        m1 = Mat4([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        m2 = m0 - m1

        self.assertEqual(m2, (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31))

    # ------------------------------------------------------------------------------------------------------------------
    def testTranspose(self):
        m0 = Mat4( [2,4,6,8,
                    10,12,14,16,
                    18,20,22,24,
                    26,28,30,32])

        m0.transpose()

        self.assertEqual(m0, (2,10,18,26,
                              4,12,20,28,
                              6,14,22,30,
                              8,16,24,32))

    # ------------------------------------------------------------------------------------------------------------------
    def testMultiplication(self):
        q0 = Mat4([1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15, 16])

        q1 = Mat4([17, 18, 19, 20,
                   21, 22, 23, 24,
                   25, 26, 27, 28,
                   29, 30, 31, 32])

        q3 = q0 * q1
        self.assertEqual(q3, (250, 260, 270, 280, 618,644,670,696,986,1028,1070,1112,1354,1412,1470,1528))

    # ------------------------------------------------------------------------------------------------------------------
    def testIdentity(self):
        m = CreateIdentity4()
        self.assertEqual(m, (1, 0, 0, 0,
                             0, 1, 0, 0,
                             0, 0, 1, 0,
                             0, 0, 0, 1))


    # ------------------------------------------------------------------------------------------------------------------





"""
from pyrt.math import *
from pyrt.geometry import Triangle
from pyrt.camera import PerspectiveCamera
#from pyrt.renderer import SimpleRT

print("Hello World!")

v = Vec3(1.0, 2.0, 3.0)

cam = PerspectiveCamera()
"""



if __name__ == '__main__':
    unittest.main()
