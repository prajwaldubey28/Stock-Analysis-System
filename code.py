import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
ro = Tk()
ro.geometry("450x620")
ro.configure(bg='black')

# my_img=ImageTk.PhotoImage(Image.open('abc.png'))
# label_my_img=Label(ro,width=9000,height=400,image=my_img,justify='left',bg='black')
# label_my_img.pack()

ro.title("Welcome")
Top = Frame(ro, width=1600, height=50, relief=SUNKEN, bg="black")
Top.pack(side=TOP)
f3 = Frame(ro, width=900, height=700, relief=SUNKEN, pady=90, bg='black')
f3.pack()

lblinf = Label(Top, font=('aria', 35, 'bold'), text="STOCK MARKET", fg="green", bg='black', bd=10, anchor='w', pady=4)
lblinf.grid(row=0, column=0)

def branch():
    r = Tk()
    r.geometry('1200x400')
    r.title("LIST OF COMPANIES SECTORWISE")
    r.configure(bg='black')
    lbl1 = Label(r, font=('aria', 15, 'bold'), text="FINANCIALSECTOR", fg="white", bg='black', bd=5)
    lbl1.grid(row=0, column=0)
    lbl2 = Label(r, font=('aria', 15, 'bold'), text=" 	", fg="black", bg='black', anchor=W)
    lbl2.grid(row=0, column=2)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="AUTOMOBILESECTOR", fg='white', bg='black', anchor=W)
    lbl3.grid(row=0, column=3)
    lbl4 = Label(r, font=('aria', 15, 'bold'), text="AXISBANK", fg="green", bg='black', anchor=W)
    lbl4.grid(row=1, column=0)
    lbl5 = Label(r, font=('aria', 15, 'bold'), text="EICHERMOTORS", fg="green", bg='black', anchor=W)
    lbl5.grid(row=1, column=3)
    lbl6 = Label(r, font=('aria', 15, 'bold'), text="HDFCBANK", fg="green", bg='black', anchor=W)
    lbl6.grid(row=2, column=0)
    lbl7 = Label(r, font=('aria', 15, 'bold'), text="MARUTISUZUKI", fg="green", bg='black', anchor=W)
    lbl7.grid(row=2, column=3)
    lbl8 = Label(r, font=('aria', 15, 'bold'), text="INDUSINDBANK", fg="green", bg='black', anchor=W)
    lbl8.grid(row=3, column=0)
    lbl9 = Label(r, font=('aria', 15, 'bold'), text="HEROMOTOCOP", fg="green", bg='black', anchor=W)
    lbl9.grid(row=3, column=3)
    lbl10 = Label(r, font=('aria', 15, 'bold'), text="ICICIBANK", fg="green", bg='black', anchor=W)
    lbl10.grid(row=4, column=0)
    lbl11 = Label(r, font=('aria', 15, 'bold'), text="TATAMOTORS", fg="green", bg='black', anchor=W) 

    lbl11.grid(row=4, column=3)
    lbl12 = Label(r, font=('aria', 15, 'bold'), text="KOTAKBANK", fg="green", bg='black', anchor=W)
    lbl12.grid(row=5, column=0)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="JSWSTEEL", fg="green", bg='black', anchor=W)
    lbl3.grid(row=5, column=3)
    lbl4 = Label(r, font=('aria', 15, 'bold'), text="BAJAJFINANCE", fg="green", bg='black', anchor=W)
    lbl4.grid(row=6, column=0)
    lbl5 = Label(r, font=('aria', 15, 'bold'), text="MAHINDRAANDMAHINDRA", fg="green", bg='black', anchor=W)
    lbl5.grid(row=6, column=3)
    lbl6 = Label(r, font=('aria', 15, 'bold'), text="BAJAJFINSERV", fg="green", bg='black', anchor=W)
    lbl6.grid(row=7, column=0)
    lbl7 = Label(r, font=('aria', 15, 'bold'), text="HDFC LTD", fg="green", bg='black', anchor=W)
    lbl7.grid(row=8, column=0)
    lbl8 = Label(r, font=('aria', 15, 'bold'), text="HDFC BANK", fg="green", bg='black', anchor=W)
    lbl8.grid(row=9, column=0)
    lbl9 = Label(r, font=('aria', 15, 'bold'), text="STATE BANK OF INDIA", fg="green", bg='black', anchor=W)
    lbl9.grid(row=10, column=0)

