import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "backend",
        ".env"
    )
)

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def create_constraints(session):
    queries = [
        """
        CREATE CONSTRAINT candidate_id IF NOT EXISTS
        FOR (c:Candidate)
        REQUIRE c.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT skill_id IF NOT EXISTS
        FOR (s:Skill)
        REQUIRE s.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT job_id IF NOT EXISTS
        FOR (j:Job)
        REQUIRE j.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT company_id IF NOT EXISTS
        FOR (c:Company)
        REQUIRE c.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT project_id IF NOT EXISTS
        FOR (p:Project)
        REQUIRE p.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT technology_id IF NOT EXISTS
        FOR (t:Technology)
        REQUIRE t.id IS UNIQUE
        """,
        """
        CREATE CONSTRAINT resource_id IF NOT EXISTS
        FOR (r:LearningResource)
        REQUIRE r.id IS UNIQUE
        """
    ]

    for query in queries:
        session.run(query)


def seed_candidates(session):
    candidates = [
        {
            "id": "candidate-001",
            "name": "Saranya",
            "education": "B.Tech Artificial Intelligence and Machine Learning"
        },
        {
            "id": "candidate-002",
            "name": "Rahul",
            "education": "B.Tech Computer Science"
        },
        {
            "id": "candidate-003",
            "name": "Priya",
            "education": "B.Tech Information Technology"
        }
    ]

    session.run(
        """
        UNWIND $candidates AS candidate
        MERGE (c:Candidate {id: candidate.id})
        SET c.name = candidate.name,
            c.education = candidate.education
        """,
        candidates=candidates
    )


def seed_skills(session):
    skills = [
        {"id": "python", "name": "Python"},
        {"id": "sql", "name": "SQL"},
        {"id": "machine-learning", "name": "Machine Learning"},
        {"id": "deep-learning", "name": "Deep Learning"},
        {"id": "tensorflow", "name": "TensorFlow"},
        {"id": "pytorch", "name": "PyTorch"},
        {"id": "fastapi", "name": "FastAPI"},
        {"id": "flask", "name": "Flask"},
        {"id": "react", "name": "React"},
        {"id": "javascript", "name": "JavaScript"},
        {"id": "git", "name": "Git"},
        {"id": "docker", "name": "Docker"},
        {"id": "aws", "name": "AWS"},
        {"id": "data-analysis", "name": "Data Analysis"},
        {"id": "pandas", "name": "Pandas"},
        {"id": "numpy", "name": "NumPy"},
        {"id": "computer-vision", "name": "Computer Vision"},
        {"id": "nlp", "name": "Natural Language Processing"},
        {"id": "rest-api", "name": "REST APIs"},
        {"id": "statistics", "name": "Statistics"}
    ]

    session.run(
        """
        UNWIND $skills AS skill
        MERGE (s:Skill {id: skill.id})
        SET s.name = skill.name
        """,
        skills=skills
    )


def seed_companies(session):
    companies = [
        {
            "id": "company-001",
            "name": "TechNova",
            "industry": "Technology"
        },
        {
            "id": "company-002",
            "name": "DataWorks",
            "industry": "Data and Analytics"
        },
        {
            "id": "company-003",
            "name": "InnovateAI",
            "industry": "Artificial Intelligence"
        },
        {
            "id": "company-004",
            "name": "CloudStack",
            "industry": "Cloud Computing"
        },
        {
            "id": "company-005",
            "name": "VisionLabs",
            "industry": "Computer Vision"
        }
    ]

    session.run(
        """
        UNWIND $companies AS company
        MERGE (c:Company {id: company.id})
        SET c.name = company.name,
            c.industry = company.industry
        """,
        companies=companies
    )


def seed_jobs(session):
    jobs = [
        {
            "id": "job-001",
            "title": "Python Developer",
            "level": "Entry Level"
        },
        {
            "id": "job-002",
            "title": "Machine Learning Engineer",
            "level": "Entry Level"
        },
        {
            "id": "job-003",
            "title": "AI Engineer",
            "level": "Entry Level"
        },
        {
            "id": "job-004",
            "title": "Data Analyst",
            "level": "Entry Level"
        },
        {
            "id": "job-005",
            "title": "Data Scientist",
            "level": "Entry Level"
        },
        {
            "id": "job-006",
            "title": "Backend Developer",
            "level": "Entry Level"
        },
        {
            "id": "job-007",
            "title": "Computer Vision Engineer",
            "level": "Entry Level"
        },
        {
            "id": "job-008",
            "title": "Full Stack Developer",
            "level": "Entry Level"
        }
    ]

    session.run(
        """
        UNWIND $jobs AS job
        MERGE (j:Job {id: job.id})
        SET j.title = job.title,
            j.level = job.level
        """,
        jobs=jobs
    )


