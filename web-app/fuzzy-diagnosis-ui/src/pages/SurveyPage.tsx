import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getSymptoms, getDiagnosis } from "../api";

const SurveyPage: React.FC = () => {
  const [allSymptoms, setSymptoms] = useState<string[]>([]);
  const [form, setForm] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    getSymptoms()
      .then((res) => {
        console.log("Symptoms loaded:", res.data);
        setSymptoms(res.data);
      })
      .catch((err) => {
        console.error("Error fetching symptoms:", err);
        setError(
          err.response?.data?.error ||
          err.message === "Network Error"
            ? "Cannot connect to the backend. Is the server running on http://localhost:5000?"
            : `Failed to load symptoms: ${err.message}`
        );
      })
      .finally(() => setLoading(false));
  }, []);

  const handleChange = (symptom: string, value: string) => {
    setForm((prev) => ({ ...prev, [symptom]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const filtered = Object.fromEntries(
      Object.entries(form).filter(([_, v]) => v !== "")
    );
    if (Object.keys(filtered).length === 0) {
      setError("Please select at least one symptom");
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const res = await getDiagnosis(filtered);
      console.log("Diagnosis API response:", res.data);
      // Save results to localStorage
      localStorage.setItem("diagnosisResults", JSON.stringify(res.data));
      navigate("/result", { state: { result: res.data } });
    } catch (err: any) {
      console.error("Diagnosis error:", err);
      setError(err.response?.data?.error || "Failed to diagnose");
    } finally {
      setLoading(false);
    }
  };

  if (loading && !allSymptoms.length) {
    return <div className="text-center py-10">Loading symptoms...</div>;
  }

  if (error && !allSymptoms.length) {
    return <div className="text-center py-10 text-red-500">{error}</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4">
      <div className="max-w-md mx-auto bg-white p-6 rounded-2xl shadow">
        <h1 className="text-2xl font-bold text-center mb-6 flex items-center justify-center gap-2">
          <span role="img" aria-label="brain">🧠</span> Fuzzy Diagnosis
        </h1>
        {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}
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
            disabled={loading}
            className={`w-full rounded-full py-2 font-semibold text-white ${
              loading ? "bg-blue-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loading ? "Processing..." : "Complete Diagnosis"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default SurveyPage;