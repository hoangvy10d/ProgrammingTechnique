class Manager:
    def __init__(self,ManagerID, ManagerName, LoginName, Password):
        self.ManagerID=ManagerID
        self.ManagerName=ManagerName
        self.LoginName=LoginName
        self.Password=Password
    def __str__(self):
        return f"{self.ManagerID}\t{self.ManagerName}\t{self.LoginName}\t{self.Password}"