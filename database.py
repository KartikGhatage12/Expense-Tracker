import csv
import sqlite3
from datetime import datetime
import shutil
from utils import(validate_amount,validate_category,validate_description,CATEGORIES)


def create_table():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT,
               amount REAL,
               category TEXT,
               date TEXt,
               description TEXT)""")
    conn.commit()
    conn.close()

def add_expenses():
    while True:
        try:
            amount=validate_amount()
            break
        except ValueError:
            print("Invalid input! Enter again")

    category = validate_category()

    while True:
        date = input("Enter a date (DD/MM/YYYY): ")
        try:
             valid_date = datetime.strptime(date, "%d/%m/%Y")
             formatted_date=datetime.strftime(valid_date,"%d/%m/%Y")
             break
        except ValueError:
             print("\nInvalid format or date. Please try again.")

    description = validate_description()

    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("""
    INSERT INTO expenses(amount,category,date,description)
    VALUES(?,?,?,?)""",(amount,category,formatted_date,description))
    conn.commit()
    conn.close()
    print("\nExpenses added successfully")


    # with open(path, "a", newline="") as file:
    #     writer = csv.writer(file)
    #     writer.writerow([amount, category, date, description])

    # print("\nExpense Added Successfully!")
    # print("Amount:", amount)
    # print("Category:", category)
    # print("Date:", date)
    # print("Description:", description)


# import os
# if not os.path.exists("Expenses.csv"):
#     with open(path,"w",newline="") as file:
#         writer=csv.writer(file)
#         writer.writerow(["Amount" ,"Category" ,"Date" ,"Description"])



def view_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("        \nNo Expense Added Yet        ")
        conn.close()
        return
    cursor.execute("SELECT * FROM expenses")
    rows=cursor.fetchall()
    print("\n\n=====All Expenses=====")
    for row in rows:
        print("=" * 35)

        print(f"ID             :{row[0]}")
        print(f"Amount         :{row[1]}")
        print(f"Category       :{row[2].title()}")
        print(f"Date           :{row[3]}")
        print(f"Description    :{row[4]}")
        
        print("=" * 35)
    conn.close()
    # with open(path,"r")as file:
    #     reader=csv.reader(file)
    #     next(reader)
    #     print("\n=====All Expenses=====(this line was written for csv objects view)")
    #     for index,row in enumerate(reader,start=1):
    #         if len(row)>=4:
    #             print(f"{index}.Amount: ₹{row[0]} | Category: {row[1]} | Date: {row[2]} | Description: {row[3]}")
        
def delete_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("\nNo Expenses to delete")
        conn.close()
        return
    view_expenses()
    try:
        delete_ID=int(input("\n\nEnter ID to delete:"))
        cursor.execute("DELETE FROM expenses WHERE id=?",(delete_ID,))
        if cursor.rowcount==0:
            print("\nExpense ID not found")
        else:
            conn.commit()
            print("Expense Deleted")
        conn.close()
    except ValueError:
        print("\nInvalid input!!! Enter only Id number")
    # expenses = []
    # with open(path, "r") as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         if row:
    #             expenses.append(row)
    # if not expenses:
    #     print("Expenses file empty !!")
    #     return
    # view_expenses()

    # while True:
    #     try:
    #         delete_id = int(input("Enter Expense ID to delete(made for csv file deletion)"))
    #         if delete_id >= 1 and delete_id <= len(expenses):
    #             expenses.pop(delete_id - 1)

    #             with open(path, "w", newline="") as file:
    #                 writer = csv.writer(file)
    #                 writer.writerows(expenses)

    #             print("Expense deleted successfully !!")
    #             break
    #         else:
    #             print("Expense ID does not exist")
    #     except ValueError:
    #         print("Enter only numeric Expense ID")

def search_expenses():
    search_catrgory=input("\n\nEnter category to search: ")
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM  expenses WHERE LOWER(category) = LOWER(?)",(search_catrgory,))
    rows=cursor.fetchall()

    print("\n=====Search Result=====")
    if rows:
        for row in rows:
           
           print("=" * 35)

           print(f"ID             :{row[0]}")
           print(f"Amount         :{row[1]}")
           print(f"Category       :{row[2].title()}")
           print(f"Date           :{row[3]}")
           print(f"Description    :{row[4]}")
        
           print("=" * 35)
    else:
        print("No matching found for the give catrgory")
    conn.close()
    

    # while True:
    #     search_category=input("Enter category to search: ")
    #     with open(path,"r") as file:
    #         reader=csv.reader(file)
    #         found=False
    #         print("\n=====Search Result=====")
    #         for index,row in enumerate(reader,start=1):
    #             if row[1].lower()==search_category.lower():
    #                 print(f"{index}. Amount :₹{row[0]} | Category : {row[1]} | Date : {row[2]} | Description : {row[3]}")
    #                 found=True
    #         if not found:
    #             print("No matching expense found for entered category")


def update_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("No Expenses found")
        conn.close()
        return
    view_expenses()
    try:
        expense_id=int(input("Enter Expense ID to Update: "))
    except ValueError:
        print("Invalid Id")
        conn.close()
        return
    cursor.execute("SELECT * FROM expenses WHERE id=?",(expense_id,))
    row=cursor.fetchone()
    if row is None:
        print("Expense ID not found")
        conn.close()
        return
    
    print("\nLeave the field blank to keep old value")
    print("Press Enter to leave blank\n")
    
    old_amount=row[1]
    old_category=row[2]
    old_date=row[3]
    old_description=row[4]

    amount_input=(input(f"Enter new Amount [{old_amount}] : ")).strip()
    if amount_input=="":
        new_amount=old_amount
    else:
        try:
            new_amount=float(amount_input)
            if new_amount<=0:
                print("Amount should be positive")
                conn.close()
                return
        except ValueError:
            print("Invalid amount!!")
            conn.close()
            return
    
    category_input=input(f"Enter new Catrgory [{old_category}] : ").strip()
    if category_input=="":
        new_category=old_category
    else:
        formatted_category=category_input.title()
        if formatted_category in CATEGORIES:
            new_category=formatted_category
        else:
            print("Invalid category!!!")
            conn.close()
            return
    
    date_input=input(f"Enter new Date [{old_date}] : ").strip()
    if date_input=="":
        new_date=old_date
    else:
        try:
            valid_date=datetime.strptime(date_input,"%d/%m/Y%")
            new_date=valid_date.strftime("%d/%m/Y%")
        except ValueError:
            print("Invalid date")
            conn.close()
            return
    
    description_input=input(f"Enter new Description [{old_description}] : ").strip()
    if description_input=="":
        new_description=old_description
    else:
        if len(description_input)>50:
            print("Description too long!"
                  "Maximum 50 characters")
            conn.close()
            return
        new_description=description_input
        new_description=description_input.capitalize()

    cursor.execute(f"UPDATE expenses SET amount=?,category=?,date=?,description=? WHERE id=?",(new_amount,new_category,new_date,new_description,expense_id))
    
    conn.commit()
    print("\nExpenses updated successfully!!!")
    conn.close()
    # print("What do you want to change: ")

    # print("1. Amount")
    # print("2. Category")
    # print("3. Date")
    # print("4. Description")

    # choice=input("Enter your choice: ")

    # if choice=="1":
    #     try:
    #         new_amount=float(input("Enter new amount: "))
    #         if new_amount<=0:
    #             print("Amount must be positive!!")
    #             conn.close()
    #             return
    #         cursor.execute("UPDATE expenses SET amount=? WHERE id=?",(new_amount,expense_id))
    #     except ValueError:
    #         print("Invalid amount")
    #         conn.close()
    #         return
    # elif choice=="2":
    #     new_category=input("Enter new category: ").strip()
    #     if new_category=="":
    #         print("Category cannot be empty!!")
    #         conn.close()
    #         return
    #     cursor.execute("UPDATE expenses SET category=? WHERE id=?",(new_category,expense_id))
    # elif choice=="3":
    #     while True:
    #         new_date=input("Enter new Date (DD/MM/YYYY): ")
    #         try:
    #             valid_date=datetime.strptime(new_date,"%d/%m/%")
    #             formatted_date=valid_date.strftime("%d/%m/%")
    #             break
    #         except ValueError:
    #             print("Invalid date!")
    #     cursor.execute("UPDATE expenses SET date=? WHERE id=?",(formatted_date,expense_id))
    # elif choice=="4":
    #     new_description=input("Enter new Description: ").strip()
    #     if new_description=="":
    #         print("Description cannot be empty")
    #         conn.close()
    #         return
    #     cursor.execute("UPDATE expenses SET description=? WHERE id=?",(new_description,expense_id))
    # else:
    #     print("Invalid input!!")
    #     conn.close()
    #     return
    # conn.commit()
    # print("Expense Updated successfully!!")
    # conn.close()


    
def export_to_csv():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows=cursor.fetchall()
    if len(rows)==0:
        print("No expenses found to export!")
        conn.close()
        return
    with open("expenses_export.csv","w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([
        "ID",
        "Amount",
        "Category",
        "Date",
        "Description",
        ])

        writer.writerows(rows)
    print("\nData exported successfully")
    print("File name: expenses_report.csv")
    conn.close()

def sort_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT (*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("No expenses found")
        conn.close()
        return
    print("\n=====Sort Options=====")
    
    print("1. Amount")
    print("2. Category")
    print("3. Date")

    sort_choice=(int(input("Sort by : ")))

    print("\n1. Ascending")
    print("2. Descending")

    order_choice=(int(input("Order : ")))
    if sort_choice==1:
        column="amount"
    elif sort_choice==2:
        column="category"
    elif sort_choice==3:
        column="date"
    else:
        print("Invalid option")
        conn.close()
        return
    if order_choice==1:
        order="ASC"
    elif order_choice==2:
        order="DESC"
    else:
        print("Invalid order option")
        conn.close()
        return
    query=f"SELECT * FROM expenses ORDER BY {column} {order}"
    cursor.execute(query)
    rows=cursor.fetchall()
    print("\n=====SORTED EXPENSES=====")
    for row in rows:
        print("="*35)
        print(f"ID              :{row[0]}")
        print(f"Amount          :₹{row[1]}")
        print(f"Category        :{row[2]}")
        print(f"Date            :{row[3]}")
        print(f"Description     :{row[4]}")

        print("="*35)
    conn.close()

def latest_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("No expenses found")
        conn.close()
        return
    try:
        limit=int(input("How many latest expenses to show???: "))
        if limit<0:
            print("Limit must br greater than 0")
            conn.close()
            return
    except ValueError:
        print("Invalid number!!!")
        conn.close()
        return
    cursor.execute(f"SELECT * FROM expenses ORDER BY id DESC LIMIT ?",(limit,))
    rows=cursor.fetchall()
    print("\n===== LATEST EXPENSES =====")
    for row in rows:
        print("="*35)

        print(f"ID              :{row[0]}")
        print(f"Amount          :₹{row[1]}")
        print(f"Category        :{row[2]}")
        print(f"Date            :{row[3]}")
        print(f"Description     :{row[4]}")

        print("="*35)
    conn.close()

def database_backup():
    try:
        shutil.copy("expenses.db","expenses_backup.db")
        print("\nDatabase backup created successfully")
        print("Backup file : expenses_backup.db")
    except FileNotFoundError:
        print("Database file not found")
    except Exception as e:
        print("Error creating backup!")
        print(e)

def delete_all_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    total=cursor.fetchone()
    if total[0]==0:
        print("No Expenses found")
        conn.close()
        return
    print("\nWARNING!!!")
    print("This will delete all the expenses permanently.")
    confirm=input("Type YES to confirm and NO to abort activity : ").strip()
    if confirm!="YES":
        print("Operation cancelled")
        conn.close()
        return
    cursor.execute("DELETE FROM expenses")
    conn.commit()
    print("\nAll Expeses Delete Successfully")
    conn.close()