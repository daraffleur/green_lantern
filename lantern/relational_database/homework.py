from typing import List

import psycopg2



def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """

    cursor = con.cursor()
    cursor.execute("INSERT INTO Customers (Customername, Contactname, Address, City, Postalcode, Country) "
                   "VALUES (%s, %s, %s, %s, %s, %s)",
                   ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore',))
    con.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """

    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """

    cur.execute("SELECT * FROM Customers WHERE Country = 'Germany'")
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        con: psycopg cursor

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    cur.execute(
        "UPDATE Customers SET Customername = 'Johnny Depp' WHERE Customerid = (SELECT MIN(Customerid) FROM Customers)")
    con.commit()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    
    cursor = con.cursor()
    cursor.execute("DELETE FROM Customers WHERE Customerid = (SELECT MAX(Customerid) FROM Customers);")
    con.commit()



def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("SELECT Country FROM Suppliers")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """

    cur.execute("SELECT Country FROM Suppliers ORDER BY Country DESC")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order
    """
    
    execute("SELECT COUNT(Customerid), City FROM Customers GROUP BY City ORDER BY City DESC")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT COUNT(Customername), Country FROM Customers GROUP BY Country HAVING COUNT(Customername) > 10")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    
    cur.execute("SELECT * FROM Customers LIMIT 10")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    
    cur.execute("SELECT * FROM Customers OFFSET 11")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """

    cur.execute("SELECT Supplierid, Suppliername, Contactname, City, Country FROM Suppliers"
                "WHERE Country in ('USA','UK','Japan')")
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT Productname FROM Products, Suppliers WHERE Country = 'Sweden' AND Products.SupplierID = "
                "Suppliers.Supplierid")
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """

    cur.execute("""SET LOCAL lc_monetary = 'en_US.UTF-8'; 
    SELECT Productid, Productname, Unit, Price, Country, City, Suppliername
    FROM Products, Suppliers WHERE Products.Supplierid = Suppliers.Supplierid;""")
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """

    cur.execute("SELECT Customername, Contactname, Country, Orderid FROM Customers, Orders "
                "WHERE Customers.Customerid = Orders.Customerid")
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """

    cur.execute("SELECT C.Customername, C.Address, C.Country as Customercountry, S.Country "
                "as Suppliercountry, S.Suppliername "
                "FROM Customers as c FULL JOIN Suppliers as s ON S.Country = c.Country "
                "ORDER BY Customercountry, Suppliercountry")
    return cur.fetchall()
