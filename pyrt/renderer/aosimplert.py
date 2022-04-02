from .simplert import *

class AOSimpleRT(SimpleRT):

    def __init__(self, shadow=False, iterations=1, n_aorays=64, aoray_len=1.):
        super().__init__(shadow, iterations)
        
        self.aorays_len = aoray_len
        self.random_directions = [Vec3(*((random.uniform(-1, 1)) for _ in range(3))) for _ in range(n_aorays)]
    
    def _shade(self, scene: Scene, ray: Ray, hitrecord: HitRecord) -> tuple:
        
        hit, r, g, b = super()._shade(scene, ray, hitrecord)
        if not hit:
            return hit, r, g, b

        ao = self._get_ao(scene, hitrecord)
        r, g, b = ((1 - ao) * x for x in [r, g, b])

        return hit, r, g, b

    def _get_ao(self, scene: Scene, hitrecord: HitRecord):
        
        n_ao = 0
        for random_ray in self._random_rays_range(hitrecord.normal_g, hitrecord.point):
            for node in scene.nodes:
                if node == hitrecord.obj: 
                    continue
                hit = HitRecord()
                if  node.hit(random_ray, hit) and (hit.point - random_ray.start).length() < self.aorays_len:
                    n_ao += 1
                    break

        return n_ao / len(self.random_directions)

    def _random_rays_range(self, normal: Vec3, start: Vec3, epsilon: float = 0.01):
        for direction in self.random_directions:
            
            if direction.dot(normal) < 0:
                normal_direction = -1. * direction
            else:
                normal_direction = direction

            yield Ray(start, normal_direction)

