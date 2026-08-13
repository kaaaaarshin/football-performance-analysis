import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
  Legend
} from "recharts";

function RadarComparison({ comparison }) {

  if (!comparison) return null;

const stats = [
  {
    key: "goals",
    label: "Goals"
  },
  {
    key: "shots",
    label: "Shots"
  },
  {
    key: "pass_accuracy",
    label: "Pass %"
  },
  {
    key: "dribbles",
    label: "Dribbles"
  },
  {
    key: "pressures",
    label: "Pressures"
  },
  {
    key: "interceptions",
    label: "Interceptions"
  }
];

const data = stats.map((stat) => {

  const p1 =
    comparison.player1[stat.key];

  const p2 =
    comparison.player2[stat.key];

  const max =
    Math.max(p1, p2);

  return {

    stat: stat.label,

    Player1:
      max === 0
        ? 0
        : (p1 / max) * 100,

    Player2:
      max === 0
        ? 0
        : (p2 / max) * 100

  };

});
  return (

    <div
      style={{
        width: "100%",
        height: 500
      }}
    >

      <h3>
        Radar Comparison
      </h3>

      <ResponsiveContainer>

        <RadarChart data={data}>

          <PolarGrid />

          <PolarAngleAxis
            dataKey="stat"
          />

          <PolarRadiusAxis
            domain={[0, 100]}
        />

          <Radar
            name={comparison.player1.player}
            dataKey="Player1"
            stroke="#3B82F6"
            fill="#3B82F6"
            fillOpacity={0.35}
        />

        <Radar
            name={comparison.player2.player}
            dataKey="Player2"
            stroke="#EF4444"
            fill="#EF4444"
            fillOpacity={0.35}
        />

          <Legend />

        </RadarChart>

      </ResponsiveContainer>

    </div>

  );
}

export default RadarComparison;