import React from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

const ResultFeedback = ({ feedback }) => {
  const barData = {
    labels: ["Strengths", "Weaknesses"],
    datasets: [
      {
        label: "Code Analysis",
        data: [feedback.strengths.length, feedback.weaknesses.length],
        backgroundColor: ["rgba(54, 162, 235, 0.2)", "rgba(255, 99, 132, 0.2)"],
        borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 99, 132, 1)"],
        borderWidth: 1,
      },
    ],
  };

  const pieData = {
    labels: ["Strengths", "Weaknesses"],
    datasets: [
      {
        data: [feedback.strengths.length, feedback.weaknesses.length],
        backgroundColor: ["rgba(54, 162, 235, 0.2)", "rgba(255, 99, 132, 0.2)"],
        borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 99, 132, 1)"],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div className="flex-1 p-8 bg-gray-50 rounded-lg shadow-inner">
      <h2 className="text-2xl font-bold text-center text-gray-700 mb-4">
        Code Analysis Feedback
      </h2>
      <div className="space-y-4">
        <div>
          <h3 className="text-xl font-semibold text-gray-800">Strengths</h3>
          <p className="text-gray-600">{feedback.strengths}</p>
        </div>
        <div>
          <h3 className="text-xl font-semibold text-gray-800">Weaknesses</h3>
          <p className="text-gray-600">{feedback.weaknesses}</p>
        </div>
        <div>
          <h3 className="text-xl font-semibold text-gray-800">
            Overall Feedback
          </h3>
          <p className="text-gray-600">{feedback.overall}</p>
        </div>
        <div className="mt-6">
          <h3 className="text-xl font-semibold text-gray-800">
            Visual Feedback
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
            <div className="h-80">
              <Bar
                data={barData}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: { legend: { display: false } },
                }}
              />
            </div>
            <div className="h-80">
              <Pie
                data={pieData}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                }}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultFeedback;
