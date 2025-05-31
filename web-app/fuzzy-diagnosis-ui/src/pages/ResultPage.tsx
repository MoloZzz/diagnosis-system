import React from "react";
import type { DiagnosisResult } from "../types";

interface Props {
  result: DiagnosisResult;
}

const ResultPage: React.FC<Props> = ({ result }) => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="bg-white p-6 rounded-2xl shadow w-full max-w-sm">
        <h1 className="text-2xl font-bold text-center mb-4 flex items-center justify-center gap-2">
          <span role="img" aria-label="brain">🧠</span> Fuzzy Diagnosis
        </h1>
        <h2 className="text-lg font-semibold mb-4 text-center">Diagnosis Result</h2>
        <ul className="space-y-2">
          {Object.entries(result).map(([disease, value]) => (
            <li
              key={disease}
              className="flex justify-between border-b border-gray-200 pb-1"
            >
              <span className="capitalize">{disease}</span>
              <span className="font-semibold text-blue-600">{value.toFixed(0)}%</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ResultPage;
