from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import pymysql
import time
import tempfile, os
class Covcard:

    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Covid Card System")
        self.root.geometry("1495x800+0+0")
        
        #================================================Frames==================================================
        
        MainFrame = Frame(self.root ,bd=10, width =1515, height=700,  relief=RIDGE)
        MainFrame.grid()

        
        TopFrame1 = Frame(MainFrame ,bd=5, width =1515, height=50 ,relief=RIDGE)
        TopFrame1.grid(row = 2 ,column = 0)
        TitleFrame = Frame(MainFrame ,bd=7, width =1515, height=100 ,relief=GROOVE)
        TitleFrame.grid(row = 0 ,column = 0)
        TopFrame3 = Frame(MainFrame ,bd=5, width =1515, height=550 ,relief=FLAT)
        TopFrame3.grid(row = 1 ,column = 0)
    
        LeftFrame = Frame(TopFrame3 ,bd=5, width =1510, height=540, padx=2,relief=FLAT)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame ,bd=5, width =800, height=240, padx=2,pady=4,relief=GROOVE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)
        
        
        LeftFrame3 = Frame(LeftFrame ,bd=5, width =550, height=200,relief=FLAT)
        LeftFrame3.pack(side=TOP,padx=10,pady=5)
        LeftFrame3Left = Frame(LeftFrame3 ,bd=5, width =400, height=240, padx=2 ,relief=GROOVE)
        LeftFrame3Left.pack(side=LEFT)
        LeftFrame3Right = Frame(LeftFrame3 ,bd=5, width =400, height=240, padx=2 ,relief=GROOVE)
        LeftFrame3Right.pack(side=RIGHT)

        

        LeftFrame4 = Frame(LeftFrame ,bd=5, width =500, height=200,relief=GROOVE)
        LeftFrame4.pack(side=TOP)
        
        LeftFrame2 = Frame(LeftFrame ,bd=5, width =800, height=240, padx=2 ,relief=FLAT)
        LeftFrame2.pack(side=TOP,pady=4)
        LeftFrame2Left = Frame(LeftFrame2 ,bd=5, width =400, height=240, padx=2 ,relief=GROOVE)
        LeftFrame2Left.pack(side=LEFT,pady=4)
        LeftFrame2Right = Frame(LeftFrame2 ,bd=5, width =400, height=240, padx=2 ,relief=GROOVE)
        LeftFrame2Right.pack(side=RIGHT)

        RightFrame1 = Frame(TopFrame3 ,bd=5, width =320, height=700, padx=2,relief=GROOVE)
        RightFrame1.pack(side=RIGHT)


        RightFrame0 = Frame(RightFrame1 ,bd=5, width =320, height=700, padx=2)
        RightFrame0.pack(side=TOP)

        
        RightFrame1a = Frame(RightFrame1 ,bd=5, width =310, height=330, padx=2,pady=2)
        RightFrame1a.pack(side=TOP)


        #==================================================================================================

        CovID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        AadharNo =StringVar()
        District =StringVar()
 
        Stat1=StringVar()
        Dat1=StringVar()
        Hosp=StringVar()
        
        Vacname =StringVar()
        Status1 =StringVar()
        Date1=StringVar()
        Center1=StringVar()
        

        Status2=StringVar()
        Date2=StringVar()        
        Center2=StringVar()

        Dname=StringVar()
        Did=StringVar()

        #=================================Function Definitions======================================================================
        


        #=================================Exit======================================================================================
        def eExit():
            eExit =tkinter.messagebox.askyesno("Covid Card Management System", "Do you want to exit ?")
            if eExit > 0:
                root.destroy()
                return

        #=================================Reset======================================================================================

        def eReset():
            self.txtCovID.delete(0,END)
            self.txtFirstname.delete(0,END)
            self.txtSurname.delete(0,END)    
            self.txtAadharNo.delete(0,END)    
            District.set("")   
            
            self.txtDname.delete(0,END)
            self.txtDid.delete(0,END)
            self.txtDat1.delete(0,END)
            self.txtHosp.delete(0,END)
            self.txtDate1.delete(0,END)
            self.txtCenter1.delete(0,END)
            self.txtDate2.delete(0,END)
            self.txtCenter2.delete(0,END)
            Vacname.set("")
            Stat1 .set("")
            Status1 .set("")            
            Status2 .set("")
            
        #=================================Print======================================================================================
        def ePrint():


            for child in self.covcard_records.get_children():
                print(self.covcard_records.item(child)["values"])

        #=================================Add Data======================================================================================
        def eAddData():
            if CovID.get() =="" or Firstname.get()=="" or Surname.get()=="" :
                tkinter.messagebox.showerror("Enter correct members details")
            else:
                sqlCon =pymysql.connect(host="localhost",user="root",password="XknR231+",database="covidcard")
                cur =sqlCon.cursor()
                cur.execute("insert into patient values(%s,%s,%s,%s,%s)",(

                CovID.get(),
                Firstname.get(),
                Surname.get(),
                AadharNo.get(),
                District.get()))
                sqlCon.commit()
                cur.execute("insert into covid_infection(cov_id,status,date,hospital) values(%s,%s,%s,%s)",(
                CovID.get(),
                Stat1.get(), 
                Dat1.get(), 
                Hosp.get()))
                sqlCon.commit()
                cur.execute("insert into doctor(cov_id,Name,Doc_ID) values(%s,%s,%s)",(
                CovID.get(),
                Dname.get(),
                Did.get()))
                sqlCon.commit()
                cur.execute("insert into covid_vaccine(cov_id,vaccine_name,status1,date1,centre1,status2,date2,centre2) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                CovID.get(),
                Vacname.get(),
                Status1.get(), 
                Date1.get(),
                Center1.get(),
               Status2.get(), 
                Date2.get(),       
                Center2.get() 
                ))
                
                sqlCon.commit()
                eDisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")


        #=================================Display======================================================================================
        def eDisplayData():
            sqlCon =pymysql.connect(host="localhost",user="root",password="XknR231+",database="covidcard")
            cur =sqlCon.cursor()
            cur.execute("select p.cov_id,firstname,surname,aadhar_no,district,i.status,i.date,v.status1,v.status2,i.hospital,v.vaccine_name,\
                        v.centre1,v.date1,v.centre2,v.date2,d.Doc_ID,d.name from patient p,covid_infection i,covid_vaccine v, doctor d \
                        where p.cov_id=i.cov_id AND p.cov_id=v.cov_id AND p.cov_id=d.cov_id")
            result = cur.fetchall()
            if len(result)!= 0:
                self.covcard_records.delete(*self.covcard_records.get_children())
                for row in result:
                        self.covcard_records.insert('',END,values =row)
                sqlCon.commit()
            sqlCon.close()

        #=================================View======================================================================================
        def eTreeInfo(ev):
            viewInfo = self.covcard_records.focus()
            eData = self.covcard_records.item(viewInfo)
            row = eData['values']
            CovID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            AadharNo.set(row[3])
            District.set(row[4])
            Stat1.set(row[5])
            Dat1.set(row[6])
            Vacname.set(row[10])     
            Status1.set(row[7])                   
            Status2.set(row[8])
            Hosp.set(row[9])
            Date1.set(row[12])
            Center1.set(row[11])
            Date2.set(row[14])        
            Center2.set(row[13])
            Dname.set(row[16])
            Did.set(row[15])
        
            

        #=================================Update======================================================================================
        def eUpdate():
            sqlCon =pymysql.connect(host="localhost",user="root",password="XknR231+",database="covidcard")
            cur =sqlCon.cursor()
            cur.execute("update patient p,covid_infection i ,covid_vaccine v ,doctor d set p.firstname=%s,p.surname=%s,p.aadhar_no=%s,p.district=%s,i.status=%s,i.date=%s,\
                        v.status1=%s,v.status2=%s,i.hospital=%s,v.vaccine_name=%s,\
                        v.centre1=%s,v.date1=%s,v.centre2=%s,v.date2=%s,d.Doc_ID=%s,d.name=%s \
                        where p.cov_id=i.cov_id AND p.cov_id=v.cov_id AND p.cov_id=d.cov_id AND p.cov_id=%s",(
           
            Firstname.get(),
            Surname.get(),
            AadharNo.get(),
            District.get(),          
            Stat1.get(),
            Dat1.get(),                        
            Status1.get(),
            Status2.get(),
            Hosp.get(),
            Vacname.get(), 
            Center1.get(),
            Date1.get(),    
            Center2.get(),
            Date2.get(),
            Did.get(),
            Dname.get(),     
            CovID.get()
            
            ))
            

            sqlCon.commit()
            eDisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Updated")

        #=================================Delete======================================================================================
        def eDelete():
            sqlCon =pymysql.connect(host="localhost",user="root",password="XknR231+",database="covidcard")
            cur =sqlCon.cursor()
            cur.execute("delete patient,covid_infection,covid_vaccine ,doctor from patient join covid_infection join covid_vaccine join doctor \
                        on patient.cov_id=covid_infection.cov_id AND patient.cov_id=covid_vaccine.cov_id \
                        AND patient.cov_id=doctor.cov_id where patient.cov_id=%s" ,(
                        CovID.get()))

            sqlCon.commit()
            eDisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")
            eReset()

        #=================================Search======================================================================================
        def eSearch():
            try:
                sqlCon =pymysql.connect(host="localhost",user="root",password="XknR231+",database="covidcard")
                cur =sqlCon.cursor()
                cur.execute("select p.cov_id,firstname,surname,aadhar_no,district,i.status,i.date,v.status1,v.status2,i.hospital,v.vaccine_name,\
                        v.centre1,v.date1,v.centre2,v.date2,d.Doc_ID,d.name from patient p,covid_infection i,covid_vaccine v, doctor d \
                        where p.cov_id=i.cov_id AND p.cov_id=v.cov_id AND p.cov_id=d.cov_id AND p.cov_id=%s",(
                            CovID.get()))                
                        
                row = cur.fetchone()

                CovID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                AadharNo.set(row[3])
                District.set(row[4])
                Stat1.set(row[5])
                Dat1.set(row[6])
                Vacname.set(row[10])     
                Status1.set(row[7])                   
                Status2.set(row[8])
                Hosp.set(row[9])
                Date1.set(row[12])
                Center1.set(row[11])
                Date2.set(row[14])        
                Center2.set(row[13])
                Dname.set(row[16])
                Did.set(row[15])              
                     
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                eReset()
            sqlCon.close()


        
        #=========================================Title============================================================
        self.lblTitle = Label(TitleFrame, font=('Bernard',59, 'bold'),text="Covid Card Management System",fg='black')                                  
        self.lblTitle.grid(row=0,column=0,  padx=132)

        
        lblTitleInf = Label(LeftFrame2Left, font=('Bernard',13, 'bold'),text="Dose-1",fg='black')                                  
        lblTitleInf.grid(row=0,column=0)

        lblTitleInf = Label(LeftFrame2Right, font=('Bernard',13, 'bold'),text="Dose-2",fg='black')                                  
        lblTitleInf.grid(row=0,column=0)
        
        
        lblTitleInf = Label(LeftFrame3Left, font=('Bernard',15, 'bold'),text="Infection Details",fg='black')                                  
        lblTitleInf.grid(row=0,column=0)

        lblTitleInf = Label(LeftFrame3Right, font=('Bernard',15, 'bold'),text="Doctor Details",fg='black')                                  
        lblTitleInf.grid(row=0,column=0,pady=16)

        lblTitleInf = Label(RightFrame0, font=('Bernard',18, 'bold'),text="Tree View",fg='black')                                  
        lblTitleInf.grid(row=0,column=0)
        #===================================================Buttons================================================
        self.lblCovID = Label(LeftFrame1, font=('arial',12, 'bold'),text="Cov ID",bd=7)
        self.lblCovID.grid(row=0,column=0, sticky =W, padx=20)
        self.txtCovID = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=38,justify = 'left',textvariable=CovID)
        self.txtCovID.grid(row=0,column=1)

        self.lblFirstname = Label(LeftFrame1, font=('arial',12, 'bold'),text="Firstname", bd=7)
        self.lblFirstname.grid(row=1,column=0, sticky =W, padx=20)
        self.txtFirstname = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=38,justify = 'left',textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial',12, 'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=2,column=0, sticky =W, padx=20)
        self.txtSurname = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=38,justify = 'left',textvariable=Surname)
        self.txtSurname.grid(row=2,column=1)
      
        self.lblAadharNo = Label(LeftFrame1, font=('arial',12, 'bold'),text="Aadhar No", bd=7)
        self.lblAadharNo.grid(row=3,column=0, sticky =W, padx=20)
        self.txtAadharNo = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=38,justify = 'left', textvariable=AadharNo)
        self.txtAadharNo.grid(row=3,column=1)


        
        self.lblDistrict = Label(LeftFrame1, font=('arial',12, 'bold'),text="District ", bd=5)
        self.lblDistrict.grid(row=4,column=0, sticky =W, padx=20)
       
        self.cboDistrict=ttk.Combobox(LeftFrame1, width=37 , font=('arial',12,'bold'),state='readonly',textvariable=District)
        self.cboDistrict['values'] =(' ','Thiruvananthapuram', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode', 'Wayanadu','Kannur','Kasaragod')
        self.cboDistrict.current(0)
        self.cboDistrict.grid(row=4,column=1)


        #======================================================Infection Details============================================
        self.lblStatus1 = Label(LeftFrame3Left, font=('arial',12, 'bold'),text="Status", bd=7, anchor='w', justify=LEFT)
        self.lblStatus1.grid(row=1,column=0, sticky =W)

        self.cboStatus1 = ttk.Combobox(LeftFrame3Left,width=19, font=('arial', 12,'bold'),state='readonly',textvariable=Stat1)                                                                                  
        self.cboStatus1['values'] = ('','Infected', 'Not Infected')
        self.cboStatus1.current(0)
        self.cboStatus1.grid(row=1, column=1)
        
        self.lblDat1 = Label(LeftFrame3Left, font=('arial',12, 'bold'),text="Date", bd=7, anchor='e')
        self.lblDat1.grid(row=2,column=0, sticky =W)
        self.txtDat1 = Entry(LeftFrame3Left,font=('arial', 12,'bold'), bd=5, width=20,justify = 'left', textvariable=Dat1)                                                                                  
        self.txtDat1.grid(row=2, column=1)

        self.lblHosp = Label(LeftFrame3Left, font=('arial',12, 'bold'),text="Hospital", bd=7, anchor='e')
        self.lblHosp.grid(row=3,column=0, sticky =W)
        self.txtHosp = Entry(LeftFrame3Left,font=('arial', 12,'bold'), bd=5, width=20,justify = 'left', textvariable=Hosp)                                                                                  
        self.txtHosp.grid(row=3, column=1)

        #======================================================Doctor Details============================================
        self.lblDname = Label(LeftFrame3Right, font=('arial',12, 'bold'),text="Name", bd=7, anchor='e')
        self.lblDname.grid(row=1,column=0, sticky =W)
        self.txtDname = Entry(LeftFrame3Right,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Dname)                                                                                  
        self.txtDname.grid(row=1, column=1)

        self.lblDid = Label(LeftFrame3Right, font=('arial',12, 'bold'),text="Doc-ID", bd=7, anchor='e')
        self.lblDid.grid(row=2,column=0, sticky =W)
        self.txtDid = Entry(LeftFrame3Right,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Did)                                                                                  
        self.txtDid.grid(row=2, column=1)
    
        
        
        #======================================================Vaccination Details============================================
        self.lblVacname = Label(LeftFrame4, font=('arial',15, 'bold'),text="Vaccine", bd=7, anchor='w', justify=LEFT,fg='black')
        self.lblVacname.grid(row=0,column=1, sticky =W)

        self.cboVacname = ttk.Combobox(LeftFrame4,width=13, font=('arial', 12,'bold'),state='readonly',textvariable=Vacname)                                                                                  
        self.cboVacname['values'] = ('','Covishield', 'Covaxine', 'Pfizer', 'Sputnik', 'Johnson & Johnson', 'Sinopharm', 'Sputnik')
        self.cboVacname.current(0)
        self.cboVacname.grid(row=0, column=2)
        
        self.lblStatus1 = Label(LeftFrame2Left, font=('arial',12, 'bold'),text="Status", bd=7, anchor='w', justify=LEFT)
        self.lblStatus1.grid(row=1,column=0, sticky =W)

        self.cboStatus1 = ttk.Combobox(LeftFrame2Left,width=13, font=('arial', 12,'bold'),state='readonly',textvariable=Status1)                                                                                  
        self.cboStatus1['values'] = ('','Vaccinated', 'Not Vaccinated')
        self.cboStatus1.current(0)
        self.cboStatus1.grid(row=1, column=1)
        
        self.lblDate1 = Label(LeftFrame2Left, font=('arial',12, 'bold'),text="Date", bd=7, anchor='e')
        self.lblDate1.grid(row=2,column=0, sticky =W)
        self.txtDate1 = Entry(LeftFrame2Left,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Date1)                                                                                  
        self.txtDate1.grid(row=2, column=1)

        self.lblCenter1 = Label(LeftFrame2Left, font=('arial',12, 'bold'),text="Center", bd=7, anchor='e')
        self.lblCenter1.grid(row=3,column=0, sticky =W)
        self.txtCenter1 = Entry(LeftFrame2Left,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Center1)                                                                                  
        self.txtCenter1.grid(row=3, column=1)





        
        self.lblStatus2 = Label(LeftFrame2Right, font=('arial',12, 'bold'),text="Status", bd=7, anchor='w', justify=LEFT)
        self.lblStatus2.grid(row=1,column=0, sticky =W)

        self.cboStatus2 = ttk.Combobox(LeftFrame2Right,width=13, font=('arial', 12,'bold'),state='readonly',textvariable=Status2)                                                                                  
        self.cboStatus2['values'] = ('','Vaccinated', 'Not Vaccinated')
        self.cboStatus2.current(0)
        self.cboStatus2.grid(row=1, column=1)
        
        self.lblDate2 = Label(LeftFrame2Right, font=('arial',12, 'bold'),text="Date", bd=7, anchor='e')
        self.lblDate2.grid(row=2,column=0, sticky =W)
        self.txtDate2 = Entry(LeftFrame2Right,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Date2)                                                                                  
        self.txtDate2.grid(row=2, column=1)

        self.lblCenter2 = Label(LeftFrame2Right, font=('arial',12, 'bold'),text="Center", bd=7, anchor='e')
        self.lblCenter2.grid(row=3,column=0, sticky =W)
        self.txtCenter2 = Entry(LeftFrame2Right,font=('arial', 16,'bold'), bd=5, width=11,justify = 'left', textvariable=Center2)                                                                                  
        self.txtCenter2.grid(row=3, column=1)
        #=====================================================Tree View==============================================

        scroll_x=Scrollbar(RightFrame1a,orient=HORIZONTAL)
        scroll_y=Scrollbar(RightFrame1a,orient=VERTICAL)

        self.covcard_records=ttk.Treeview(RightFrame1a,height=24,columns=("CovID","Firstname","Surname","AadharNo",
        "District","Stat1","Dat1","Status1","Status2"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.covcard_records.heading("CovID",text="Cov ID")
        self.covcard_records.heading("Firstname",text="Firstname")
        self.covcard_records.heading("Surname",text="Surname")
        self.covcard_records.heading("AadharNo",text="Aadhar No")
        self.covcard_records.heading("District",text="District")
        self.covcard_records.heading("Stat1",text="Inf-Status")
        self.covcard_records.heading("Dat1",text="Date of Inf")
        self.covcard_records.heading("Status1",text="Dose-1")
        self.covcard_records.heading("Status2",text="Dose-2")
                                                                          

        self.covcard_records['show']='headings'
        
        self.covcard_records.column("CovID", width=70)
        self.covcard_records.column("Firstname",width=100)
        self.covcard_records.column("Surname",width=100)
        self.covcard_records.column("AadharNo",width=100)
        self.covcard_records.column("District",width=70)
        self.covcard_records.column("Stat1",width=70)
        self.covcard_records.column("Dat1",width=70)
        self.covcard_records.column("Status1",width=70)
        self.covcard_records.column("Status2",width=70)

        self.covcard_records.pack(fill=BOTH,expand=1)
        self.covcard_records.bind("<ButtonRelease-1>",eTreeInfo)
        eDisplayData()
       #===================================================Functions================================================
        self.btnAddNew=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eAddData,
                            width=8,text="Add New Data").grid(row=0, column=0,padx=1)

        self.btnPrint=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=ePrint,
                            width=8,text="Print").grid(row=0, column=1,padx=1)
       
        self.btnDisplay=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eDisplayData,
                            width=8,text="Display").grid(row=0, column=2,padx=1)

        self.btnUpdate=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eUpdate,
                            width=8,text="Update").grid(row=0, column=3,padx=1)

        self.btnDelete=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eDelete,
                    width=8, text="Delete").grid(row=0, column=4,padx=1)


        self.btnSearch=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eSearch,
                            width=8,text="Search").grid(row=0, column=5,padx=1)

        self.btnReset=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eReset,
                            width=8,text="Reset").grid(row=0, column=6,padx=2)

        self.btnExit=Button(TopFrame1,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=eExit,
                    width=8, text='Exit').grid(row=0, column=7, padx=1)


        


        
if __name__=='__main__':
    root = Tk()
    application = Covcard(root)
    root.mainloop()
