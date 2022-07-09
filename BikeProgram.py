class Bike:
    def __init__(self,name,model,fuelType,color,noOfWheels,milage):
        self.name=name
        self.model=model
        self.fuelType=fuelType
        self.color=color
        self.noOfWheels=noOfWheels
        self.milage=milage
    def show(self):
        print(self.name,self.model,self.fuelType,self.color,self.noOfWheels,self.milage)
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
print("----------------MENU---------------")
print("press 1 to add new Bike")
print("press 2 to show all the bikes available")
print("press 3 to update existing bike details")
print("press 4 to retrive particular Bike")
print("press 5 to delete Bike")
print("press 6 to retrive no of bikes we have")
print("press 7 to retrive bikes of particular colour")
print("press 8 bikes sort by name ")
print("press 9 to sort based on milage")
print("press 10 to exit")
def retirve(temp):
    for i in temp:
        i.show()
def delete(name):
    flag=False
    for i in temp:
        if(i.getName()==name):
            temp.remove(i)
            flag=True
        if(flag==False):
            print("bike not found")
def find(val):
    for i in temp:
        if(i.getName()==val):
            return i
    print("bike not found")
def retrieveClr(val):
    for i in temp:
        if(i.getColor()==val):
            i.show()
def modify(val):
    print("----------------MENU---------------")
    print("1.fuel type")
    print("2.colour")
    print("3.no of wheels")
    print("4.milage")
    n=int(input("enter field to modify :"))
    for i in temp:
         if(i.getName()==val):
            new=input("enter new value : ")
            if(n==1):
                i.fuelType=new
            elif(n==2):
                i.color=new
            elif(n==3):
                i.noOfWheels=int(new)
            else:
                i.milage=int(new)
            break
    print("record not found")
def sortName(data):
    data.sort(key=lambda a:a.name)
    return data
def sortMilage(data):
    data.sort(key=lambda a:a.milage,reverse=True)
    return data
temp=[]
while True:
    a=int(input("enter the choice:-"))          
    if a==1:
        print("enter bike details :")
        name=input("name : ")
        model=int(input("model : "))
        fuelType=input("fuel type : ")
        color=input("colour : ")
        noOfWheels=int(input("No of wheels : "))
        milage=int(input("Milage : "))
        bike=Bike(name,model,fuelType,color,noOfWheels,milage)
        temp.append(bike)
    elif a==2:
        retirve(temp)
    elif a==3:
        val=input("enter record name to modify:")
        modify(val)
    elif a==4:
        val=input('enter name of bike : ')
        st=find(val)
        st.show()
    elif a==5:
        val=input("enter name of bike to delete : ")
        delete(val)
    elif a==6:
        print(len(temp))
    elif a==7:
        clr=input("enter colour : ")
        retrieveClr(clr)
    elif a==8:
        rec=sortName(temp)
        retirve(rec)
    elif a==9:
        rec=sortModel(temp)
        retirve(rec)
    else:
        break