#ENERGY AND TECH COMPANIES
    lbl2 = Label(r, font=('aria', 15, 'bold'), text=" 	", fg="black", bg='black', anchor=W)
    lbl2.grid(row=0, column=5)

    lbl1 = Label(r, font=('aria', 15, 'bold'), text="TECH COMPANIES", fg="white", bg='black', bd=5)
    lbl1.grid(row=0, column=6)
    lbl2 = Label(r, font=('aria', 15, 'bold'), text=" 	", fg="black", bg='black', anchor=W)
    lbl2.grid(row=15, column=2)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="ENERGY SECTOR", fg='white', bg='black', anchor=W)
    lbl3.grid(row=0, column=9)
    lbl4 = Label(r, font=('aria', 15, 'bold'), text="HCL TECH", fg="green", bg='black', anchor=W)
    lbl4.grid(row=1, column=6)
    lbl5 = Label(r, font=('aria', 15, 'bold'), text="ONGC", fg="green", bg='black', anchor=W)
    lbl5.grid(row=1, column=9)
    lbl6 = Label(r, font=('aria', 15, 'bold'), text="TECH MAHINDRA", fg="green", bg='black', anchor=W)
    lbl6.grid(row=2, column=6)
    lbl7 = Label(r, font=('aria', 15, 'bold'), text="BPCL", fg="green", bg='black', anchor=W)
    lbl7.grid(row=2, column=9)
    lbl8 = Label(r, font=('aria', 15, 'bold'), text="TCS", fg="green", bg='black', anchor=W)
    lbl8.grid(row=3, column=6)
    lbl9 = Label(r, font=('aria', 15, 'bold'), text="GAIL", fg="green", bg='black', anchor=W)
    lbl9.grid(row=3, column=9)
    lbl10 = Label(r, font=('aria', 15, 'bold'), text="INFOSYS", fg="green", bg='black', anchor=W)
    lbl10.grid(row=4, column=6)
    lbl11 = Label(r, font=('aria', 15, 'bold'), text="IOC", fg="green", bg='black', anchor=W)
    lbl11.grid(row=4, column=9)
    lbl12 = Label(r, font=('aria', 15, 'bold'), text="WIPRO", fg="green", bg='black', anchor=W)
    lbl12.grid(row=5, column=6)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="NTPC", fg="green", bg='black', anchor=W)
    lbl3.grid(row=5, column=9)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="ONGC", fg="green", bg='black', anchor=W)
    lbl3.grid(row=6, column=9)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="POWERGRID CORP", fg="green", bg='black', anchor=W)
    lbl3.grid(row=7, column=9)
    lbl3 = Label(r, font=('aria', 15, 'bold'), text="RELIANCE INDUSTRIES", fg="green", bg='black', anchor=W)
    lbl3.grid(row=8, column=9)

    r.mainloop()
    


	
def about():
    p = Tk()
    p.geometry("900x200")
    p.title("ABOUT THE PROJECT")
    p.configure(bg='black')

    lbla = Label(p, font=('aria', 15, 'bold'),text="In this project we have done an analysis of Nifty50 Stock Market using Seaborn.\n.In this project an investor can get an idea of the variation of the stock prices with each year\n1.The graphs show us the volatality of the share during a period. ",fg="red", bg='black', bd=5)
    lbla.grid(row=0, column=0)
    p.mainloop()

