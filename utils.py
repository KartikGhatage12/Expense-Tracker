CATEGORIES=[
    "Food",
    "Travel",
    "Shopping",
    "Entertainment",
    "Bills",
    "Medical",
    "Education",
    "Others"
]

def validate_amount():
        while True:
            amount_input=input("Enter Amount : ").strip()
            if amount_input=="":
                print("Amount must be positive")
                continue
            try:
                amount=float(amount_input)
                if amount<=0:
                    print("Amount must be greater than 0!")
                    continue
                return amount
            except ValueError:
                print("Invalid amount ! Enter numbers only")

def validate_category():
    while True:
        print("\nAvailable Categories :")
        for index, category in enumerate(CATEGORIES,start=1):
            print(f"{index}. {category}")
        category_input=input("\nEnter Category : ").strip()
        if category_input=="":
            print("Category cannot be empty!!!")
            continue
        formatted_category=category_input.title()
        if formatted_category in CATEGORIES:
            return formatted_category
        else:
            print("Invalid category!!")

def validate_description():
    while True:
        description=input("Enter description : ").strip()
        if description=="":
            print("Description cannot be empty!!!")
            continue
        if len(description)>50:
            print("Description too long"
                  "Maximum 50 characters")
            continue
        return description.capitalize()