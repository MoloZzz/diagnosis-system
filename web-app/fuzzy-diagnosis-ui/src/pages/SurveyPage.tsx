import React, { useEffect, useState } from "react";
import { getSymptoms, getDiagnosis } from "../api";
import type { DiagnosisResult } from "../types";

const SurveyPage: React.FC = () => {
  const [allSymptoms, setAllSymptoms] = useState<string[]>([]);
  const [form, setForm] = useState<Record<string, string>>({});
  const [results, setResults] = useState<DiagnosisResult | null>(null);

  useEffect(() => {
    getSymptoms().then((res) => setAllSymptoms(res.data));
  }, []);

  const handleChange = (symptom: string, value: string) => {
    setForm((prev) => ({ ...prev, [symptom]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const filtered = Object.fromEntries(
      Object.entries(form).filter(([_, v]) => v !== "")
    );
    const res = await getDiagnosis(filtered);
    setResults(res.data);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4">
      <div className="max-w-md mx-auto bg-white p-6 rounded-2xl shadow">
        <h1 className="text-2xl font-bold text-center mb-6 flex items-center justify-center gap-2">
          <span role="img" aria-label="brain">🧠</span> Fuzzy Diagnosis
        </h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          {allSymptoms.map((symptom) => (
            <div key={symptom} className="flex justify-between items-center">
              <span className="capitalize text-gray-700 font-medium">
                {symptom.replace(/_/g, " ")}
              </span>
              <select
                value={form[symptom] || ""}
                onChange={(e) => handleChange(symptom, e.target.value)}
                className="border rounded px-2 py-1"
              >
                <option value="">-</option>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </select>
            </div>
          ))}
          <button
            type="submit"
            className="w-full bg-blue-600 text-white rounded-full py-2 font-semibold hover:bg-blue-700"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default SurveyPage;