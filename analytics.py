import sqlite3

def total_expenses():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total=cursor.fetchone() 
    if total[0] is None:
        print("No expenses found")
    else:
        print("\n\n")
        print("="*35)
        print(f"Total Expenses: ₹{total[0]}")
        print("="*35)
    conn.close() 

def highest_expense():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT MAX(amount) FROM expenses")
    highest=cursor.fetchone()
    if highest[0] is None:
        print("No expenses found")
    else:
        print("\n\n")
        print("="*35)
        print(f"Highest Expense : ₹{highest[0]}")
        print("="*35)
    conn.close()

def smallest_expense():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT MIN(amount) FROM expenses")
    smallest=cursor.fetchone()
    if smallest[0] is None:
        print("No expenses found")
    else:
        print("\n\n")
        print("="*35)
        print(f"Smallest Expnese : ₹{smallest[0]}")
        print("="*35)
    conn.close()

def average_expense():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT AVG(amount) FROM expenses")
    average=cursor.fetchone()
    if average[0] is None:
        print("No expense found")
    else:
        print("\n\n")
        print("="*35)
        print(f"Average Expense : ₹{average[0]}")
        print("="*35)   
    conn.close()

def total_transactions():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    count=cursor.fetchone()
    print("\n\n")
    print("="*35)
    print(f"Total Transactions : {count[0]}")
    print("="*35)
    conn.close()

def category_summary():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT LOWER(category), SUM(amount) FROM expenses GROUP BY LOWER(category)")
    rows=cursor.fetchall()
    print("\n\n=======Catrgoey wise-Summary=======")
    if rows:
        for row in rows:
            print(f"{row[0].title():15} -> ₹{row[1]}")
    else:
        print("No Expenses found")
    conn.close()

def monthly_summary():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT amount,date FROM expenses")
    rows=cursor.fetchall()
    monthly_data={}
    for row in rows:
        amount=row[0]
        date=row[1]
        month_year=date[3:10]
        if month_year in monthly_data:
            monthly_data[month_year] += amount
        else:
            monthly_data[month_year] = amount
    print("\n\n=======Monthly Expense Summary=======")
    if monthly_data:
        for month ,total in sorted(monthly_data.items()):
            print(f"{month:<10} -> ₹{total:.2f}")
    else:
        print("No Expenses found")
    conn.close()

def analytics_menu():
    while True:
        print("="*35)
        print("     Analytics")
        print("="*35)
        print("1. Total Expenses")
        print("2. Highest Expense")
        print("3. Smallest Expense")
        print("4. Average Expense")
        print("5. Total Transactions")
        print("6. Category wise Summarry")
        print("7. Monthly Summary")
        print("8. Exit")
        print("="*35)
        choice=input("Enter your choice: ")
        if choice=="1":
            total_expenses()
        elif choice=="2":
            highest_expense()
        elif choice=="3":
            smallest_expense()
        elif choice=="4":
            average_expense()
        elif choice=="5":
            total_transactions()
        elif choice=="6":
            category_summary()
        elif choice=="7":
            monthly_summary()
        elif choice=="8":
            print("Exiting......")
            break
        else:
            print("Invaild input")