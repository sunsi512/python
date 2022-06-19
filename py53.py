# import pandas as pd
# import openpyxl.workbook import Workbook
# import matplotlib.pyplot as 

# def 표만들기():

#     번호 = [1,2,3]
#     data = {
#         '이름':['홍길동', '아무개','김철수'],
#         '키':[175.5, 166.3, 180.0]
#     }


#     df = pd.DataFrame(data, index=번호)
#     print(df)

#     df.to_csv('myTadle.txt', sep = '\t')

#     df.to_csv('myTadle.txt', index=False)

#     # 읽기
#     df2 = pd.read_excel('myTable.xlsx')
#     print(df2)

#340p

from matplotlib import font_manager
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun']
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle='--', marker = '^')
plt.show()


def 원형그래프():
    font_name = font_manager.FontProperties(fname='H2PORM.TTF').get_name()
    plt.rc('font', family=font_name)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]
    label = ['비타민 A', '비타민 B1', '비타민 B2', '나이아신', '비타민 B6', '비타민 C', '비타민 D', '비타민 E', '염산']
    axes.pie(data, labels=label,autopct = '%d%%')
    plt.axis('equal')
    plt.legend(label, loc='center left')
    plt.show()

원형그래프()