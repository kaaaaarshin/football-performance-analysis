function DashboardStats() {

  return (

    <div
      style={{
        display: "flex",
        justifyContent: "center",
        gap: "20px",
        marginTop: "20px",
        marginBottom: "40px",
        flexWrap: "wrap"
      }}
    >

      <div
        style={{
          background: "#1E293B",
          padding: "20px",
          borderRadius: "12px",
          width: "150px",
          textAlign: "center",
          boxShadow:
            "0 4px 12px rgba(0,0,0,0.3)"
        }}
      >
        <h2>539</h2>
        <p>Players</p>
      </div>

      <div
        style={{
          background: "#1E293B",
          padding: "20px",
          borderRadius: "12px",
          width: "150px",
          textAlign: "center",
          boxShadow:
            "0 4px 12px rgba(0,0,0,0.3)"
        }}
      >
        <h2>5</h2>
        <p>Roles</p>
      </div>

      <div
        style={{
          background: "#1E293B",
          padding: "20px",
          borderRadius: "12px",
          width: "150px",
          textAlign: "center",
          boxShadow:
            "0 4px 12px rgba(0,0,0,0.3)"
        }}
      >
        <h2>5</h2>
        <p>Clusters</p>
      </div>

      <div
        style={{
          background: "#1E293B",
          padding: "20px",
          borderRadius: "12px",
          width: "200px",
          textAlign: "center",
          boxShadow:
            "0 4px 12px rgba(0,0,0,0.3)"
        }}
      >
        <h2>LaLiga</h2>
        <p>2015-16 Dataset</p>
      </div>

    </div>

  );

}

export default DashboardStats;