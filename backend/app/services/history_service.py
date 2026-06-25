from app.database.db import conn


def save_price(product_name, store, price, url):

    print("Saving:", product_name, price)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO price_history(
            product_name,
            store,
            price,
            url
        )
        VALUES(%s,%s,%s,%s)
        """,
        (
            product_name,
            store,
            price,
            url
        )
    )

    conn.commit()

    print("Saved Successfully")

    cur.close()

def get_price_history(
    product_name
):

    cur = conn.cursor()

    cur.execute(

        """

        SELECT

        store,

        price,

        created_at

        FROM price_history

        WHERE product_name=%s

        ORDER BY created_at ASC

        """,

        (

            product_name,

        )

    )

    rows = cur.fetchall()

    cur.close()

    return rows

def get_lowest_price(
    product_name
):

    cur = conn.cursor()

    cur.execute(

        """

        SELECT MIN(price)

        FROM price_history

        WHERE product_name=%s

        """,

        (

            product_name,

        )

    )

    result = cur.fetchone()

    cur.close()

    return result[0]