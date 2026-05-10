import sqlite3


def parse_chrome_history(path):

    conn = sqlite3.connect(path)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            url,
            title,
            visit_count
        FROM urls
        ORDER BY visit_count DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    results = []

    for row in rows:

        results.append({

            "type": "HISTORY",
            "url": row[0],
            "title": row[1],
            "visit_count": row[2]
        })

    return results


def parse_chrome_downloads(path):

    conn = sqlite3.connect(path)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            tab_url,
            target_path
        FROM downloads
        """
    )

    rows = cursor.fetchall()

    conn.close()

    results = []

    for row in rows:

        results.append({

            "type": "DOWNLOAD",
            "url": row[0],
            "path": row[1]
        })

    return results


def parse_chrome_logins(path):

    conn = sqlite3.connect(path)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            origin_url,
            username_value,
            password_value
        FROM logins
        """
    )

    rows = cursor.fetchall()

    conn.close()

    results = []

    for row in rows:

        encrypted = (
            "[ENCRYPTED]"
            if row[2]
            else "[EMPTY]"
        )

        results.append({

            "type": "LOGIN",
            "url": row[0],
            "username": row[1],
            "password": encrypted
        })

    return results