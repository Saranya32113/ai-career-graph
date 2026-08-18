from fastapi import APIRouter, HTTPException

from app.database import db
from app.services.graph_service import (
    get_candidate,
    get_jobs,
    get_skill_gap,
    get_recommendations
)


router = APIRouter()


@router.get("/health")
def health():

    try:

        db.verify_connection()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:

        return {
            "status": "unhealthy",
            "database": "unreachable"
        }


@router.get("/candidates/{candidate_id}")
def candidate(candidate_id: str):

    try:

        result = get_candidate(candidate_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found"
            )

        return result

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )


@router.get("/jobs")
def jobs():

    try:

        return get_jobs()

    except Exception:

        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )


@router.get("/skill-gap/{candidate_id}/{job_id}")
def skill_gap(
    candidate_id: str,
    job_id: str
):

    try:

        return get_skill_gap(
            candidate_id,
            job_id
        )

    except Exception:

        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )


@router.get("/recommendations/{candidate_id}")
def recommendations(candidate_id: str):

    try:

        return get_recommendations(candidate_id)

    except Exception:

        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )