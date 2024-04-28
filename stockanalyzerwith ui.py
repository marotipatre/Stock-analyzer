from tkinter import *
import matplotlib.pyplot as plt
import yfinance as yf

# var1 = "1990-01-01"
# var2 = "2021-01-01"

window=Tk()

window.title('stock analyzer')

def plotgraph():
  if(int(var3.get()) == 1): 
     ticker = str(var4.get())
     
     data = yf.download(ticker, var1.get(), var2.get())['Adj Close']
     t5=Text(window,height=1,width=20)
     t5.grid(row=10,column=2)
     t5.delete("1.0",END)
     t5.insert(END,'Adj Close Price')
    
     t6=Text(window,height=var6.get()+2,width=25)
     t6.grid(row=11,column=2)
     t6.delete("8.0",END)
     t6.insert(END,data.tail(var6.get()))
     
     data.plot(figsize=(10, 7))
     plt.legend(loc="upper left")
     plt.title(var4.get(), fontsize=16)

     plt.ylabel('Price', fontsize=14)
     plt.xlabel('Year', fontsize=14)
     plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
     plt.show()

    

    
  if(int(var3.get()) == 2):
      ticker = str(var4.get())
      
      data = yf.download(ticker, var1.get(), var2.get())['Adj Close']
      
      t5=Text(window,height=1,width=20)
      t5.grid(row=10,column=2)
      t5.delete("1.0",END)
      t5.insert(END,'Adj Close Price')
    
      t6=Text(window,height=var6.get()+2,width=25)
      t6.grid(row=11,column=2)
      t6.delete("8.0",END)
      t6.insert(END,data.tail(var6.get()))
      data.plot(figsize=(10, 7))
      plt.legend(loc="upper left")
      plt.title(var4.get(), fontsize=16)

      plt.ylabel('Price', fontsize=14)
      plt.xlabel('Year', fontsize=14)
      plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
      plt.show()
      
      ticker2 =str(var5.get())
      data1 = yf.download(ticker2, var1.get(), var2.get())['Adj Close']
      t7=Text(window,height=1,width=20)
      t7.grid(row=12,column=2)
      t7.delete("1.0",END)
      t7.insert(END,'Adj Close Price')
      t8=Text(window,height=var6.get()+2,width=25)
      t8.grid(row=13,column=2)
      t8.delete("8.0",END)
      t8.insert(END,data1.tail(var6.get()))
      data1.plot(figsize=(10, 7))
      plt.legend(loc="upper left")
      plt.title(var5.get(), fontsize=16)

      plt.ylabel('Price', fontsize=14)
      plt.xlabel('Year', fontsize=14)
      plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
      plt.show()

 


def printstockdata() :

  
 
  #tickers_list = []


 
  # for i in range(0, int(var3.get())):
 if(int(var3.get()) == 1): 
     ticker = str(var4.get())
     data = yf.download(ticker, var1.get(), var2.get())
     t1=Text(window,height=1,width=20)
     t1.grid(row=10,column=1)
     t1.delete("1.0",END)
     t1.insert(END,ticker)
    
     t2=Text(window,height=var6.get()+2,width=85)
     t2.grid(row=11,column=1)
     t2.delete("8.0",END)
     t2.insert(END,data.tail(var6.get()))
     
     #tickers_list.append(ticker)

     #for ticker in tickers_list:
    

    
 if(int(var3.get()) == 2):
      ticker = str(var4.get())
      data = yf.download(ticker, var1.get(), var2.get())
      t1=Text(window,height=1,width=20)
      t1.grid(row=10,column=1)
      t1.delete("1.0",END)
      t1.insert(END,ticker)
    
      t2=Text(window,height=var6.get()+2,width=85)
      t2.grid(row=11,column=1)
      t2.delete("8.0",END)
      t2.insert(END,data.tail(var6.get()))
      
      ticker2 =str(var5.get())
      data1 = yf.download(ticker2, var1.get(), var2.get())
      t3=Text(window,height=1,width=20)
      t3.grid(row=12,column=1)
      t3.delete("1.0",END)
      t3.insert(END,ticker2)
      t4=Text(window,height=var6.get()+2,width=85)
      t4.grid(row=13,column=1)
      t4.delete("8.0",END)
      t4.insert(END,data1.tail(var6.get()))


    
    
    


#  data = pd.DataFrame(columns=tickers_list)

menu=StringVar()
menu.set("Tickers of some comapnies")
drop=OptionMenu(window,menu,"Apple-AAPL","Microsoft-MSFT","Google-GOOG","Amazon-AMZN","Tesla-TSLA","Walmart-WMT")
drop.grid(row=4,column=2)
l1=Label(window,text="Enter start date : ")
l2=Label(window,text="Enter end date : ")
l3=Label(window,text="Enter number of companies : ")
l5=Label(window,text="Enter company ticker name : ")
l6=Label(window,text="(max 2)")
l4=Label(window, text="Enter number of days: ")

var1=StringVar()
var2=StringVar()
var3=IntVar()
var6=IntVar()
var4=StringVar()
var5=StringVar()


e1=Entry(window,textvariable=var1)
e2=Entry(window,textvariable=var2)
e3=Entry(window,textvariable=var3)
e4=Entry(window,textvariable=var4)
e5=Entry(window,textvariable=var5)
e6=Entry(window,textvariable=var6)
b1=Button(window,text="submit",command=printstockdata)
b2=Button(window,text="Plot a graph",command=plotgraph)



 
 

l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)
l5.grid(row=5,column=0)
l6.grid(row=5,column=3)
l4.grid(row=4,column=0)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=5,column=1)
e5.grid(row=5,column=2)
e6.grid(row=4,column=1)
 
b1.grid(row=8,column=1)
b2.grid(row=8,column=2)
# t2=Text(window,height=8,width=85)
# t2.grid(row=11,column=1)

window.mainloop()


