function App() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #0f172a, #1e293b, #111827)",
        color: "white",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial, sans-serif",
        padding: "20px",
      }}
    >
      <div
        style={{
          textAlign: "center",
          background: "rgba(255,255,255,0.08)",
          padding: "50px",
          borderRadius: "20px",
          backdropFilter: "blur(10px)",
          boxShadow: "0 8px 30px rgba(0,0,0,0.4)",
          maxWidth: "700px",
          width: "100%",
        }}
      >
        <h1
          style={{
            fontSize: "3rem",
            marginBottom: "20px",
            color: "#38bdf8",
          }}
        >
          🚀 DevOps CI/CD Portfolio
        </h1>

        <p
          style={{
            fontSize: "1.2rem",
            color: "#cbd5e1",
            lineHeight: "1.8",
          }}
        >
          Successfully deployed using{" "}
          <span style={{ color: "#22c55e", fontWeight: "bold" }}>
            Jenkins
          </span>
          ,{" "}
          <span style={{ color: "#f97316", fontWeight: "bold" }}>
            Docker
          </span>
          ,{" "}
          <span style={{ color: "#eab308", fontWeight: "bold" }}>
            GitHub
          </span>{" "}
          and{" "}
          <span style={{ color: "#a855f7", fontWeight: "bold" }}>
            AWS EC2
          </span>
          .
        </p>

        <div
          style={{
            marginTop: "35px",
            display: "flex",
            justifyContent: "center",
            gap: "15px",
            flexWrap: "wrap",
          }}
        >
          {["React", "Docker", "Jenkins", "AWS", "CI/CD"].map((tech) => (
            <span
              key={tech}
              style={{
                background: "#1e293b",
                padding: "12px 20px",
                borderRadius: "999px",
                border: "1px solid #334155",
                fontSize: "0.95rem",
                transition: "0.3s",
              }}
            >
              {tech}
            </span>
          ))}
        </div>

        <button
          style={{
            marginTop: "40px",
            padding: "14px 30px",
            border: "none",
            borderRadius: "10px",
            background: "#38bdf8",
            color: "#0f172a",
            fontSize: "1rem",
            fontWeight: "bold",
            cursor: "pointer",
            boxShadow: "0 4px 15px rgba(56,189,248,0.4)",
          }}
        >
          Frontend Service Running Succesfully by Jenkins Pipeline (by Agent)⚡
        </button>
      </div>
    </div>
  )
}

export default App
