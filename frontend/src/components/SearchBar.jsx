function SearchBar({
  search,
  handleSearch,
  matches,
  selectPlayer
}) {

  return (

    <div
      style={{
        marginTop: "30px",
        marginBottom: "30px",
        textAlign: "center"
      }}
    >

      <h2
        style={{
          marginBottom: "20px"
        }}
      >
        🔍 Player Search
      </h2>

      <div
        style={{
          position: "relative",
          width: "600px",
          margin: "0 auto"
        }}
      >

        <input
          type="text"
          value={search}
          placeholder="Search Messi, Ronaldo, Neymar..."
          onChange={(e) =>
            handleSearch(
              e.target.value
            )
          }
          style={{
            width: "100%",
            padding: "16px",
            borderRadius: "12px",
            border: "2px solid #334155",
            background: "#0F172A",
            color: "white",
            fontSize: "16px",
            outline: "none",
            boxSizing: "border-box"
          }}
        />

        {

          matches.length > 0 && (

            <div
              style={{
                position: "absolute",
                top: "100%",
                left: 0,
                right: 0,
                background: "#1E293B",
                borderRadius: "12px",
                marginTop: "8px",
                overflow: "hidden",
                boxShadow:
                  "0 8px 20px rgba(0,0,0,0.4)",
                zIndex: 1000,
                textAlign: "left",
                maxHeight: "300px",
                overflowY: "auto"
              }}
            >

              {matches.map(
                (player) => (

                  <div
                    key={player}
                    onClick={() =>
                      selectPlayer(
                        player
                      )
                    }
                    style={{
                      padding: "14px 18px",
                      cursor: "pointer",
                      borderBottom:
                        "1px solid #334155"
                    }}
                  >
                    ⚽ {player}
                  </div>

                )
              )}

            </div>

          )

        }

      </div>

      <p
        style={{
          color: "#94A3B8",
          marginTop: "10px",
          fontSize: "14px"
        }}
      >
        Search any player from the LaLiga 2015-16 dataset
      </p>

    </div>

  );

}

export default SearchBar;