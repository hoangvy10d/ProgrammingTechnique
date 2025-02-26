class User:
    def __init__(self, UserID, UserName, LoginName, Password, Email, SignUpDate, FanficNumber):
        self.UserID = UserID
        self.UserName = UserName
        self.LoginName = LoginName
        self.Password = Password
        self.Email = Email
        self.SignUpDate = SignUpDate
        self.FanficNumber = FanficNumber

    def __str__(self):
        return (f"{self.UserID}\t{self.UserName}\t{self.LoginName}\t{self.Password}"
                f"\t{self.Email}\t{self.SignUpDate}\t{self.FanficNumber}")