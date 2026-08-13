import { useState } from "react";

import api from "./api/api";

import SearchBar from "./components/SearchBar";
import PlayerCard from "./components/PlayerCard";
import SimilarPlayers from "./components/SimilarPlayers";
import ComparePlayers from "./components/ComparePlayers";
import DashboardStats from "./components/DashboardStats";
import RoleDistribution from "./components/RoleDistribution";

function App() {

  const [search, setSearch] =
    useState("");

  const [matches, setMatches] =
    useState([]);

  const [selectedPlayer,
    setSelectedPlayer] =
    useState(null);

  const [similarPlayers,
    setSimilarPlayers] =
    useState([]);

  // ==========================
  // SEARCH PLAYERS
  // ==========================

  const handleSearch =
    async (value) => {

      setSearch(value);

      if (value.length < 2) {

        setMatches([]);
        return;

      }

      try {

        const response =
          await api.get(
            `/search/${value}`
          );

        setMatches(
          response.data
        );

      } catch (error) {

        console.error(error);

      }

    };

  // ==========================
  // SELECT PLAYER
  // ==========================

  const selectPlayer =
    async (playerName) => {

      try {

        const playerResponse =
          await api.get(
            `/player/${playerName}`
          );

        setSelectedPlayer(
          playerResponse.data
        );

        const similarResponse =
          await api.get(
            `/similar/${playerName}`
          );

        setSimilarPlayers(
          similarResponse.data
        );

        setMatches([]);

        setSearch(playerName);

      } catch (error) {

        console.error(error);

      }

    };

  return (

    <div
      style={{
        maxWidth: "1400px",
        margin: "0 auto",
        padding: "30px"
      }}
    >

      {/* ========================== */}
      {/* HEADER */}
      {/* ========================== */}

      <div
        style={{
          textAlign: "center",
          marginBottom: "40px"
        }}
      >

        <h1
          style={{
            fontSize: "42px",
            marginBottom: "10px"
          }}
        >
          ⚽ Football Performance Analysis
        </h1>

        <p
          style={{
            color: "#94A3B8"
          }}
        >
          Player Similarity, Role Analysis &
          Performance Comparison Dashboard
        </p>

      </div>

      {/* ========================== */}
      {/* DASHBOARD STATS */}
      {/* ========================== */}

      <DashboardStats />

      {/* ========================== */}
      {/* ROLE DISTRIBUTION */}
      {/* ========================== */}

      <div
        style={{
          marginTop: "30px",
          marginBottom: "40px"
        }}
      >

        <RoleDistribution />

      </div>

      {/* ========================== */}
      {/* SEARCH */}
      {/* ========================== */}

      <SearchBar
        search={search}
        handleSearch={handleSearch}
        matches={matches}
        selectPlayer={selectPlayer}
      />

      {/* ========================== */}
      {/* PROFILE + SIMILAR PLAYERS */}
      {/* ========================== */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "1fr 1fr",
          gap: "25px",
          marginTop: "30px",
          marginBottom: "40px",
          alignItems: "start"
        }}
      >

        <PlayerCard
          selectedPlayer={
            selectedPlayer
          }
        />

        <SimilarPlayers
          similarPlayers={
            similarPlayers
          }
          onPlayerClick={
            selectPlayer
          }
        />

      </div>

      {/* ========================== */}
      {/* COMPARE PLAYERS */}
      {/* ========================== */}

      <ComparePlayers />

    </div>

  );

}

export default App;