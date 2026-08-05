class CalculateArea:
    
    def rectangle_area(self, w, h):
        return w * h
    
    @classmethod
    def triangle_area(self, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        import math
        return math.pi * r * r
    
cal = CalculateArea()
cal_rec = cal.rectangle_area(5, 10)
cal_tri = CalculateArea.triangle_area(5, 10)
cal_cir = CalculateArea.circle_area(7)

print("Area of Rectangle:", cal_rec)
print("Area of Triangle:", cal_tri)
print("Area of Circle:", cal_cir)

print('Test triangle_area method:', CalculateArea.triangle_area(3, 6))
print('Test circle_area method:', CalculateArea.circle_area(10))
print('Test rectangle_area method:', cal.rectangle_area(4, 8))