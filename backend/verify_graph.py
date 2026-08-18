import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()

    with driver.session() as session:

        result = session.run(
            """
            MATCH (n)
            RETURN count(n) AS total_nodes
            """
        )

        record = result.single()

        print("Total nodes:", record["total_nodes"])

        result = session.run(
            """
            MATCH ()-[r]->()
            RETURN count(r) AS total_relationships
            """
        )

        record = result.single()

        print(
            "Total relationships:",
            record["total_relationships"]
        )

finally:
    driver.close()