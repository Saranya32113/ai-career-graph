from app.database import db


def get_candidate(candidate_id):

    query = """
    MATCH (c:Candidate {id: $candidate_id})

    OPTIONAL MATCH (c)-[:HAS_SKILL]->(s:Skill)

    OPTIONAL MATCH (c)-[:BUILT]->(p:Project)

    RETURN
        c.id AS id,
        c.name AS name,
        c.education AS education,
        collect(DISTINCT s.name) AS skills,
        collect(DISTINCT p.name) AS projects
    """

    with db.driver.session() as session:

        result = session.run(
            query,
            candidate_id=candidate_id
        )

        record = result.single()

        if not record:
            return None

        return dict(record)


def get_jobs():

    query = """
    MATCH (company:Company)-[:OFFERS]->(job:Job)

    OPTIONAL MATCH (job)-[:REQUIRES]->(skill:Skill)

    RETURN
        job.id AS id,
        job.title AS title,
        job.level AS level,
        company.name AS company,
        collect(DISTINCT skill.name) AS required_skills

    ORDER BY job.title
    """

    with db.driver.session() as session:

        result = session.run(query)

        return [dict(record) for record in result]


def get_skill_gap(candidate_id, job_id):

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

    with db.driver.session() as session:

        result = session.run(
            query,
            candidate_id=candidate_id,
            job_id=job_id
        )

        return [dict(record) for record in result]


def get_recommendations(candidate_id):

    query = """
    MATCH (c:Candidate {id: $candidate_id})
          -[:HAS_SKILL]->(s1:Skill)
          -[:RELATED_TO]->(s2:Skill)
          <-[:REQUIRES]-(j:Job)

    MATCH (company:Company)-[:OFFERS]->(j)

    RETURN DISTINCT
        j.id AS id,
        j.title AS title,
        company.name AS company,
        collect(DISTINCT s2.name) AS matched_path_skills

    ORDER BY title
    """

    with db.driver.session() as session:

        result = session.run(
            query,
            candidate_id=candidate_id
        )

        return [dict(record) for record in result]