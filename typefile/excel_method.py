import xlrd
import xlwt

# 打开excel文件
workbook = xlrd.open_workbook(r'300.xlsx')
# 读取指定sheet
sheet = workbook.sheet_by_name('300')
# 创建excel对象
excel = xlwt.Workbook()
# 创建一个sheet
newsheet = excel.add_sheet('Sheet1')
for i in range(1,sheet.nrows):
    # 读取行数据
    rows = sheet.row_values(i)
    # 读取对应行数据中的第几列数据
    data = rows[1]
    # 将读取的data写入另一excel文件
    newsheet.write(i,0,data)
# 保存excel对象到excel文件
excel.save("300s.xls")