def seed_projects(session):
    projects = [
        {
            "id": "project-001",
            "name": "Image Compression Tool",
            "description": "Machine learning based image compression application"
        },
        {
            "id": "project-002",
            "name": "Plant Disease Detection",
            "description": "Computer vision application for detecting plant diseases"
        },
        {
            "id": "project-003",
            "name": "Smart Traffic Management",
            "description": "AI-based traffic violation and congestion detection system"
        },
        {
            "id": "project-004",
            "name": "AI Career Graph",
            "description": "Graph database application for career exploration"
        },
        {
            "id": "project-005",
            "name": "Support Ticket Management",
            "description": "Web application for managing support tickets"
        }
    ]

    session.run(
        """
        UNWIND $projects AS project
        MERGE (p:Project {id: project.id})
        SET p.name = project.name,
            p.description = project.description
        """,
        projects=projects
    )


def seed_technologies(session):
    technologies = [
        {"id": "tensorflow", "name": "TensorFlow"},
        {"id": "opencv", "name": "OpenCV"},
        {"id": "fastapi", "name": "FastAPI"},
        {"id": "flask", "name": "Flask"},
        {"id": "react", "name": "React"},
        {"id": "neo4j-driver", "name": "Neo4j Python Driver"},
        {"id": "mysql", "name": "MySQL"},
        {"id": "pandas", "name": "Pandas"},
        {"id": "scikit-learn", "name": "Scikit-learn"},
        {"id": "git", "name": "Git"}
    ]

    session.run(
        """
        UNWIND $technologies AS technology
        MERGE (t:Technology {id: technology.id})
        SET t.name = technology.name
        """,
        technologies=technologies
    )


def seed_learning_resources(session):
    resources = [
        {
            "id": "resource-001",
            "name": "Python Programming Course",
            "type": "Course"
        },
        {
            "id": "resource-002",
            "name": "Machine Learning Fundamentals",
            "type": "Course"
        },
        {
            "id": "resource-003",
            "name": "TensorFlow Developer Guide",
            "type": "Documentation"
        },
        {
            "id": "resource-004",
            "name": "Docker Fundamentals",
            "type": "Course"
        },
        {
            "id": "resource-005",
            "name": "AWS Cloud Practitioner",
            "type": "Course"
        }
    ]

    session.run(
        """
        UNWIND $resources AS resource
        MERGE (r:LearningResource {id: resource.id})
        SET r.name = resource.name,
            r.type = resource.type
        """,
        resources=resources
    )


def create_candidate_skills(session):
    relationships = [
        ("candidate-001", "python"),
        ("candidate-001", "sql"),
        ("candidate-001", "machine-learning"),
        ("candidate-001", "flask"),
        ("candidate-001", "javascript"),
        ("candidate-001", "react"),
        ("candidate-001", "git"),
        ("candidate-001", "data-analysis"),
        ("candidate-001", "pandas"),
        ("candidate-001", "numpy"),
        ("candidate-001", "fastapi"),
        ("candidate-002", "python"),
        ("candidate-002", "sql"),
        ("candidate-002", "java"),
        ("candidate-002", "git"),
        ("candidate-003", "python"),
        ("candidate-003", "sql"),
        ("candidate-003", "data-analysis"),
        ("candidate-003", "statistics"),
        ("candidate-003", "pandas")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (c:Candidate {id: rel[0]})
        MATCH (s:Skill {id: rel[1]})
        MERGE (c)-[:HAS_SKILL]->(s)
        """,
        relationships=relationships
    )


def create_job_skills(session):
    relationships = [
        ("job-001", "python"),
        ("job-001", "git"),
        ("job-001", "rest-api"),

        ("job-002", "python"),
        ("job-002", "machine-learning"),
        ("job-002", "tensorflow"),
        ("job-002", "docker"),
        ("job-002", "sql"),

        ("job-003", "python"),
        ("job-003", "machine-learning"),
        ("job-003", "deep-learning"),
        ("job-003", "tensorflow"),
        ("job-003", "aws"),

        ("job-004", "sql"),
        ("job-004", "python"),
        ("job-004", "data-analysis"),
        ("job-004", "pandas"),
        ("job-004", "statistics"),

        ("job-005", "python"),
        ("job-005", "sql"),
        ("job-005", "machine-learning"),
        ("job-005", "statistics"),
        ("job-005", "pandas"),

        ("job-006", "python"),
        ("job-006", "fastapi"),
        ("job-006", "rest-api"),
        ("job-006", "docker"),
        ("job-006", "git"),

        ("job-007", "python"),
        ("job-007", "computer-vision"),
        ("job-007", "tensorflow"),
        ("job-007", "opencv"),

        ("job-008", "javascript"),
        ("job-008", "react"),
        ("job-008", "python"),
        ("job-008", "rest-api")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (j:Job {id: rel[0]})
        MATCH (s:Skill {id: rel[1]})
        MERGE (j)-[:REQUIRES]->(s)
        """,
        relationships=relationships
    )


