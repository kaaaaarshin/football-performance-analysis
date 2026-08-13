import { useEffect, useState } from "react";
import api from "../api/api";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function RoleDistribution() {

  const [data, setData] =
    useState([]);

  useEffect(() => {

    const loadRoles = async () => {

      try {

        const response =
          await api.get(
            "/role-distribution"
          );

        const chartData =
          Object.entries(
            response.data
          ).map(
            ([role, count]) => ({
              role,
              count
            })
          );

        setData(chartData);

      } catch (error) {

        console.error(error);

      }

    };

    loadRoles();

  }, []);

  return (

    <div
      style={{
        marginTop: "40px"
      }}
    >

      <h2>
        Role Distribution
      </h2>

      <ResponsiveContainer
        width="100%"
        height={400}
      >

        <BarChart data={data}>

          <CartesianGrid />

          <XAxis
            dataKey="role"
          />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="count"
          />

        </BarChart>

      </ResponsiveContainer>

    </div>

  );

}

export default RoleDistribution;