import sqlite3
import pandas as pd

try:
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')

    query = """
    SELECT
        c.CustomerId,
        c.FirstName,
        c.LastName,
        c.Country,
        SUM(i.Total) AS TotalSpending
    FROM
        Customer c
    JOIN
        Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY
        c.CustomerId
    ORDER BY
        TotalSpending DESC
    LIMIT 10;
    """

    df = pd.read_sql_query(query, sqliteConnection)

    print("\n--- Top 10 khách hàng có tổng giá trị mua hàng cao nhất ---")
    print(df)


except sqlite3.Error as error:
    print("Lỗi xảy ra - ", error)

finally:
    if 'sqliteConnection' in locals() and sqliteConnection:
        sqliteConnection.close()
        print('\nSQLite Connection closed')