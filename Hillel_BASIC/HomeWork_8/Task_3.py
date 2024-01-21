# Як і 2му завданні маємо data  у вигляді строки(прочитано з файла) Теж таблиця.
# ship_mode -  деякий режим продажу
# sales - продажі
# Завданя :
# підрахувати і вивести репорт у вигляді таблички:
# скільки окремо продано в режимах : Standard, Second , First

data = """id,order_date,ship_mode,customer_id,sales
100006,2014-09-07,Standard,DK-13375,377.97
100090,2014-07-08,Standard,EB-13705,699.192
100293,2014-03-14,Standard,NF-18475,91.056
100328,2014-01-28,Standard,JC-15340,3.928
100363,2014-04-08,Standard,JM-15655,21.376
100391,2014-05-25,Standard,BW-11065,14.62
100678,2014-04-18,Standard,KM-16720,697.074
100706,2014-12-16,Second,LE-16810,129.44
100762,2014-11-24,Standard,NG-18355,508.62
100860,2014-03-26,Second,CS-12505,18.75
100867,2014-10-19,Standard,EH-14125,321.552
100881,2014-03-28,Standard,DR-12940,302.376
100895,2014-06-02,Standard,SV-20785,605.47
100916,2014-10-21,Standard,FH-14275,788.86
100972,2014-11-19,Second,DB-13360,166.44
101147,2014-12-02,First,MC-17575,2.394
101175,2014-12-09,Standard,DM-12955,100.704
101266,2014-08-27,Second,MM-17920,13.36
101364,2014-12-22,Standard,TW-21025,296.712
101392,2014-12-07,Standard,AS-10630,269.36
101427,2014-12-26,Standard,AY-10555,8.016
101462,2014-04-20,Standard,BP-11230,59.92
101476,2014-09-12,First,SD-20485,69.99
101560,2014-11-28,Second,CS-12250,542.34
101602,2014-12-15,First,MC-18100,803.96
101770,2014-03-31,Standard,KB-16240,1.869
101833,2014-11-17,Second,FG-14260,34.44
101931,2014-10-28,First,TS-21370,1252.602"""

my_list = data.split("\n")

standard_sales = 0
first_sales = 0
second_sales = 0

new_list = [i.split(",") for i in my_list]

for item in new_list:
    if "Standard" in item:
        standard_sales += float(item[4])
    elif "First" in item:
        first_sales += float(item[4])
    elif "Second" in item:
        second_sales += float(item[4])

final_table = [
    ["Standard Sales", "First Sales", "Second Sales"],
    [round(standard_sales, 3), round(first_sales, 3), round(second_sales, 3)],
]

for row in final_table:
    print(f"{row[0]: >15} {row[1]: >15} {row[2]: >15}")
