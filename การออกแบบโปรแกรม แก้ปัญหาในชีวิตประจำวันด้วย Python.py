print("สวัสดีครับ ยินดีต้อนรับสู่โปรแกรมการคำนวณ")
print("")
Menu = 0
while Menu != 5:
  print("##################################")
  print("# 1.การแบ่งช่วงวัยตามอายุ               ")
  print("# 2.การหาค่า BMI (ดัชนีมวลกาย)     ")
  print("# 3.การเปลี่ยนหน่วยอุณหภูมิ (C/F)    ")
  print("# 4.แม่สูตรคูณ                    ")  
  print("# 5.ออกจากโปรแกรม              ")
  print("##################################")
  print("")
  Menu = int(input(" โปรดเลือกโปรแกรมที่ต้องการ :"))
  print("")

  if Menu == 1 :
   print("# 1.การแบ่งช่วงวัยตามอายุ")
   age=int(input("* อายุ :"))
   if age>=12 and age <=14:
     print("ย่างเข้าสู่วัยรุ่น")
   elif age>=14 and age<=21:
     print("วัยรุ่น")
   elif age>=21 and age<=40:
     print("วัยผู้ใหญ่")
   elif age>=40 and age<=60:
     print("วัยผกลางคน")
   elif age>=60 and age<=80:
     print("วัยสูงอายุ")
   elif age>=80:
     print("วัยชรา")
   else :
     print("วัยเด็ก")
   print("")

  elif Menu == 2 :
    print("# 2.การหาค่า BMI (ดัชนีมวลกาย) ")
    high=float(input("* ส่วนสูง (เซนติเมตร) :"))/100 
    weight=float(input("* น้ำหนัก (กิโลกรัม):"))
    BMI = weight/(high**2)
    if BMI>=0 and BMI<18.0:
     result=("ผอม / นํ้าหนักน้อย")
    elif BMI>=18.5 and BMI<=22.9:
     result=("สมส่วน (สุขภาพดี)")
    elif BMI>=23.0 and BMI<=24.9:
     result=("ท้วม / โรคอ้วนระดับ 1")
    elif BMI>=25.0 and BMI<=29.9:
     result=("อ้วน / โรคอ้วนระดับ 2")
    elif BMI>30:
     result=("อ้วนมาก / โรคอ้วนระดับ 3")
    else :
     print("ค่าที่ชัดเจน")
    print("ค่า bmi = ", BMI)
    print("คาดว่า =",result)
    print("")

  elif Menu == 3 :
    print("การเปลี่ยนหน่วยอุณหภูมิ (เซลเซียส(C) / ฟาเรนไฮต์(F)") 
    temp = input("* ใส่อุณหภูมิ ตามด้วยหน่วยองศา C/F :") 
    degree= float(temp[:-1]) 
    unit=temp[-1].upper() 
    if unit=="C":
     result=(9*degree)/5+32
     unit_result="ฟาเรนไฮน์"
     print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)
     print("")
    elif unit=="F":
     result=(degree-32)*5/9
     unit_result="เซลเซียส"
     print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)
     print("")
    else :
     print("* ลืมใส่หน่วย(C,F) ตัวอย่าง 77F , 25C หรือใส่หน่วยผิด ")
     print("")

  elif Menu == 4 :
   print("# 4.แม่สูตรคูณ    ")
   n = int(input("* ใส่แม่สูตรคูณ "))
   for i in range(12) :
     a=i+1
     print(n, "x", a, "=", n * a)
     print("")

  elif Menu == 5 :
    print("##################################")
    print("* ขอขอบคุณที่ใช้โปรแกรมการคำนวณนี้และถ้าหากมีข้อผิดพลาดต้องขออภัยเป็นอย่างสูง")
    print("* จัดทำขึ้นโดย : นายคณาธิป นอกขุนทด ม.4/4 เลขที่ 27")
    print("##################################")

  else :
    print("* โปรดเลือกโปรแกรมที่กำหนดเท่านั้น")
    print("")

