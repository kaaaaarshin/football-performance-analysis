function SimilarPlayers({
  similarPlayers,
  onPlayerClick
}) {

  if (
    similarPlayers.length === 0
  )
    return null;

  return (

    <div
      style={{
        marginTop: "25px",
        marginBottom: "25px"
      }}
    >

      <h2>
        Similar Players
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit, minmax(220px, 1fr))",
          gap: "15px"
        }}
      >

        {similarPlayers.map(
          (player, index) => (

            <div
              key={index}
              onClick={() =>
                onPlayerClick(
                  player.player
                )
              }
              style={{
                background: "#1E293B",
                padding: "20px",
                borderRadius: "12px",
                cursor: "pointer",
                boxShadow:
                  "0 4px 12px rgba(0,0,0,0.3)",
                transition:
                  "transform 0.2s ease"
              }}
            >

              <h3>
                {player.player}
              </h3>

              <p
                style={{
                  color: "#94A3B8"
                }}
              >
                Similarity Score
              </p>

              <h2
                style={{
                  color: "#22C55E"
                }}
              >
                {player.similarity}%
              </h2>

            </div>

          )
        )}

      </div>

    </div>

  );

}

export default SimilarPlayers;