import React, { useEffect, useState } from "react";
import type { ChangeEvent, FormEvent } from "react";
import axios from "axios";

interface DiagnosisResult {
  [disease: string]: number;
}

const App: React.FC = () => {
  const [symptoms, setSymptoms] = useState<string[]>([]);
  const [form, setForm] = useState<Record<string, string>>({});
  const [results, setResults] = useState<DiagnosisResult | null>(null);

  useEffect(() => {
    axios.get("http://localhost:5000/symptoms").then((res) => {
      setSymptoms(res.data);
    });
  }, []);

  const handleChange = (symptom: string, value: string) => {
    setForm((prev) => ({ ...prev, [symptom]: value }));
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const res = await axios.post("http://localhost:5000/diagnose", form);
    setResults(res.data);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Fuzzy Diagnosis</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        {symptoms.map((symptom) => (
          <div key={symptom}>
            <label className="block mb-1 font-medium">{symptom}</label>
            <select
              value={form[symptom] || ""}
              onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                handleChange(symptom, e.target.value)
              }
              className="border px-3 py-1 rounded w-full"
            >
              <option value="">Select...</option>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>
        ))}
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Get Diagnosis
        </button>
      </form>

      {results && (
        <div className="mt-6">
          <h2 className="text-xl font-semibold mb-2">Diagnosis Results:</h2>
          <ul>
            {Object.entries(results).map(([disease, value]) => (
              <li key={disease}>
                <strong>{disease}</strong>: {value.toFixed(2)}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default App;
