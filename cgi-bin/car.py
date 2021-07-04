#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "MH12 DE1433":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Number : MH12DE1433
    License No : xxxxxxxxxx
    Registration date : 28-FEB-2006
    Chassis Number : MAJBXXMRTB6YB7466
    Engine Number : 6YB7466
    Fuel Type : PETROL
    Model/Model Name : FORD
    Color : Grey
    Owner Name : GOLWILKAR JAYANT
    Vehicle Class : MOTOR CAR(LMV)
    RTO Code : MH12
    Vehicle RTO : PUNE
           </pre>''')
    print("</body>")

elif plate_no == "KAGSMT 8654":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Number : KA05MT8654
    License No : xxxxxxxxxx
    Registration Date : 2016-08-10
    Chassis Number : MA3ETDE1S00326011
    Engine Number : K10BN1979577
    Fuel Type : PETROL
    Model/Model Name : MARUTI SUZUKI
    Owner Name : PRATHIBA H K
    Vehicle Class : MOTOR CAR(LMV)
    Insurance expiry : 2021-08-10
    RTO Code : KA05
    Vehicle RTO : BANGALORE SOUTH (JAYANAGAR)]]
    </pre>''')
    print("</body>")

elif plate_no == "KA 05 NB 1786":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Number : KA05 NB1786
    License No : xxxxxxxxxxx
    Make / Model : KIA / SELTOS
    Registration Date : 1/12/2020
    Registering Authority : GUJARAT, INDIA
    Fuel Type : DIESEL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2030
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
