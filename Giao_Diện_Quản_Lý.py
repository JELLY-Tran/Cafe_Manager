import tkinter as tk
root=tk.Tk()
root.title('QUẢN LÝ QUÁN CAFE')
root.geometry("1200x600")

#Lưu giá trị có thể thay đổi
r:int=0  # Row
c:int=0  # Column

#Khung trên thêm bàn cafe
khungTren=tk.Frame(root)
khungTren.pack(fill='both',expand=True)
tk.Button(khungTren,text='Thêm bàn',font=('Garamond',25),fg='red',bd=5).grid(row=r+1,column=c+1,padx=20,pady=20)

#Khung trên xóa bàn cafe
tk.Button(khungTren,text='Xóa bàn',font=('Garamond',25),fg='red',bd=5).grid(row=r+1,column=c+2,padx=20,pady=20)

#Khung trên chỉnh sửa bàn cafe
tk.Button(khungTren,text='Chỉnh sửa bàn',font=('Garamond',25),fg='red',bd=5).grid(row=r+1,column=c+3,padx=20,pady=20)

#Khung dưới thoát giao diện 
khungDuoi=tk.Frame(root)
khungDuoi.pack(side='bottom',fill='x')
tk.Button(khungDuoi,text='Thoát',font=('Garamond',25),fg='red',bd=5,command=root.quit).pack(side='right',padx=20,pady=20)

root.mainloop()
