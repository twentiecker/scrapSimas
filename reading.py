class Reading:
    def __init__(self):
        self.list_pagination = []
        self.list_profil = []

    def read_pagination(self, file_name):
        f = open(f"{file_name}.csv", "r", encoding="utf-8")
        f1 = f.readlines()
        for x in f1:
            self.list_pagination.append(x.strip())
            print(x.strip())
        f.close()

    def read_profil(self, file_name):
        f = open(f"{file_name}.csv", "r", encoding="utf-8")
        f1 = f.readlines()
        for x in f1:
            self.list_profil.append(x.strip())
            print(x.strip())
        f.close()
