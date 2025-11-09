from config import load_config
from neo4j import GraphDatabase

config = load_config()

with GraphDatabase.driver(**config.get_neo4j_driver_kwargs()) as driver:
    driver.verify_connectivity()

    records, summary, keys = driver.execute_query("""
        MATCH (p:Player)-[:SHARES]->(l:Level)
        RETURN p.username AS username, l.name AS level_name
        """,
        database_=config.get_neo4j_database_name(),
    )

    # Loop through results and do something with them
    for record in records:
        print(record.data())  # obtain record as dict

    # Summary information
    print("The query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records),
        time=summary.result_available_after
    ))
