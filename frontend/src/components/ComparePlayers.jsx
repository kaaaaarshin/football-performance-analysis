import { useState } from "react";
import api from "../api/api";

import RadarComparison from "./RadarComparision";

function ComparePlayers() {

  const [search1, setSearch1] = useState("");
  const [search2, setSearch2] = useState("");

  const [matches1, setMatches1] = useState([]);
  const [matches2, setMatches2] = useState([]);

  const [player1, setPlayer1] = useState("");
  const [player2, setPlayer2] = useState("");

  const [comparison, setComparison] =
    useState(null);

  const winnerStyle = {
    color: "#22C55E",
    fontWeight: "bold"
  };

  const renderStatRow = (
    label,
    stat
  ) => {

    const p1 =
      comparison.player1[stat];

    const p2 =
      comparison.player2[stat];

    return (

      <tr
        style={{
          textAlign: "center"
        }}
      >

        <td
          style={{
            padding: "18px",
            background: "#0F172A"
          }}
        >
          {label}
        </td>

        <td
          style={{
            padding: "18px",
            ...(p1 > p2
              ? winnerStyle
              : {})
          }}
        >
          {p1 > p2 && "🏆 "}
          {p1}
        </td>

        <td
          style={{
            padding: "18px",
            ...(p2 > p1
              ? winnerStyle
              : {})
          }}
        >
          {p2 > p1 && "🏆 "}
          {p2}
        </td>

      </tr>

    );

  };

  const handleSearch1 = async (value) => {

    setSearch1(value);

    if (value.length < 2) {

      setMatches1([]);
      return;

    }

    try {

      const response =
        await api.get(
          `/search/${value}`
        );

      setMatches1(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  const handleSearch2 = async (value) => {

    setSearch2(value);

    if (value.length < 2) {

      setMatches2([]);
      return;

    }

    try {

      const response =
        await api.get(
          `/search/${value}`
        );

      setMatches2(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  const compare = async () => {

    if (!player1 || !player2)
      return;

    try {

      const response =
        await api.get(
          `/compare/${player1}/${player2}`
        );

      setComparison(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <div
      style={{
        background: "#1E293B",
        padding: "30px",
        borderRadius: "16px",
        marginTop: "30px",
        boxShadow:
          "0 8px 24px rgba(0,0,0,0.35)"
      }}
    >

      <h2
        style={{
          textAlign: "center",
          marginBottom: "25px"
        }}
      >
        Compare Players
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "1fr 1fr",
          gap: "20px"
        }}
      >

        <div>

          <input
            type="text"
            placeholder="Search Player 1"
            value={search1}
            onChange={(e) =>
              handleSearch1(
                e.target.value
              )
            }
            style={{
              width: "100%",
              padding: "14px",
              borderRadius: "10px",
              border: "none",
              background: "#0F172A",
              color: "white"
            }}
          />

          {matches1.length > 0 && (

            <div
              style={{
                background: "#0F172A",
                borderRadius: "10px",
                marginTop: "8px"
              }}
            >

              {matches1.map(
                (player) => (

                  <div
                    key={player}
                    style={{
                      padding: "10px",
                      cursor: "pointer"
                    }}
                    onClick={() => {

                      setPlayer1(
                        player
                      );

                      setSearch1(
                        player
                      );

                      setMatches1([]);

                    }}
                  >
                    {player}
                  </div>

                )
              )}

            </div>

          )}

        </div>

        <div>

          <input
            type="text"
            placeholder="Search Player 2"
            value={search2}
            onChange={(e) =>
              handleSearch2(
                e.target.value
              )
            }
            style={{
              width: "100%",
              padding: "14px",
              borderRadius: "10px",
              border: "none",
              background: "#0F172A",
              color: "white"
            }}
          />

          {matches2.length > 0 && (

            <div
              style={{
                background: "#0F172A",
                borderRadius: "10px",
                marginTop: "8px"
              }}
            >

              {matches2.map(
                (player) => (

                  <div
                    key={player}
                    style={{
                      padding: "10px",
                      cursor: "pointer"
                    }}
                    onClick={() => {

                      setPlayer2(
                        player
                      );

                      setSearch2(
                        player
                      );

                      setMatches2([]);

                    }}
                  >
                    {player}
                  </div>

                )
              )}

            </div>

          )}

        </div>

      </div>

      <div
        style={{
          textAlign: "center",
          marginTop: "25px"
        }}
      >

        <button
          onClick={compare}
          style={{
            background: "#38BDF8",
            border: "none",
            padding: "14px 28px",
            borderRadius: "10px",
            fontWeight: "bold",
            fontSize: "16px",
            cursor: "pointer"
          }}
        >
          Compare Players
        </button>

      </div>

      {comparison && (

        <div>

          <h2
            style={{
              textAlign: "center",
              marginTop: "40px"
            }}
          >
            Comparison
          </h2>

          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              gap: "30px",
              flexWrap: "wrap",
              marginTop: "25px",
              marginBottom: "35px"
            }}
          >

            <div
              style={{
                background: "#0F172A",
                padding: "20px",
                borderRadius: "12px",
                minWidth: "260px",
                textAlign: "center"
              }}
            >
              <h3>
                {comparison.player1.player}
              </h3>

              <p>
                Role: {comparison.player1.role}
              </p>

              <p>
                Cluster: {comparison.player1.cluster}
              </p>
            </div>

            <h1>
              VS
            </h1>

            <div
              style={{
                background: "#0F172A",
                padding: "20px",
                borderRadius: "12px",
                minWidth: "260px",
                textAlign: "center"
              }}
            >
              <h3>
                {comparison.player2.player}
              </h3>

              <p>
                Role: {comparison.player2.role}
              </p>

              <p>
                Cluster: {comparison.player2.cluster}
              </p>
            </div>

          </div>

          <table
            style={{
              width: "80%",
              margin: "0 auto",
              borderCollapse: "collapse"
            }}
          >

            <thead>

              <tr>

                <th
                  style={{
                    padding: "18px",
                    background: "#0F172A"
                  }}
                >
                  Stat
                </th>

                <th
                  style={{
                    padding: "18px",
                    background: "#0F172A"
                  }}
                >
                  {
                    comparison.player1.player
                      .split(" ")
                      .slice(0, 2)
                      .join(" ")
                  }
                </th>

                <th
                  style={{
                    padding: "18px",
                    background: "#0F172A"
                  }}
                >
                  {
                    comparison.player2.player
                      .split(" ")
                      .slice(0, 2)
                      .join(" ")
                  }
                </th>

              </tr>

            </thead>

            <tbody>

              {renderStatRow("Goals", "goals")}
              {renderStatRow("Shots", "shots")}
              {renderStatRow("Pass Accuracy", "pass_accuracy")}
              {renderStatRow("Dribbles", "dribbles")}
              {renderStatRow("Interceptions", "interceptions")}
              {renderStatRow("Pressures", "pressures")}

            </tbody>

          </table>

          <div
            style={{
              marginTop: "40px",
              background: "#0F172A",
              borderRadius: "12px",
              padding: "20px"
            }}
          >

            <h3
              style={{
                textAlign: "center"
              }}
            >
              Performance Radar
            </h3>

            <RadarComparison
              comparison={comparison}
            />

          </div>

        </div>

      )}

    </div>

  );

}

export default ComparePlayers;