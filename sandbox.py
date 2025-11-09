from database import GraphDatabaseDriver

with GraphDatabaseDriver() as driver:
    results = driver.execute_query("""
        MATCH (p:Player)-[:SHARES]->(l:Level)
        RETURN p.username AS username, l.name AS level_name
        """
    )

    # Loop through results and do something with them
    for x in results:
        print(x)  # obtain record as dict

    # Summary information
    records, summary, keys = driver.get_last_result_details()
    print("The query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records),
        time=summary.result_available_after
    ))
