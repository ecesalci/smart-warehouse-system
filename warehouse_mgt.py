import os

product_names = []
stock_quantities = []
unit_prices = []
categories = []
REPORT_FILE = "Inventory_Report.txt"

def load_data():
    if os.path.exists(REPORT_FILE):
        try:
            f = open(REPORT_FILE, "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            current_cat = "OTHER"
            for line in lines:
                line = line.strip()
                if "--- CATEGORY:" in line:
                    current_cat = line.replace("--- CATEGORY:", "").replace("---", "").strip()
                elif "|" in line and "Stock:" in line:
                    parts = line.split("|")
                    product_names.append(parts[0].strip())
                    stock_quantities.append(int(parts[1].split(":")[1].strip()))
                    unit_prices.append(float(parts[2].split(":")[1].replace("TL", "").strip()))
                    categories.append(current_cat)
        except: print("Warning: Could not load data.")

def update_report():
    f = open(REPORT_FILE, "w", encoding="utf-8")
    unique_cats = sorted(list(set(categories))) 
    for cat in unique_cats:
        f.write("--- CATEGORY: " + cat + " ---\n")
        for i in range(len(product_names)):
            if categories[i] == cat:
                report_line = product_names[i].ljust(15) + " | Stock: " + str(stock_quantities[i]).ljust(5) + " | Price: " + str(unit_prices[i]) + " TL"
                f.write(report_line + "\n")
        f.write("\n")
    f.close()

def main():
    load_data()
    while True:
        print("\n=== SMART WAREHOUSE MANAGEMENT SYSTEM ===")
        print("(1) Add Product\n(2) Inventory Statistics\n(3) Critical Stock Alert")
        print("(4) Search Inventory & Filter\n(5) Stock Out\n(6) Sort by Price/Name")
        print("(7) Show Report\n(8) Edit Price\n(9) Exit\n")
        try:
            choice = input("Select an option (1-9)        : ")
            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: raise ValueError
        except ValueError:
            print("\nError: Invalid selection!"); continue
        
        if choice == "1":
            print("(Enter 'Q' at any step to cancel)")
            while True:
                name = input("Product Name (or Q to cancel) : ").upper().strip()
                if name == 'Q': break
                if name and not name.replace(" ", "").isdigit(): break
                print("Error: Invalid name!")
            if name == 'Q': continue
            while True:
                qty_in = input("Quantity (or Q to cancel)     : ").upper().strip()
                if qty_in == 'Q': break
                try:
                    qty = int(qty_in)
                    if qty >= 0: break
                    print("Error: Negative value!")
                except: print("Error: Invalid number.")
            if qty_in == 'Q': continue
            while True:
                price_in = input("Unit Price (or Q to cancel)   : ").upper().strip()
                if price_in == 'Q': break
                try:
                    price = float(price_in)
                    if price >= 0: break
                    print("Error: Negative price!")
                except: print("Error: Invalid number.")
            if price_in == 'Q': continue
            allowed_cats = ["FOOD", "BEVERAGE", "ELECTRONICS", "OTHER"]
            print("Available: [FOOD, BEVERAGE, ELECTRONICS, OTHER]")
            while True:
                cat = input("Category (or Q to cancel)     : ").upper().strip()
                if cat == 'Q': break
                if cat in allowed_cats: break
                print("Invalid category!")
            if cat == 'Q': continue
            if cat == "OTHER":
                detail = input("Specify detail (or Q to cancel): ").upper().strip()
                if detail == 'Q': continue
                cat = "OTHER: " + (detail if detail else "UNSPECIFIED")
            product_names.append(name)
            stock_quantities.append(qty)
            unit_prices.append(price)
            categories.append(cat)
            update_report()
            print("\nProduct added successfully.")
        elif choice == "2":
            if not product_names: print("\nInventory is empty.")
            else:
                total_val = sum([stock_quantities[i] * unit_prices[i] for i in range(len(product_names))])
                print("\nTotal Value                   : " + str(total_val) + " TL")
                for cat in set(categories):
                    val = sum([stock_quantities[i] * unit_prices[i] for i in range(len(product_names)) if categories[i] == cat])
                    print("Category " + cat.ljust(20) + " : " + str(val) + " TL")
        elif choice == "3":
            try:
                threshold = int(input("\nEnter threshold               : "))
                print("\nCritical Items:")
                found = False
                for i in range(len(product_names)):
                    if stock_quantities[i] < threshold:
                        print("- " + product_names[i] + ": " + str(stock_quantities[i]))
                        found = True
                if not found: print("No critical items.")
            except ValueError: print("\nError: Invalid number.")
        elif choice == "4":
            mode = input("Search (K)eyword or (P)rice? (Q to cancel): ").upper()
            if mode == 'K':
                kw = input("Keyword                       : ").upper()
                for i in range(len(product_names)):
                    if kw in product_names[i]: print(product_names[i] + " | " + str(unit_prices[i]) + " TL")
            elif mode == 'P':
                while True:
                    min_p_in = input("Min Price (or Q to cancel)    : ").upper().strip()
                    if min_p_in == 'Q': break
                    try:
                        min_p = float(min_p_in)
                        if min_p >= 0: break
                        print("Error: Price cannot be negative!")
                    except: print("Error: Invalid number.")
                if min_p_in == 'Q': continue
                while True:
                    max_p_in = input("Max Price (or Q to cancel)    : ").upper().strip()
                    if max_p_in == 'Q': break
                    try:
                        max_p = float(max_p_in)
                        if max_p >= min_p: break
                        print("Error: Max price cannot be less than Min!")
                    except: print("Error: Invalid number.")
                if max_p_in == 'Q': continue
                print("\nResults:")
                for i in range(len(product_names)):
                    if min_p <= unit_prices[i] <= max_p: print(product_names[i] + " | " + str(unit_prices[i]) + " TL")
        elif choice == "5":
            name = input("Enter name                    : ").upper()
            if name in product_names:
                idx = product_names.index(name)
                try:
                    qty = int(input("Remove amount                 : "))
                    if 0 <= qty <= stock_quantities[idx]:
                        stock_quantities[idx] -= qty
                        update_report()
                        print("Success. Remaining: " + str(stock_quantities[idx]))
                    else: print("Error: Invalid amount or out of stock.")
                except ValueError: print("Error: Invalid number.")
            else: print("Product not found.")
        elif choice == "6":
            sort_mode = input("Sort by (A)lphabet or (P)rice? : ").upper()
            for i in range(len(product_names)):
                for j in range(0, len(product_names) - i - 1):
                    condition = False
                    if sort_mode == 'A': condition = product_names[j] > product_names[j + 1]
                    elif sort_mode == 'P': condition = unit_prices[j] > unit_prices[j + 1]
                    else: break 
                    if condition:
                        product_names[j], product_names[j+1] = product_names[j+1], product_names[j]
                        stock_quantities[j], stock_quantities[j+1] = stock_quantities[j+1], stock_quantities[j]
                        unit_prices[j], unit_prices[j+1] = unit_prices[j+1], unit_prices[j]
                        categories[j], categories[j+1] = categories[j+1], categories[j]
            update_report()
            print("\nSorted successfully.")
        elif choice == "7":
            if not product_names: print("\nEmpty.")
            else:
                print("\n--- CURRENT REPORT ---")
                for i in range(len(product_names)):
                    print(product_names[i].ljust(15) + " | Stock: " + str(stock_quantities[i]).ljust(5) + " | Price: " + str(unit_prices[i]) + " TL")
                print("----------------------")
        elif choice == "8":
            if not product_names: print("\nInventory is empty."); continue
            while True:
                unique_cats = sorted(list(set(categories)))
                print("\nAvailable Categories:")
                for idx, cat in enumerate(unique_cats, 1): print(f"({idx}) {cat}")
                try:
                    c_idx = int(input("Select category (0 to cancel) : ")) - 1
                    if c_idx == -1: break
                    selected_cat = unique_cats[c_idx]
                    while True:
                        print(f"\nProducts in {selected_cat}:")
                        cat_indices = [i for i, c in enumerate(categories) if c == selected_cat]
                        for idx, i in enumerate(cat_indices, 1): print(f"({idx}) {product_names[i]} - Current Price: {unit_prices[i]} TL")
                        p_idx_in = int(input("Select product (0 to cancel)  : ")) - 1
                        if p_idx_in == -1: break
                        target_idx = cat_indices[p_idx_in]
                        new_price = float(input(f"Enter new price for {product_names[target_idx]}: "))
                        if new_price >= 0:
                            unit_prices[target_idx] = new_price
                            update_report()
                            print("Price updated successfully."); break
                        else: print("Error: Price cannot be negative!")
                    break
                except (ValueError, IndexError): print("Error: Invalid selection! Try again.")
        elif choice == "9": break

if __name__ == "__main__":
    main()