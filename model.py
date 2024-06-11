class FormCategory:
    _data_base = "category.txt"

    def getAllCategory(self):
        link = open(self._data_base, "r")
        data = link.readline()
        print(data)

FormCategory.getAllCategory()
    # _data_hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

    # _data_name = ["Саша", "Sasha", "usasha", "main Alex"]

    # def getDataHello(self):
    #     return self._data_hello

    # def getAllData(self):
    #     data = list()
    #     for id in range(4):
    #         lang_data = {
    #             "msg": self._data_hello[id-1],
    #             "name": self._data_name[id-1],
    #         }
    #         data.append(lang_data)
    #     return data

# class NameModel:
    

#     def getDataName(self):
#         return self._data_name
    
