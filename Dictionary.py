garry_gajultos = {"Name":"Garry Gajultos","Age":19,"Motto":"Mga bobo","Games":['DOTA','CF']}
print(garry_gajultos["Name"],garry_gajultos["Age"],garry_gajultos["Motto"],garry_gajultos["Games"][0])
garry_gajultos = [{"Name":"Garry","Age":"19"},{"Surname":"Gajutos","Age":"18"}]
print(garry_gajultos[1]["Age"])

listSlum = []
dictPage = {}
dictPage["Name"] = str(input("Enter Name: "))
dictPage["Age"] = int(input("Enter Age: "))
dictPage["Games"] = str(input("Enter your Game: "))
listSlum.append(dictPage)
print(listSlum)