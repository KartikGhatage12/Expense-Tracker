from database import *
from analytics import analytics_menu
create_table() 

while True:
    print("\n\n"+"="*35)
    print("     Expense Tracker")
    print("=" * 35)

    print("1.  Add Expenses")
    print("2.  View Expenses")
    print("3.  Update Expenses")
    print("4.  Delete Expenses")
    print("5.  Search Expense")
    print("6.  Sort Expenses")
    print("7.  Latest Expenses")
    print("8.  Analytics")
    print("9.  Backup database")
    print("10. Export to csv")
    print("11. Delete all expenses")
    print("12. Exit")
    print("="*35)

    
    choice = input("Enter your choice: ")
    print("="*35)

    if choice=="1":
        add_expenses()

    elif choice=="2":
        view_expenses()

    elif choice=="3":
        update_expenses()

    elif choice=="4":
        delete_expenses()

    elif choice=="5":
        search_expenses()

    elif choice=="6":
        sort_expenses()

    elif choice=="7":
        latest_expenses()

    elif choice=="8":
        analytics_menu()

    elif choice=="9":
        database_backup()

    elif choice=="10":
        export_to_csv()

    elif choice=="11":
        delete_all_expenses()

    elif choice=="12":
        print("Exiting process....")
        break

    else:
        print("Invalid choice! Please try again")