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
      -[:HAS_SKILL]->(s1:Skill)
      -[:RELATED_TO]->(s2:Skill)
      <-[:REQUIRES]-(j:Job)
RETURN DISTINCT
       c.name AS candidate,
       s1.name AS existing_skill,
       s2.name AS related_skill,
       j.title AS recommended_job
ORDER BY recommended_job
"""


try:
    with driver.session() as session:

        result = session.run(
            query,
            candidate_id="candidate-001"
        )

        print()
        print("========================================")
        print("MULTI-HOP CAREER RECOMMENDATIONS")
        print("========================================")

        for record in result:

            print(
                f"{record['candidate']} | "
                f"{record['existing_skill']} -> "
                f"{record['related_skill']} -> "
                f"{record['recommended_job']}"
            )

except Exception as e:

    print("ERROR:", e)

finally:

    driver.close()