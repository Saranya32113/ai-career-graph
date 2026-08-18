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