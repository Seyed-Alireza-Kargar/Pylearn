import sqlite3

def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers
                      (id INTEGER PRIMARY KEY, name TEXT, city TEXT, country TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL, count INTEGER)''')

def add_customer(cursor):
    name = input("نام مشتری: ")
    city = input("شهر: ")
    country = input("کشور: ")
    cursor.execute("INSERT INTO Customers (name, city, country) VALUES (?, ?, ?)", (name, city, country))

def add_product(cursor):
    name = input("نام محصول: ")
    price = float(input("قیمت: "))
    count = int(input("تعداد: "))
    cursor.execute("INSERT INTO Products (name, price, count) VALUES (?, ?, ?)", (name, price, count))

def show_available_products(cursor):
    cursor.execute('SELECT * FROM Products WHERE count > 0')
    available_products = cursor.fetchall()
    print("محصولات موجود:")
    for product in available_products:
        print(product)

def show_non_iranian_customers(cursor):
    cursor.execute("SELECT * FROM Customers WHERE country != 'ایران'")
    non_iranian_customers = cursor.fetchall()
    print("مشتریان غیر ایرانی:")
    for customer in non_iranian_customers:
        print(customer)

def delete_non_iranian_customers(conn, cursor):
    show_non_iranian_customers(cursor)
    choice = input("آیا می‌خواهید مشتریان غیر ایرانی را حذف کنید؟ (y/n): ")
    if choice.lower() == 'y':
        cursor.execute("DELETE FROM Customers WHERE country != 'ایران'")
        conn.commit()
        print("مشتریان غیر ایرانی با موفقیت حذف شدند.")

def update_product_prices(conn, cursor):
    cursor.execute("UPDATE Products SET price = price * 0.8")
    conn.commit()
    print("قیمت تمامی محصولات با موفقیت کاهش یافت.")

def main():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    create_table(cursor)
    
    while True:
        print("\nلطفاً یکی از گزینه‌های زیر را انتخاب کنید:")
        print("1. اضافه کردن مشتری جدید")
        print("2. اضافه کردن محصول جدید")
        print("3. نمایش کالاهای موجود")
        print("4. نمایش مشتریان غیر ایرانی و حذف آن‌ها")
        print("5. کاهش قیمت تمامی محصولات")
        print("6. خروج")

        choice = input("انتخاب شما: ")

        if choice == '1':
            add_customer(cursor)
            conn.commit()
        elif choice == '2':
            add_product(cursor)
            conn.commit()
        elif choice == '3':
            show_available_products(cursor)
        elif choice == '4':
            delete_non_iranian_customers(conn, cursor)
        elif choice == '5':
            update_product_prices(conn, cursor)
        elif choice == '6':
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره امتحان کنید.")

    conn.close()

if __name__ == "__main__":
    main()
