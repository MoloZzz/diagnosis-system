import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import type { DiagnosisResult } from "../types";

const ResultPage: React.FC = () => {
  const { state } = useLocation();
  const navigate = useNavigate();
  // Try to get results from state or localStorage
  const result = (state?.result as DiagnosisResult | undefined) ||
    (localStorage.getItem("diagnosisResults")
      ? JSON.parse(localStorage.getItem("diagnosisResults")!)
      : undefined);

  console.log("Result data:", result);

  if (!result || Object.keys(result).length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="bg-white p-6 rounded-2xl shadow w-full max-w-md text-center">
          <p className="text-red-500 mb-4">
            No results available. Please complete the survey first.
          </p>
          <button
            onClick={() => navigate("/survey")}
            className="bg-blue-600 text-white rounded-full py-2 px-4 font-semibold hover:bg-blue-700"
          >
            Go to Survey
          </button>
        </div>
      </div>
    );
  }

  // Filter results to show only probabilities > 1%
  const filteredResults = Object.fromEntries(
    Object.entries(result).filter(([_, value]) => value > 0.01)
  );

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-2xl shadow w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-4 flex items-center justify-center gap-2">
          <span role="img" aria-label="brain">🧠</span> Fuzzy Diagnosis
        </h1>
        <h2 className="text-lg font-semibold mb-4 text-center">Diagnosis Results</h2>
        {Object.keys(filteredResults).length === 0 ? (
          <p className="text-center text-gray-500">No significant diagnosis results to display.</p>
        ) : (
          <ul className="space-y-2 mb-6">
            {Object.entries(filteredResults).map(([disease, value]) => (
              <li
                key={disease}
                className="flex justify-between border-b border-gray-200 pb-2"
              >
                <span className="capitalize">{disease.replace(/_/g, " ")}</span>
                <span className="font-semibold text-blue-600">{(value * 100).toFixed(2)}%</span>
              </li>
            ))}
          </ul>
        )}
        <button
          onClick={() => navigate("/survey")}
          className="mt-6 w-full bg-blue-600 text-white rounded-full py-2 font-semibold hover:bg-blue-700"
        >
          Back to Survey
        </button>
      </div>
    </div>
  );
};

export default ResultPage;