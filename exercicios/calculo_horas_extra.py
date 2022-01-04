from datetime import datetime

var = '18:23:00'
var2 = '09:00:00'
var3 = '08:00:00'
formata = "%H:%M:%S"
times = (datetime.strptime(var, formata) - datetime.strptime(var2, formata))
times = str(times)
var5 = datetime.strptime(times, formata) - datetime.strptime(var3, formata)
print(type(times), times)
print(type(var5), var5)