import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/api";

function App() {
  const [candidate, setCandidate] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [skillGap, setSkillGap] = useState([]);
  const [selectedJob, setSelectedJob] = useState("job-002");
  const [loading, setLoading] = useState(true);
  const [gapLoading, setGapLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    loadDashboard();
  }, []);

  useEffect(() => {
    if (selectedJob) {
      loadSkillGap(selectedJob);
    }
  }, [selectedJob]);

  async function loadDashboard() {
    try {
      setLoading(true);
      setError("");

      const [candidateRes, jobsRes, recommendationsRes] =
        await Promise.all([
          axios.get(`${API_URL}/candidates/candidate-001`),
          axios.get(`${API_URL}/jobs`),
          axios.get(`${API_URL}/recommendations/candidate-001`),
        ]);

      setCandidate(candidateRes.data);
      setJobs(jobsRes.data);
      setRecommendations(recommendationsRes.data);

      if (jobsRes.data.length > 0) {
        setSelectedJob(jobsRes.data[0].id);
      }
    } catch (err) {
      console.error(err);
      setError(
        "Unable to connect to the Career Graph. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  }

  async function loadSkillGap(jobId) {
    try {
      setGapLoading(true);

      const response = await axios.get(
        `${API_URL}/skill-gap/candidate-001/${jobId}`
      );

      setSkillGap(response.data);
    } catch (err) {
      console.error(err);
      setSkillGap([]);
    } finally {
      setGapLoading(false);
    }
  }

  const selectedJobData = jobs.find(
    (job) => job.id === selectedJob
  );

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loader"></div>
        <h2>Loading Career Graph</h2>
        <p>Connecting to CognoDB...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-screen">
        <div className="error-card">
          <div className="error-icon">!</div>
          <h2>Connection unavailable</h2>
          <p>{error}</p>
          <button onClick={loadDashboard}>
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="app">

      <header className="header">
        <div className="brand">
          <div className="brand-icon">AI</div>

          <div>
            <h1>Career Graph</h1>
            <p>Graph-powered career intelligence</p>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          CognoDB Connected
        </div>
      </header>

      <main className="container">

        <section className="hero">
          <div>
            <span className="eyebrow">
              CAREER PROFILE
            </span>

            <h2>
              Welcome, {candidate?.name}
            </h2>

            <p>
              Explore your skills, discover relevant jobs and
              identify the skills that can move your career forward.
            </p>
          </div>

          <div className="profile-card">
            <div className="avatar">
              {candidate?.name?.charAt(0)}
            </div>

            <div>
              <strong>{candidate?.name}</strong>
              <span>{candidate?.education}</span>
            </div>
          </div>
        </section>

        <section className="stats">

          <div className="stat-card">
            <span className="stat-label">
              Skills
            </span>

            <strong>
              {candidate?.skills?.length || 0}
            </strong>

            <span className="stat-description">
              Skills in your graph
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">
              Projects
            </span>

            <strong>
              {candidate?.projects?.length || 0}
            </strong>

            <span className="stat-description">
              Projects you've built
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">
              Jobs
            </span>

            <strong>
              {jobs.length}
            </strong>

            <span className="stat-description">
              Roles in the graph
            </span>
          </div>

          <div className="stat-card">
            <span className="stat-label">
              Recommendations
            </span>

            <strong>
              {recommendations.length}
            </strong>

            <span className="stat-description">
              Graph-based matches
            </span>
          </div>

        </section>

        <section className="grid">

          <div className="panel">
            <div className="panel-header">
              <div>
                <span className="eyebrow">
                  YOUR PROFILE
                </span>

                <h3>Skills</h3>
              </div>
            </div>

            <div className="skill-list">
              {candidate?.skills?.length > 0 ? (
                candidate.skills.map((skill) => (
                  <span
                    className="skill-tag"
                    key={skill}
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="empty">
                  No skills found.
                </p>
              )}
            </div>
          </div>

          <div className="panel">
            <div className="panel-header">
              <div>
                <span className="eyebrow">
                  EXPERIENCE
                </span>

                <h3>Projects</h3>
              </div>
            </div>

            <div className="project-list">
              {candidate?.projects?.length > 0 ? (
                candidate.projects.map((project) => (
                  <div
                    className="project-item"
                    key={project}
                  >
                    <div className="project-icon">
                      ↗
                    </div>

                    <span>{project}</span>
                  </div>
                ))
              ) : (
                <p className="empty">
                  No projects found.
                </p>
              )}
            </div>
          </div>

        </section>

        <section className="panel recommendations">

          <div className="panel-header">
            <div>
              <span className="eyebrow">
                GRAPH INSIGHT
              </span>

              <h3>
                Recommended Career Paths
              </h3>

              <p>
                Roles discovered through connected skills
                and job requirements.
              </p>
            </div>
          </div>

          {recommendations.length > 0 ? (
            <div className="job-grid">

              {recommendations.slice(0, 8).map((job) => (
                <div
                  className="job-card"
                  key={job.id}
                >

                  <div className="job-top">
                    <div className="job-icon">
                      {job.title.charAt(0)}
                    </div>

                    <span className="match">
                      Graph Match
                    </span>
                  </div>

                  <h4>{job.title}</h4>

                  <p>{job.company}</p>

                  <div className="path-skills">
                    {job.matched_path_skills
                      ?.slice(0, 3)
                      .map((skill) => (
                        <span key={skill}>
                          {skill}
                        </span>
                      ))}
                  </div>

                </div>
              ))}

            </div>
          ) : (
            <div className="empty-state">
              No recommendations available.
            </div>
          )}

        </section>

        <section className="panel skill-gap-panel">

          <div className="panel-header gap-header">

            <div>
              <span className="eyebrow">
                NEXT STEP
              </span>

              <h3>
                Skill Gap Analysis
              </h3>

              <p>
                Compare your current skills with the
                requirements of a target role.
              </p>
            </div>

            <select
              value={selectedJob}
              onChange={(event) =>
                setSelectedJob(event.target.value)
              }
            >
              {jobs.map((job) => (
                <option
                  key={job.id}
                  value={job.id}
                >
                  {job.title}
                </option>
              ))}
            </select>

          </div>

          {selectedJobData && (
            <div className="target-job">
              <strong>
                {selectedJobData.title}
              </strong>

              <span>
                {selectedJobData.company}
              </span>
            </div>
          )}

          {gapLoading ? (
            <div className="gap-loading">
              Analyzing graph relationships...
            </div>
          ) : (
            <div className="gap-list">

              {skillGap.map((item) => (
                <div
                  className="gap-item"
                  key={item.skill}
                >

                  <div className="gap-skill">

                    <span
                      className={
                        item.has_skill
                          ? "check"
                          : "missing"
                      }
                    >
                      {item.has_skill ? "✓" : "!"}
                    </span>

                    <span>
                      {item.skill}
                    </span>

                  </div>

                  <span
                    className={
                      item.has_skill
                        ? "ready"
                        : "learn"
                    }
                  >
                    {item.has_skill
                      ? "Already have"
                      : "Learn this"}
                  </span>

                </div>
              ))}

            </div>
          )}

        </section>

        <footer>
          <span>AI Career Graph</span>

          <span>
            Powered by CognoDB + FastAPI + React
          </span>
        </footer>

      </main>

    </div>
  );
}

export default App;