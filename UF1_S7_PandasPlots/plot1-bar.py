import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter", "Sarah"]
grades_list = [7,9,8,4,5]
wants_fct_list = [False,True,False,True, True]
dades: dict[list] = {"grade": grades_list,
                   "fct": wants_fct_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = dades
)
students_frame = students_frame.sort_values(by=['grade'], ascending=False)

#Seleccionem la info que volem i generem el gràfic.
students_frame.loc[:,"grade"].plot(kind="bar")


# Per a què es mostri el gràfic amb IPYNB o amb IPython:
# plt.show()

# Per a què es mostri el gràfic amb Python cal guardar-lo en fitxer.
plt.savefig('intro-barplot1.png')
