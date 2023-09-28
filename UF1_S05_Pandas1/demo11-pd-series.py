import numpy as np 
import pandas as pd

#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
ser = pd.Series(grades_list)
print(ser)

ser = pd.Series(data=grades_list,index=student_list)
print(ser)

# Expected result.
# John     7
# Mary     9
# Lucy     8
# Peter    4
# dtype: int64

dates = pd.date_range("20230929", periods=6, freq='D')
places = ['Sarria','Portomarín','Palas Do Rei','Arzúa','O Pedrouzo','Santiago']
s2 = pd.Series(data=places,index=dates, dtype="string")
print(dates)
print(s2)

id_classrooms = list(range(41,45))
list_classrooms = [f'or{room}' for room in id_classrooms]
serie_classrooms = pd.Series(data=list_classrooms, index=id_classrooms, dtype="string")
print(serie_classrooms)
