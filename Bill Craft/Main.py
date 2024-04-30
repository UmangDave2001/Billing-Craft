from tkinter import *   # Imports everything from tkinter
from tkinter import ttk
import tempfile
import random ,os
from tkinter import messagebox
#import sqlite3 

# # DATABASE
# #==========create or connect to database
# connect = sqlite3.connect('customer_data.db')

# # create cursor
# cursor = connect.cursor()

# # create table
# cursor.execute(""" CREATE TABLE Customers (
#                first_name text,
#                Lasr_name text, 
#                phone_numbers integer, 
#                customer_email text, 
#                customer_selected_product  text)
#                """)




# #commit
# connect.commit()

# # close connection
# connect.close()


class Bill_app:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        
        # ========== VARIABLES==========
        self.bill_num = StringVar()
        z = random.randint(100,999)
        self.bill_num.set(z)
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_email = StringVar()
        self.search_bill  = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.gst = StringVar()
        self.total = StringVar()
        
        
        
        
        # PRODUCT CATEGORIES LIST
        self.Category = ["Select option","Clothing","Footwears","Electronics","Grocery","Fmcg"]
        # make a subcategories and it's price
        self.SubCateclothing = ["pants","T_shirt","shirt"]
        # Pants
        self.pants = ["Leecopper","Levis","Spykar","Uspolo"]
        self.price_Leecopper = 1000
        self.price_Levis = 1100
        self.price_Spykar =1500
        self.price_Uspolo = 2000
        
        # T -shirt
        self.T_shirt = ["Adidas","Puma","MonteCarlo"]
        self.price_Adidas = 1000
        self.price_Puma = 1500
        self.price_MonteCarlo  = 2000
        
        
        # shirt
        self.shirt = ["Blackberrys","Raymond","PeterEngland","Allen Solly"]
        self.price_Blackberrys = 2500
        self.price_Raymond = 1000
        self.price_PeterEngland = 2000
        self.price_AllenSolly = 1500
        
        
        # FOOTWEAR
        self.SubCatefootwear = ["shoes","slippers"]
        #shoes
        self.shoes = ["adidas","puma","underarmour","newbalance"]
        self.price_adidas = 4000
        self.price_puma = 3000
        self.price_underarmour = 5000
        self.price_newbalance = 6000
        # slippers
        self.slippers = ["flite","bata","campus"]    
        self.price_campus = 300
        self.price_flite = 400
        self.price_bata = 500   
        
         #  ELECTRONICS
        self.SubCateelectronics = ["phone","laptop","trimer","headphone","Tv"]
        #phone
        self.phone = ["samsung","Apple","oppo","vivo"]
        self.price_samsung = 20000
        self.price_Apple = 100000
        self.price_oppo = 30000
        self.vivo = 25000
        
        #laptop
        self.laptop = ["Asus","HP","Dell"]
        self.price_Asus = 50000
        self.price_HP = 60000
        self.price_DELL = 70000
        
        #trimer
        self.trimer = ["philips","nova","panasonic"]
        self.price_philips = 1500
        self.price_nova = 1000
        self.price_panasonic = 2000
        
        #headphone
        self.headphone = ["boat","sony","jbl"]
        self.price_boat = 1500
        self.price_sony = 5000
        self.price_jbl = 4000
        
        #TV
        self.Tv = ["LG","Tcl","oneplus"]
        self.price_LG = 40000
        self.price_Tcl = 45000
        self.price_oneplus = 60000
        
        # GROCERY
        self.SubCategrocery = ["salt","rice","dal","wheat","sugar","jaggery"]
        #salt
        self.salt = ["tata_salt", "saffola_salt"]
        self.price_tata_salt = 40
        self.price_saffola_salt = 35
        
        #rice
        self.rice = ["kohinoor_rice", "dawat_rice"]
        self.price_dawat_rice = 400
        self.price_kohinoor_rice = 350
        
        #dal
        self.dal = ["moong dal","chana dal"]
        self.price_moong_dal = 100
        self.price_chana_dal = 150
        
        #wheat
        self.wheat = ["ashirvad_wheat","fortune_wheat"]
        self.price_ashivad_wheat = 200
        self.price_fortune_wheat = 300
        
        #sugar
        self.sugar = ["tata_sugar","fortune_sugar"]
        self.price_tata_sugar = 200
        self.price_fortune_sugar = 100
        
        #jaggery
        self.jaggery = ["patanjali_jaggery"]
        self.price_patanjali_jaggery = 100
         
         
        # FMCG
        self.SubCatefmcg = ["dish_washer","hair_oil","thoothpaste","body_lotion","soap"]
        # dish washer
        self.dish_washer = ["vim_dishwasher","dettol_dishwasher"]
        self.price_vim_dishwasher = 200
        self.price_dettol_dishwasher = 100
        
        # hair oil
        self.hair_oil = ["parachute_hairoil","dabar_amala_hairoil"]
        self.price_dabar_amala_hairoil = 200
        self.price_parachute_hairoil = 100
        
        # thoothpaste
        self.thoothpaste = ["colgate","dabar_red"]
        self.price_dabar_red = 50
        self.price_colgate = 60
        
        # body lotion
        self.body_lotion = ["vaseline","nivea"]
        self.price_vaseline = 220
        self.price_nivea = 300
        
        # soap
        self.soap = ["santoor","dove"]
        self.price_santoor = 60
        self.price_dove = 100
        
        
        
        
    
        # Create The Title Label
        self.lb_title = Label(self.root, text="Retail Billing System", font=("Helvetica", 35, "bold"), bg="white", fg="red")
        self.lb_title.place(x=0, y=0, width=1530, height=70)

        # Create the main frame under the title
        self.main_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        self.main_frame.place(x=0, y=70, width=1530, height=730)  # Position it below the title

        # CUSTOMER LABEL FRAME
        cust_frame = LabelFrame(self.main_frame ,text = "Customer",font = ("arial",15,"bold"),bg ="white",fg= "blue" )
        cust_frame.place(x=10, y= 5,width=350, height= 140)

        # FOR MOBILE NO
        self.lb_mob= Label(cust_frame,text= "Mobile No.",font = ("arial",13,"bold"),bg ="white")
        self.lb_mob.grid(row =0, column= 0 , sticky= W ,padx= 5 , pady = 2)
        # for Entry fild
        self.entry_mob = ttk.Entry(cust_frame,textvariable=self.c_phone ,font = ("arial",11,"bold"),width= 24) 
        self.entry_mob.grid(row=0 , column= 1)
         
        # FOR CUSTOMER NAME 
        self.lb_name = Label(cust_frame, text="Customer Name:", font=("arial", 11, "bold"), bg="white")
        self.lb_name.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        # for Entry fild
        self.entry_name = ttk.Entry(cust_frame,textvariable= self.c_name, font=("arial", 11, "bold"), width=24)
        self.entry_name.grid(row=1, column=1)
        
        # For CUSTOMER EMAIL
        self.lb_email = Label(cust_frame, text="Email:", font=("arial", 11, "bold"), bg="white")
        self.lb_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        # for email fild entry
        self.entry_email = ttk.Entry(cust_frame,textvariable= self.c_email, font=("arial", 11, "bold"), width=24)
        self.entry_email.grid(row=2, column=1)
        
        
        
        
        # PRODUCT label frame
        product_frame = LabelFrame(self.main_frame ,text = "Product",font = ("arial",15,"bold"),bg ="white",fg= "blue" )
        product_frame.place(x= 370, y= 5 ,width=730, height= 140)
        
        # for select categary label
        self.lb_Category = Label(product_frame, text="Select categories", font=("arial", 13, "bold"), bg="white")
        self.lb_Category.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        #  combo boxes
        self.combo_Category = ttk.Combobox(product_frame,value = self.Category ,font=('arial', 13, "bold"),width=24,state='readonly')
        self.combo_Category.current(0) # use current function for show by default value
        self.combo_Category.grid(row=0, column=1,sticky=W, padx=5, pady=2)
        # This is for binding category to combo box (Bind Method)
        self.combo_Category.bind('<<ComboboxSelected>>',self.Categories) 
        
        #subcategory
        self.lb_subCategory = Label(product_frame, text="Subcategories", font=("arial", 13, "bold"), bg="white")
        self.lb_subCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        
        self.combo_SubCategory = ttk.Combobox(product_frame,value =[""], font=('arial', 13, "bold"),width=24,state='readonly')
        self.combo_SubCategory.grid(row=1, column=1,sticky=W, padx=5, pady=2)
        self.combo_SubCategory.bind('<<ComboboxSelected>>',self.product_add) 
         
        
        #PRODUCT NAME 
        self.lb_product = Label(product_frame, text="Product Name", font=("arial", 13, "bold"), bg="white")
        self.lb_product.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        
        self.combo_product = ttk.Combobox(product_frame, textvariable= self.product,font=('arial', 13, "bold"),width=24,state='readonly')
        self.combo_product.grid(row=2, column=1,sticky=W, padx=5, pady=2)
        self.combo_product.bind('<<ComboboxSelected>>',self.price) 
        
        
        #PRICE
        self.lb_price = Label(product_frame, text="Price", font=("arial", 12, "bold"), bg="white")
        self.lb_price.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        
        self.combo_price = ttk.Combobox(product_frame, textvariable=self.prices,font=('arial', 12, "bold"),width=24,state='readonly')
        self.combo_price.grid(row=0, column=3,sticky=W, padx=5, pady=2)
        
        #Qty
        self.lb_Qty = Label(product_frame, text="Qty", font=("arial", 12, "bold"), bg="white")
        self.lb_Qty.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        
        self.combo_Qty = ttk.Entry(product_frame,textvariable=self.qty, font=('arial', 13, "bold"),width=26)
        self.combo_Qty.grid(row=1, column=3,sticky=W, padx=5, pady=2)
        
        # SEARCH BAR
        search_frame=Frame(self.main_frame,bd=2,bg="white")
        search_frame.place(x= 1110,y=5, width=400,height=40)
        
        self.Bill = Label(search_frame, text="Bill Number", font=("arial", 12, "bold"),fg= "white", bg="red")
        self.Bill.grid(row=0, column=0, sticky=W, padx=1)
        
        self.txt_entry = ttk.Entry(search_frame,textvariable=self.search_bill ,font=('arial', 10, "bold"),width=26)
        self.txt_entry.grid(row=0, column=1,sticky=W, padx=2) 
        
        self.btn_search=  Button(search_frame,text ="Find",command=self.fbill,font=("arial", 10, "bold"),bg="red",fg="white",width=7,cursor="hand2")
        self.btn_search.grid(row= 0 , column=2) 
        
        # RIGHTFRAME BILL AREA
        RightLabelFrame = LabelFrame(self.main_frame,text ='Bill Section',font = ("arial",15,"bold"),bg ="white",fg= "blue") 
        RightLabelFrame.place(x=1110,y=40,width=400,height=520)
        
        scroll_y = Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea = Text(RightLabelFrame,yscrollcommand= scroll_y.set ,bg="white",fg = "brown",font =("arial",15,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        self.welcome()
        
        
        self.li=[]
     ##====== Function declarations ==========
    def AddItem(self):
        gst =1 
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.li.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Select The Product")
        else:           
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('RS.%.2f'%(sum(self.li))))
            self.gst.set(str('RS.%.2f'%((((sum(self.li)) - (self.prices.get()))*gst)/100)))
            self.total.set(str('RS.%.2f'%(((sum(self.li))) + ((((sum(self.li)) - (self.prices.get()))*gst/100)))))

    # for generate bill button function
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Select The Product")
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.li))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n =============================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n gst:\t\t\t{self.gst.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,f"\n===========================")
            self.EntrySubTotal.insert(0, str(self.sub_total.get()))
            self.GST.insert(0, str(self.gst.get()))
            self.totalamount.insert(0, str(self.total.get()))
        
    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do You Want To Save The Bill ?")
        if op>0:
            self.bill_data = self.textarea.get(1.0,END)
            f1 = open('saved bills/'+str(self.bill_num.get())+".txt",'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved",f"Bill No:{self.bill_num.get()}saved successfully")
            f1.close()
    
    def bprint(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        
    def fbill(self):
        found = "no"
        for i in os.listdir("saved bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f'saved bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found = "yes"
        if found == "no":
            messagebox.showerror("ERROR","Invalid Bill Number.")        
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.bill_num = StringVar()
        z = random.randint(100,999)
        self.bill_num.set(str(z))
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        self.search_bill.set("") 
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.sub_total.set("")
        self.gst.set("")
        self.total.set("")
        self.welcome()
        self.li=[0]
        
    
    
          
    #==# For inside bill section
    def welcome(self):
        self.textarea.delete(1.0, END)
        # Welcome message
        welcome_message = "      Welcome to Dave's Mini Mall\n"
        self.textarea.insert(END, welcome_message)

        # Customer information
        self.textarea.insert(END, "=============================\n")
        self.insert_info("Bill Number:", self.bill_num.get())
        self.insert_info("Customer Name:", self.c_name.get())
        self.insert_info("Phone number:", self.c_phone.get())
        self.insert_info("Customer Email:", self.c_email.get())
        self.textarea.insert(END, "\n=============================\n")

        # Adjust the width to set the space between columns
        product_width = 20
        qty_width = 20
        price_width = 23
        
        # Format the headers with proper spacing
        product_header = "Product".ljust(product_width)
        qty_header = "Qty".ljust(qty_width)
        price_header = "Price".ljust(price_width)
        
        # Insert the formatted headers into the textarea
        self.insert_info(product_header, qty_header, price_header)
       
    def insert_info(self, *args):
        info_text = "\t".join(str(arg) for arg in args)
        self.textarea.insert(END, f"{info_text}\n")
            
        
    
        # BILL COUNTER label frame
        billcounter_frame = LabelFrame(self.main_frame ,text = "Bill Counter",font = ("arial",15,"bold"),bg ="white",fg= "blue" )
        billcounter_frame.place(x= 0, y= 570 ,width=1520, height= 190)
        
        #entryfields and label for billcounter
        self.lb_subtotal = Label(billcounter_frame,text="Sub Total", font=("arial", 12, "bold"), bg="white")
        self.lb_subtotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        # entry field
        self.EntrySubTotal = ttk.Entry(billcounter_frame ,font=('arial', 13, "bold"),width=26)
        self.EntrySubTotal.grid(row=0, column=1,sticky=W, padx=5, pady=2) 
        
        #For GST
        self.lb_gst = Label(billcounter_frame, text="GST", font=("arial", 12, "bold"), bg="white")
        self.lb_gst.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        # entry field
        self.GST = ttk.Entry(billcounter_frame, font=('arial', 13, "bold"),width=26)
        self.GST.grid(row=1, column=1,sticky=W, padx=5, pady=2) 
        
        #for TOTAL AMOUNT
        self.lb_totalamount = Label(billcounter_frame, text="Total Amount", font=("arial", 12, "bold"), bg="white")
        self.lb_totalamount.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        # entry field
        self.totalamount = ttk.Entry(billcounter_frame,font=('arial', 13, "bold"),width=26)
        self.totalamount.grid(row=2, column=1,sticky=W, padx=5, pady=2) 
        
        
        #BUTTON FRAME
        btn= Frame(billcounter_frame,bd=2 ,bg="white")
        btn.place(x = 420 , y= 0)
        
        self.btn=  Button(btn,height= 2,text = "Add To Cart",command=self.AddItem,font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=0) 
        
        self.btn=  Button(btn,height= 2,text = "Generate Bill",command=self.gen_bill ,font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=1) 
        
        self.btn=  Button(btn,height= 2,text = "Save Bill",command=self.save_bill,font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=2) 
        
        self.btn=  Button(btn,height= 2,text = "Print",command=self.bprint, font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=3) 
        
        self.btn=  Button(btn,height= 2,text = "Clear",command=self.clear, font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=4) 
        
        self.btn=  Button(btn,height= 2,text = "Exit",command=self.root.destroy, font=("arial", 12, "bold"),bg="green",fg="white",width= 17,cursor="hand2")
        self.btn.grid(row= 0 , column=5) 
       
        
     # for validation in combo box   
    def Categories(self,event = ""):
        if self.combo_Category.get()=="Clothing":
            self.combo_SubCategory.config(value=self.SubCateclothing)
            self.combo_SubCategory.current(0)
            
        if self.combo_Category.get()=="Footwears":
            self.combo_SubCategory.config(value=self.SubCatefootwear)
            self.combo_SubCategory.current(0)
            
        if self.combo_Category.get()=="Electronics":
            self.combo_SubCategory.config(value=self.SubCateelectronics)
            self.combo_SubCategory.current(0)    
            
        if self.combo_Category.get()=="Grocery":
            self.combo_SubCategory.config(value=self.SubCategrocery)
            self.combo_SubCategory.current(0)
            
        if self.combo_Category.get()=="Fmcg":
            self.combo_SubCategory.config(value=self.SubCatefmcg)
            self.combo_SubCategory.current(0)            
      
      # clothing
    def product_add(self,event=""):
        if self.combo_SubCategory.get()=="pants":
            self.combo_product.config(value =self.pants) 
            self.combo_product.current(0) 
            
        if self.combo_SubCategory.get()=="T_shirt":
            self.combo_product.config(value =self.T_shirt) 
            self.combo_product.current(0)
            
        if self.combo_SubCategory.get()=="shirt":
            self.combo_product.config(value =self.shirt) 
            self.combo_product.current(0)  
            
        
        # footwear
        if self.combo_SubCategory.get()=="shoes":
            self.combo_product.config(value = self.shoes)
            self.combo_product.current(0)  
            
        if self.combo_SubCategory.get()=="slippers":
            self.combo_product.config(value = self.slippers)
            self.combo_product.current(0)
                
                
        #Electronics     
        if self.combo_SubCategory.get()=="phone":
            self.combo_product.config(value = self.phone)
            self.combo_product.current(0)  
            
        if self.combo_SubCategory.get()=="laptop":
            self.combo_product.config(value = self.laptop)
            self.combo_product.current(0) 
            
        if self.combo_SubCategory.get()=="trimer":
            self.combo_product.config(value = self.trimer)
            self.combo_product.current(0) 
            
        if self.combo_SubCategory.get()=="headphone":
            self.combo_product.config(value = self.headphone)
            self.combo_product.current(0) 
            
        if self.combo_SubCategory.get()=="Tv":
            self.combo_product.config(value = self.Tv)
            self.combo_product.current(0)             
            
            
        # Grocery
        if self.combo_SubCategory.get()=="salt":
            self.combo_product.config(value = self.salt)
            self.combo_product.current(0)             
            
        if self.combo_SubCategory.get()=="rice":
            self.combo_product.config(value = self.rice)
            self.combo_product.current(0)                         
            
        if self.combo_SubCategory.get()=="dal":
            self.combo_product.config(value = self.dal)
            self.combo_product.current(0)             
            
        if self.combo_SubCategory.get()=="wheat":
            self.combo_product.config(value = self.wheat)
            self.combo_product.current(0)             
            
        if self.combo_SubCategory.get()=="sugar":
            self.combo_product.config(value = self.sugar)
            self.combo_product.current(0)                         
            
        if self.combo_SubCategory.get()=="jaggery":
            self.combo_product.config(value = self.jaggery)
            self.combo_product.current(0)             
                                        
        
        # FMCG
        if self.combo_SubCategory.get()=="dish_washer":
            self.combo_product.config(value = self.dish_washer)
            self.combo_product.current(0)   
            
        if self.combo_SubCategory.get()=="hair_oil":
            self.combo_product.config(value = self.hair_oil)
            self.combo_product.current(0)   
            
        if self.combo_SubCategory.get()=="thoothpaste":
            self.combo_product.config(value = self.thoothpaste)
            self.combo_product.current(0)           
            
        if self.combo_SubCategory.get()=="body_lotion":
            self.combo_product.config(value = self.body_lotion)
            self.combo_product.current(0)       
                 
        if self.combo_SubCategory.get()=="soap":
            self.combo_product.config(value = self.soap)
            self.combo_product.current(0)            
            
            
    # price function foe set prices
    def price(self,event = ""):
        #pant
        selected_product = self.combo_product.get()
        if selected_product == "Leecopper":
            self.prices.set(self.price_Leecopper)
            self.qty.set(1)
            
        if selected_product =="Levis":
            self.prices.set(self.price_Levis)
            self.qty.set(1)    
            
        if selected_product =="Spykar":
            self.prices.set(self.price_Spykar)
            self.qty.set(1) 
            
        if selected_product =="Uspolo":
            self.prices.set(self.price_Uspolo)
            self.qty.set(1)         

        # tshirt
        if selected_product =="Adidas":
            self.prices.set(self.price_Adidas)
            self.qty.set(1) 
            
        if selected_product =="Puma":
            self.prices.set(self.price_Puma)
            self.qty.set(1) 
            
        if selected_product =="MonteCarlo":
            self.prices.set(self.price_MonteCarlo)
            self.qty.set(1)         
        
        # shirt
        if selected_product =="Blackberrys":
            self.prices.set(self.price_Blackberrys)
            self.qty.set(1) 
            
        if selected_product =="Raymond":
            self.prices.set(self.price_Raymond)
            self.qty.set(1) 
        
        if selected_product =="PeterEngland":
            self.prices.set(self.price_PeterEngland)
            self.qty.set(1) 
        
        if selected_product =="AllenSolly":
            self.prices.set(self.price_AllenSolly)
            self.qty.set(1) 
            
        # shoes
        if selected_product =="adidas":
            self.prices.set(self.price_adidas)
            self.qty.set(1) 
            
        if selected_product =="puma":
            self.prices.set(self.price_puma)
            self.qty.set(1) 
            
        if selected_product =="underarmour":
            self.prices.set(self.price_underarmour)
            self.qty.set(1) 
            
        if selected_product =="newbalance":
            self.prices.set(self.price_newbalance)
            self.qty.set(1) 
            
        #slippers
        if selected_product =="campus":
            self.prices.set(self.price_campus)
            self.qty.set(1) 
            
        if selected_product =="flite ":
            self.prices.set(self.price_flite )
            self.qty.set(1)     
            
        if selected_product =="bata":
            self.prices.set(self.price_bata)
            self.qty.set(1) 
            
        #phone
        if selected_product =="samsung":
            self.prices.set(self.price_samsung)
            self.qty.set(1)     
            
        if selected_product =="Apple":
            self.prices.set(self.price_Apple)
            self.qty.set(1)     
        
        if selected_product =="oppo":
            self.prices.set(self.price_oppo)
            self.qty.set(1)     
        
        if selected_product =="vivo":
            self.prices.set(self.price_vivo)
            self.qty.set(1)     
        
        # laptop
        if selected_product =="Asus":
            self.prices.set(self.price_Asus)
            self.qty.set(1)      
        
        if selected_product =="HP":
            self.prices.set(self.price_HP)
            self.qty.set(1)  
            
        if selected_product =="Dell":
            self.prices.set(self.price_Dell)
            self.qty.set(1)          
            
        #trimmer
        if selected_product =="philips":
            self.prices.set(self.price_philips)
            self.qty.set(1)     
            
        if selected_product =="nova":
            self.prices.set(self.price_nova)
            self.qty.set(1)     
            
        if selected_product =="panasonic":
            self.prices.set(self.price_panasonic)
            self.qty.set(1)     
            
        # headphone 
        if selected_product =="boat":
            self.prices.set(self.price_boat)
            self.qty.set(1)      
            
        if selected_product =="sony":
            self.prices.set(self.price_sony)
            self.qty.set(1)      
            
        if selected_product =="jbl":
            self.prices.set(self.price_jbl)
            self.qty.set(1)      
            
        #TV
        if selected_product =="LG":
            self.prices.set(self.price_LG)
            self.qty.set(1)      
        
        if selected_product =="Tcl":
            self.prices.set(self.price_Tcl)
            self.qty.set(1)
                
        if selected_product =="oneplus":
            self.prices.set(self.price_oneplus)
            self.qty.set(1)      
            
        # fmcg
        ## dishwasher
        if selected_product =="vim_dishwasher":
            self.prices.set(self.price_vim_dishwasher)
            self.qty.set(1)      
             
        if selected_product =="dettol_dishwasher":
            self.prices.set(self.price_dettol_dishwasher)
            self.qty.set(1)      
            
        #hair oil
        if selected_product =="dabar_amala_hairoil":
            self.prices.set(self.price_dabar_amala_hairoil)
            self.qty.set(1)        
            
        if selected_product =="parachute_hairoil":
            self.prices.set(self.price_parachute_hairoil)
            self.qty.set(1)       
            
        #  thoothpaste
        if selected_product =="dabar_red":
            self.prices.set(self.price_dabar_red)
            self.qty.set(1)      
            
        if selected_product =="colgate":
            self.prices.set(self.price_colgate)
            self.qty.set(1)       
            
        # bodylotion
        if selected_product =="vaseline":
            self.prices.set(self.price_vaseline)
            self.qty.set(1)       
    
        if selected_product =="nivea":
            self.prices.set(self.price_nivea)
            self.qty.set(1)       
        
        #soap
        if selected_product =="santoor":
            self.prices.set(self.price_santoor)
            self.qty.set(1)
            
        if selected_product =="dove":
            self.prices.set(self.price_dove)
            self.qty.set(1)
            
        
        ###  grocery
        #dal
        if selected_product =="moong_dal":
            self.prices.set(self.price_moong_dal)
            self.qty.set(1)     
            
        if selected_product =="chana_dal":
            self.prices.set(self.price_chana_dal)
            self.qty.set(1)    
        
        #wheat    
        if selected_product =="ashivad_wheat":
            self.prices.set(self.ashivad_wheat)
            self.qty.set(1)    
            
        if selected_product =="fortune_wheat":
            self.prices.set(self.price_fortune_wheat)
            self.qty.set(1)    
        
        # salt    
        if selected_product =="tata_salt":
            self.prices.set(self.price_tata_salt)
            self.qty.set(1)    
            
        if selected_product =="saffola_salt":
            self.prices.set(self.price_saffola_salt)
            self.qty.set(1)    
        
        # rice    
        if selected_product =="dawat_rice":
            self.prices.set(self.price_dawat_rice)
            self.qty.set(1)    
            
        if selected_product =="kohinoor_rice":
            self.prices.set(self.price_kohinoor_rice)
            self.qty.set(1)    
        
        # sugar    
        if selected_product =="tata_sugar":
            self.prices.set(self.price_tata_sugar)
            self.qty.set(1)    
            
        if selected_product =="fortune_sugar":
            self.prices.set(self.price_fortune_sugar)
            self.qty.set(1)    
        
        # jaggery    
        if selected_product =="patanjali_jaggery":
            self.prices.set(self.price_patanjali_jaggery)
            self.qty.set(1)    
        
            
            
     
            
            
                  
            
        





















if __name__ == '__main__':
    root = Tk()  
    obj = Bill_app(root)
    root.mainloop()  