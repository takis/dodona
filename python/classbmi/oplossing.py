class BMI:
    def __init__(self, gewicht, lengte):
        self.gewicht = gewicht
        self.lengte = lengte
    
    def bmi(self):
        return round(self.gewicht/self.lengte**2, 1)
