function PlayerCard({
  selectedPlayer
}) {

  if (!selectedPlayer)
    return null;

  return (

    <div
      style={{
        background: "#1E293B",
        padding: "25px",
        borderRadius: "16px",
        marginTop: "25px",
        marginBottom: "25px",
        boxShadow:
          "0 6px 20px rgba(0,0,0,0.35)",
        textAlign: "center"
      }}
    >

      {/* Avatar */}

      <div
        style={{
          width: "90px",
          height: "90px",
          borderRadius: "50%",
          background: "#334155",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: "40px",
          margin: "0 auto 15px auto"
        }}
      >
        ⚽
      </div>

      {/* Player Name */}

      <h2
        style={{
          marginBottom: "5px"
        }}
      >
        {selectedPlayer.player}
      </h2>

      {/* Role Badge */}

      <span
        style={{
          background: "#0EA5E9",
          padding: "6px 14px",
          borderRadius: "20px",
          fontSize: "14px",
          fontWeight: "bold"
        }}
      >
        {selectedPlayer.role}
      </span>

      <p
        style={{
          marginTop: "15px",
          color: "#94A3B8"
        }}
      >
        Cluster {selectedPlayer.cluster}
      </p>

      {/* Stats Grid */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(3, 1fr)",
          gap: "15px",
          marginTop: "25px"
        }}
      >

        <div
          style={{
            background: "#0F172A",
            padding: "15px",
            borderRadius: "10px"
          }}
        >
          <h3>
            {selectedPlayer.goals}
          </h3>

          <p>
            Goals
          </p>
        </div>

        <div
          style={{
            background: "#0F172A",
            padding: "15px",
            borderRadius: "10px"
          }}
        >
          <h3>
            {selectedPlayer.pass_accuracy}
          </h3>

          <p>
            Pass %
          </p>
        </div>

        <div
          style={{
            background: "#0F172A",
            padding: "15px",
            borderRadius: "10px"
          }}
        >
          <h3>
            {selectedPlayer.dribbles}
          </h3>

          <p>
            Dribbles
          </p>
        </div>

      </div>

      {/* Scouting Tag */}

      <div
        style={{
          marginTop: "25px"
        }}
      >

        <span
          style={{
            background: "#16A34A",
            padding: "8px 16px",
            borderRadius: "20px",
            fontWeight: "bold"
          }}
        >
          Scouting Profile
        </span>

      </div>

    </div>

  );

}

export default PlayerCard;