def main():


    root = Tk()
    root.geometry("1520x750")
    root.configure(bg='black')
    root.title("NSE NIFTY50 STOCK ANALYSIS")
    Top = Frame(root, width=100, height=50, relief=SUNKEN, bg="black")
    Top.pack(side=TOP)
    f1 = Frame(root, width=600, height=700, relief=SUNKEN, pady=90, bg='black')
    f1.pack()
    def techcompanies():
        techcompany=['HCLTECH.NS.csv','INFY.NS.csv','TCS.NS.csv','TECHM.NS.csv','WIPRO.NS.csv']
        df1 = pd.read_csv('HCLTECH.NS.csv')
    
        df1['Date'] = pd.to_datetime(df1['Date'])
        df1['Years'] = df1['Date'].apply(lambda time: time.year)
        df2 = pd.read_csv('INFY.NS.csv')
        df2['Date'] = pd.to_datetime(df2['Date'])
        df2['Years'] = df2['Date'].apply(lambda time: time.year)
        df3 = pd.read_csv('TCS.NS.csv')
        df3['Date'] = pd.to_datetime(df3['Date'])
        df3['Years'] = df3['Date'].apply(lambda time: time.year)
        df4 = pd.read_csv('TECHM.NS.csv')
        df4['Date'] = pd.to_datetime(df4['Date'])
        df4['Years'] = df4['Date'].apply(lambda time: time.year)
        df5 = pd.read_csv('WIPRO.NS.csv')
        df5['Date'] = pd.to_datetime(df5['Date'])
        df5['Years'] = df5['Date'].apply(lambda time: time.year)
        frames = [df1,df2,df3,df4,df5]
        df = pd.concat(frames,axis=1,keys = techcompany)
    #df=pd.concat(map(pd.read_csv,['HCLTECH.NS.csv','INFY.NS.csv','TCS.NS.csv','TECHM.NS.csv','WIPRO.NS.csv']),axis=1,keys=techcompany)
    
        for comp in techcompany:
    	    x = df[comp]['Years']
    	    y = df[comp]['Close'] 
    	    sns.lineplot(x,y)
        #df[comp]['Close'].plot(figsize=(40, 30), label=comp)
    #plt.xlabel('Years')
    #plt.ylabel('Price')
    #plt.title('Stock Market Analysis')
    #plt.xlim(2015,2020)
    #plt.ylim(500,1000)
        plt.legend(techcompany)
        plt.show()

    def automobilecompanies():
  
        automobilecompanies=['EICHERMOT.NS.csv','HEROMOTOCO.NS.csv','MARUTI.NS.csv','TATAMOTORS.NS.csv','JSWSTEEL.NS.csv','M&M.NS.csv']

        df1 = pd.read_csv('EICHERMOT.NS.csv')
        df1['Date'] = pd.to_datetime(df1['Date'])
        df1['Years'] = df1['Date'].apply(lambda time: time.year)
        df2 = pd.read_csv('HEROMOTOCO.NS.csv')
        df2['Date'] = pd.to_datetime(df2['Date'])
        df2['Years'] = df2['Date'].apply(lambda time: time.year)
        df3 = pd.read_csv('MARUTI.NS.csv')
        df3['Date'] = pd.to_datetime(df3['Date'])
        df3['Years'] = df3['Date'].apply(lambda time: time.year)                  
        df4 = pd.read_csv('TATAMOTORS.NS.csv')
        df4['Date'] = pd.to_datetime(df4['Date'])
        df4['Years'] = df4['Date'].apply(lambda time: time.year)
        df5 = pd.read_csv('JSWSTEEL.NS.csv')
        df5['Date'] = pd.to_datetime(df5['Date'])
        df5['Years'] = df5['Date'].apply(lambda time: time.year)
        df6 = pd.read_csv('M&M.NS.csv')
        df6['Date'] = pd.to_datetime(df6['Date'])
        df6['Years'] = df6['Date'].apply(lambda time: time.year)
        frames = [df1,df2,df3,df4,df5,df6]
        df = pd.concat(frames,axis=1,keys = automobilecompanies)
    #df=pd.concat(map(pd.read_csv,['HCLTECH.NS.csv','INFY.NS.csv','TCS.NS.csv','TECHM.NS.csv','WIPRO.NS.csv']),axis=1,keys=techcompany)
    
        for comp in automobilecompanies:
    	    x = df[comp]['Years']
    	    y = df[comp]['Close'] 
    	    sns.lineplot(x,y)
        #df[comp]['Close'].plot(figsize=(40, 30), label=comp)
    #plt.xlabel('Years')
    #plt.ylabel('Price')
    #plt.title('Stock Market Analysis')
    #plt.xlim(2015,2020)
    #plt.ylim(500,1000)
        plt.legend(automobilecompanies)
        plt.show()

    def privatesectorcompanies():
        privatesectorcompanies=['AXISBANK.NS.csv','HDFCBANK.NS.csv','ICICIBANK.NS.csv','KOTAKBANK.NS.csv','INDUSINDBK.NS.csv','BAJAJFINSV.NS.csv','BAJFINANCE.NS.csv','HDFC.NS.csv','SBIN.NS.csv']
        df1 = pd.read_csv('AXISBANK.NS.csv')
    
        df1['Date'] = pd.to_datetime(df1['Date'])
        df1['Years'] = df1['Date'].apply(lambda time: time.year)
        df2 = pd.read_csv('HDFCBANK.NS.csv')
        df2['Date'] = pd.to_datetime(df2['Date'])
        df2['Years'] = df2['Date'].apply(lambda time: time.year)
        df3 = pd.read_csv('ICICIBANK.NS.csv')
        df3['Date'] = pd.to_datetime(df3['Date'])
        df3['Years'] = df3['Date'].apply(lambda time: time.year)
        df4 = pd.read_csv('KOTAKBANK.NS.csv')
        df4['Date'] = pd.to_datetime(df4['Date'])
        df4['Years'] = df4['Date'].apply(lambda time: time.year)
        df5 = pd.read_csv('INDUSINDBK.NS.csv')
        df5['Date'] = pd.to_datetime(df5['Date'])
        df5['Years'] = df5['Date'].apply(lambda time: time.year)
        df6 = pd.read_csv('BAJAJFINSV.NS.csv')
        df6['Date'] = pd.to_datetime(df6['Date'])
        df6['Years'] = df6['Date'].apply(lambda time: time.year)
        df7 = pd.read_csv('BAJFINANCE.NS.csv')
        df7['Date'] = pd.to_datetime(df7['Date'])
        df7['Years'] = df7['Date'].apply(lambda time: time.year)
        df8 = pd.read_csv('HDFC.NS.csv')
        df8['Date'] = pd.to_datetime(df8['Date'])
        df8['Years'] = df8['Date'].apply(lambda time: time.year)
        df9 = pd.read_csv('SBIN.NS.csv')
        df9['Date'] = pd.to_datetime(df9['Date'])
        df9['Years'] = df9['Date'].apply(lambda time: time.year)
        frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9]
        df = pd.concat(frames,axis=1,keys = privatesectorcompanies)
    #df=pd.concat(map(pd.read_csv,['HCLTECH.NS.csv','INFY.NS.csv','TCS.NS.csv','TECHM.NS.csv','WIPRO.NS.csv']),axis=1,keys=techcompany)
    
        for comp in privatesectorcompanies:
    	    x = df[comp]['Years']
    	    y = df[comp]['Close'] 
    	    sns.lineplot(x,y)
        #df[comp]['Close'].plot(figsize=(40, 30), label=comp)
    #plt.xlabel('Years')
    #plt.ylabel('Price')
    #plt.title('Stock Market Analysis')
    #plt.xlim(2015,2020)
    #plt.ylim(500,1000)
        plt.legend(privatesectorcompanies)
        plt.show()

    def energysectorcompanies():
        energysectorcompanies=['BPCL.NS.csv','GAIL.NS.csv','IOC.NS.csv','NTPC.NS.csv','ONGC.NS.csv','POWERGRID.NS.csv','RELIANCE.NS.csv']
        df1 = pd.read_csv('BPCL.NS.csv')
    
        df1['Date'] = pd.to_datetime(df1['Date'])
        df1['Years'] = df1['Date'].apply(lambda time: time.year)
        df2 = pd.read_csv('GAIL.NS.csv')
        df2['Date'] = pd.to_datetime(df2['Date'])
        df2['Years'] = df2['Date'].apply(lambda time: time.year)
        df3 = pd.read_csv('IOC.NS.csv')
        df3['Date'] = pd.to_datetime(df3['Date'])
        df3['Years'] = df3['Date'].apply(lambda time: time.year)
        df4 = pd.read_csv('NTPC.NS.csv')
        df4['Date'] = pd.to_datetime(df4['Date'])
        df4['Years'] = df4['Date'].apply(lambda time: time.year)
        df5 = pd.read_csv('ONGC.NS.csv')
        df5['Date'] = pd.to_datetime(df5['Date'])
        df5['Years'] = df5['Date'].apply(lambda time: time.year)
        df6 = pd.read_csv('POWERGRID.NS.csv')
        df6['Date'] = pd.to_datetime(df6['Date'])
        df6['Years'] = df6['Date'].apply(lambda time: time.year)
        df7 = pd.read_csv('RELIANCE.NS.csv')
        df7['Date'] = pd.to_datetime(df7['Date'])
        df7['Years'] = df7['Date'].apply(lambda time: time.year)
        frames = [df1,df2,df3,df4,df5,df6,df7]
        df = pd.concat(frames,axis=1,keys = energysectorcompanies)
    #df=pd.concat(map(pd.read_csv,['HCLTECH.NS.csv','INFY.NS.csv','TCS.NS.csv','TECHM.NS.csv','WIPRO.NS.csv']),axis=1,keys=techcompany)
    
        for comp in energysectorcompanies:
    	    x = df[comp]['Years']
    	    y = df[comp]['Close'] 
    	    sns.lineplot(x,y)
        #df[comp]['Close'].plot(figsize=(40, 30), label=comp)
    #plt.xlabel('Years')
    #plt.ylabel('Price')
    #plt.title('Stock Market Analysis')
    #plt.xlim(2015,2020)
    #plt.ylim(500,1000)
        plt.legend(energysectorcompanies)
        plt.show()

    label = Label(Top, font=('aria', 35, 'bold'), text="NSE NIFTY50 STOCK MARKET ANALYSIS", fg="green", bg='black', bd=10, anchor='w', pady=4)
    label.grid(row=0, column=0)
