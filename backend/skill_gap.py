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


query = """
MATCH (c:Candidate {id: $candidate_id})
MATCH (j:Job {id: $job_id})

OPTIONAL MATCH (c)-[:HAS_SKILL]->(owned:Skill)

WITH c, j, collect(owned.id) AS owned_skill_ids

MATCH (j)-[:REQUIRES]->(required:Skill)

RETURN
    required.name AS skill,
    required.id IN owned_skill_ids AS has_skill
ORDER BY has_skill DESC, skill
"""


try:
    with driver.session() as session:

        result = session.run(
            query,
            candidate_id="candidate-001",
            job_id="job-002"
        )

        print()
        print("========================================")
        print("SKILL GAP ANALYSIS")
        print("========================================")
        print("Candidate: Saranya")
        print("Target Job: Machine Learning Engineer")
        print()

        for record in result:

            symbol = "✓" if record["has_skill"] else "✗"

            print(f"{symbol} {record['skill']}")

except Exception as e:

    print("ERROR:", e)

finally:
    driver.close()