def create_company_jobs(session):
    relationships = [
        ("company-001", "job-001"),
        ("company-001", "job-008"),
        ("company-002", "job-004"),
        ("company-002", "job-005"),
        ("company-003", "job-002"),
        ("company-003", "job-003"),
        ("company-004", "job-006"),
        ("company-005", "job-007")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (c:Company {id: rel[0]})
        MATCH (j:Job {id: rel[1]})
        MERGE (c)-[:OFFERS]->(j)
        """,
        relationships=relationships
    )


def create_skill_relationships(session):
    relationships = [
        ("python", "machine-learning"),
        ("machine-learning", "deep-learning"),
        ("machine-learning", "data-analysis"),
        ("deep-learning", "tensorflow"),
        ("deep-learning", "pytorch"),
        ("computer-vision", "machine-learning"),
        ("nlp", "machine-learning"),
        ("data-analysis", "pandas"),
        ("data-analysis", "statistics"),
        ("fastapi", "rest-api"),
        ("flask", "rest-api"),
        ("javascript", "react"),
        ("python", "pandas"),
        ("python", "numpy")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (s1:Skill {id: rel[0]})
        MATCH (s2:Skill {id: rel[1]})
        MERGE (s1)-[:RELATED_TO]->(s2)
        MERGE (s2)-[:RELATED_TO]->(s1)
        """,
        relationships=relationships
    )


def create_projects(session):
    relationships = [
        ("candidate-001", "project-001"),
        ("candidate-001", "project-002"),
        ("candidate-001", "project-003"),
        ("candidate-001", "project-004"),
        ("candidate-001", "project-005")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (c:Candidate {id: rel[0]})
        MATCH (p:Project {id: rel[1]})
        MERGE (c)-[:BUILT]->(p)
        """,
        relationships=relationships
    )


def connect_projects_to_technologies(session):
    relationships = [
        ("project-001", "tensorflow"),
        ("project-001", "scikit-learn"),
        ("project-001", "python"),

        ("project-002", "tensorflow"),
        ("project-002", "opencv"),
        ("project-002", "python"),

        ("project-003", "opencv"),
        ("project-003", "tensorflow"),
        ("project-003", "python"),

        ("project-004", "fastapi"),
        ("project-004", "react"),
        ("project-004", "neo4j-driver"),
        ("project-004", "python"),

        ("project-005", "flask"),
        ("project-005", "mysql"),
        ("project-005", "python")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (p:Project {id: rel[0]})
        MATCH (t:Technology {id: rel[1]})
        MERGE (p)-[:USES]->(t)
        """,
        relationships=relationships
    )


def connect_projects_to_skills(session):
    relationships = [
        ("project-001", "machine-learning"),
        ("project-001", "python"),

        ("project-002", "computer-vision"),
        ("project-002", "machine-learning"),
        ("project-002", "python"),

        ("project-003", "computer-vision"),
        ("project-003", "machine-learning"),
        ("project-003", "python"),

        ("project-004", "python"),
        ("project-004", "rest-api"),

        ("project-005", "python"),
        ("project-005", "sql"),
        ("project-005", "rest-api")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (p:Project {id: rel[0]})
        MATCH (s:Skill {id: rel[1]})
        MERGE (p)-[:DEMONSTRATES]->(s)
        """,
        relationships=relationships
    )


def connect_skills_to_resources(session):
    relationships = [
        ("python", "resource-001"),
        ("machine-learning", "resource-002"),
        ("tensorflow", "resource-003"),
        ("docker", "resource-004"),
        ("aws", "resource-005")
    ]

    session.run(
        """
        UNWIND $relationships AS rel
        MATCH (s:Skill {id: rel[0]})
        MATCH (r:LearningResource {id: rel[1]})
        MERGE (s)-[:LEARNED_THROUGH]->(r)
        """,
        relationships=relationships
    )


def main():
    print("Connecting to CognoDB...")

    try:
        driver.verify_connectivity()
        print("Connected successfully.")

        with driver.session() as session:

            print("Creating constraints...")
            create_constraints(session)

            print("Creating candidates...")
            seed_candidates(session)

            print("Creating skills...")
            seed_skills(session)

            print("Creating companies...")
            seed_companies(session)

            print("Creating jobs...")
            seed_jobs(session)

            print("Creating projects...")
            seed_projects(session)

            print("Creating technologies...")
            seed_technologies(session)

            print("Creating learning resources...")
            seed_learning_resources(session)

            print("Creating candidate-skill relationships...")
            create_candidate_skills(session)

            print("Creating job-skill relationships...")
            create_job_skills(session)

            print("Creating company-job relationships...")
            create_company_jobs(session)

            print("Creating skill relationships...")
            create_skill_relationships(session)

            print("Creating candidate-project relationships...")
            create_projects(session)

            print("Connecting projects to technologies...")
            connect_projects_to_technologies(session)

            print("Connecting projects to skills...")
            connect_projects_to_skills(session)

            print("Connecting skills to learning resources...")
            connect_skills_to_resources(session)

        print()
        print("======================================")
        print("GRAPH DATABASE SEEDED SUCCESSFULLY!")
        print("======================================")

    except Exception as e:
        print("ERROR:", e)

    finally:
        driver.close()


if __name__ == "__main__":
    main()