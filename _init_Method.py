class Boy:
    def __init__(self,name,height,weight):
        self.name = name
        self.height=height
        self.weight=weight


    def config(self):
        print("name is:",self.name, ",", "height is:",self.height ,"," , "weight is:",self.weight ,".")

Boy1=Boy("ram",5,50)
Boy2=Boy("rohan",6,40)
Boy3=Boy("shan",7,60)

Boy1.config()
Boy2.config()
Boy3.config()