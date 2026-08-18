import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

uri = os.getenv("COGNODB_URI")
username = os.getenv("COGNODB_USERNAME")
password = os.getenv("COGNODB_PASSWORD")

print("Connecting to CognoDB...")

try:
    driver = GraphDatabase.driver(
        uri,
        auth=(username, password)
    )

    driver.verify_connectivity()

    print("SUCCESS: Connected to CognoDB!")

    with driver.session() as session:
        result = session.run(
            "RETURN 'Hello from CognoDB!' AS message"
        )

        record = result.single()

        print(record["message"])

    driver.close()

except Exception as e:
    print("ERROR: Could not connect to CognoDB")
    print(e)