#BUTTONS

    btn1=Button(f1,padx=70,pady=8, bd=10 ,fg="green",font=('ariel',14,'bold'),width=20, text="AUTOMOBILE COMPANIES",bg="black", command=automobilecompanies)
    btn1.grid(row=1, column=4,columnspan=2,padx=200, pady =50)

    btn2=Button(f1,padx=70,pady=8, bd=10 ,fg="green",font=('ariel',14,'bold'),width=20, text="FINANCIAL SERVICES",bg='black', command=privatesectorcompanies)
    btn2.grid(row=1, column=2,columnspan=2,padx=200, pady =50)

    btn3=Button(f1,padx=70,pady=8, bd=10 ,fg="green",font=('ariel',14,'bold'),width=20, text="TECH COMPANIES",bg='black', command=techcompanies)
    btn3.grid(row=3, column=2,columnspan=2,padx=200, pady = 50)

    btn4=Button(f1,padx=70,pady=8, bd=10 ,fg="green",font=('ariel',14,'bold'),width=20, text="ENERGY SECTOR",bg='black', command=energysectorcompanies)
    btn4.grid(row=3, column=4,columnspan=2,padx=200, pady = 50)
     
    def exit():

        messagebox.showinfo("Message","Thank You")
        root.destroy()
        ro.destroy()
        r.destroy()

    btn5=Button(f1,padx=70,pady=8, bd=10 ,fg="green",font=('ariel',14,'bold'),width=8, text="EXIT",bg='black',command=exit)
    btn5.grid(row=4, column=3,columnspan=2,padx=100, pady =10)


#FUNCTIONS



    root.mainloop()

btn2=Button(f3,padx=20,pady=8, bd=10 ,fg="green",font=('ariel' ,16,'bold'),width=15, text="STOCK ANALYSIS",bg="black",command=main)
btn2.grid(row=2, column=3,columnspan=2, pady =20)

btn3=Button(f3,padx=20,pady=8, bd=10 ,fg="green",font=('ariel' ,16,'bold'),width=15, text="LIST OF COMPANIES",bg='black',command=branch)
btn3.grid(row=3, column=3,columnspan=2, pady =20)

btn4=Button(f3,padx=20,pady=8, bd=10 ,fg="green",font=('ariel' ,16,'bold'),width=15, text="About",bg='black',command=about)
btn4.grid(row=4, column=3,columnspan=2, pady = 20)

def exits():
    messagebox.showinfo("Message","Thank You")
    ro.destroy()
btn5=Button(f3,padx=20,pady=8, bd=10 ,fg="green",font=('ariel' ,16,'bold'),width=15, text="Exit",bg='black',command=exits)
btn5.grid(row=5, column=3,columnspan=2, pady = 20)
ro.mainloop()
