from app.database.db import conn

def save_price(product_name, store, price, url):

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO price_history
        (
            product_name,
            store,
            price,
            url
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        """,
        (
            product_name,
            store,
            price,
            url
        )
    )

    conn.commit()

    cur.close()



def get_price_history(product_name):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT

        store,

        price,

        created_at

        FROM price_history

        WHERE LOWER(product_name)
        LIKE LOWER(%s)

        ORDER BY created_at ASC
        """,

        (f"%{product_name}%",)
    )

    rows = cur.fetchall()

    cur.close()

    return rows



def get_lowest_price(product_name):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT MIN(price)

        FROM price_history

        WHERE LOWER(product_name)
        LIKE LOWER(%s)
        """,

        (f"%{product_name}%",)
    )

    result = cur.fetchone()

    cur.close()

    return result[0]



def get_highest_price(product_name):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT MAX(price)

        FROM price_history

        WHERE LOWER(product_name)
        LIKE LOWER(%s)
        """,

        (f"%{product_name}%",)
    )

    result = cur.fetchone()

    cur.close()

    return result[0]



def get_average_price(product_name):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT AVG(price)

        FROM price_history

        WHERE LOWER(product_name)
        LIKE LOWER(%s)
        """,

        (f"%{product_name}%",)
    )

    result = cur.fetchone()

    cur.close()

    if result[0]:

        return round(result[0], 2)

    return None



def get_latest_price(product_name):

    cur = conn.cursor()

    cur.execute(
        """
        SELECT

        price

        FROM price_history

        WHERE LOWER(product_name)
        LIKE LOWER(%s)

        ORDER BY created_at DESC

        LIMIT 1
        """,

        (f"%{product_name}%",)
    )

    result = cur.fetchone()

    cur.close()

    if result:

        return result[0]

    return None


def get_product_analytics(product_name):

    return {

        "current_price": get_latest_price(product_name),

        "lowest_price": get_lowest_price(product_name),

        "highest_price": get_highest_price(product_name),

        "average_price": get_average_price(product_name),

        "history": get_price_history(product_name)

    }