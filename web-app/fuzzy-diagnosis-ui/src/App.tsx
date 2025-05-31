import React, { useEffect, useState } from "react";
import type { ChangeEvent, FormEvent } from "react";
import { getSymptoms, getDiagnosis } from "./api";
import type { DiagnosisResult } from "./types";

const App: React.FC = () => {
  const [allSymptoms, setAllSymptoms] = useState<string[]>([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState<string[]>([]);
  const [form, setForm] = useState<Record<string, string>>({});
  const [results, setResults] = useState<DiagnosisResult | null>(null);
  const [search, setSearch] = useState("");
  const [showPopup, setShowPopup] = useState(false);

  useEffect(() => {
    getSymptoms().then((res) => setAllSymptoms(res.data));
  }, []);

  const handleAddSymptom = (symptom: string) => {
    if (!selectedSymptoms.includes(symptom)) {
      setSelectedSymptoms([...selectedSymptoms, symptom]);
      setForm((prev) => ({ ...prev, [symptom]: "" }));
    }
    setShowPopup(false);
    setSearch("");
  };

  const handleChange = (symptom: string, value: string) => {
    setForm((prev) => ({ ...prev, [symptom]: value }));
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const filledInputs: Record<string, string> = {};
    selectedSymptoms.forEach((s) => {
      if (form[s]) filledInputs[s] = form[s];
    });
    const res = await getDiagnosis(filledInputs);
    setResults(res.data);
  };

  const filteredSymptoms = allSymptoms.filter(
    (s) =>
      s.toLowerCase().includes(search.toLowerCase()) &&
      !selectedSymptoms.includes(s)
  );

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow p-6">
        <h1 className="text-3xl font-bold text-center text-blue-700 mb-6">
          🧠 Fuzzy Diagnosis
        </h1>

        <div className="flex justify-center mb-6">
          <button
            type="button"
            onClick={() => setShowPopup(true)}
            className="bg-emerald-600 hover:bg-emerald-700 transition text-white px-6 py-2 rounded-full text-sm font-semibold shadow"
          >
            ➕ Додати симптом
          </button>
        </div>

        {showPopup && (
          <div className="fixed inset-0 bg-black bg-opacity-40 flex justify-center items-start pt-32 z-50">
            <div className="bg-white rounded-xl w-full max-w-md p-6 shadow-lg relative">
              <button
                className="absolute top-2 right-3 text-gray-500 hover:text-red-500"
                onClick={() => setShowPopup(false)}
              >
                ✖
              </button>
              <input
                type="text"
                placeholder="🔍 Пошук симптома..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="border border-gray-300 p-2 rounded w-full mb-3"
              />
              <ul className="max-h-48 overflow-y-auto divide-y divide-gray-100">
                {filteredSymptoms.map((symptom) => (
                  <li
                    key={symptom}
                    className="py-2 px-3 hover:bg-blue-50 cursor-pointer"
                    onClick={() => handleAddSymptom(symptom)}
                  >
                    {symptom}
                  </li>
                ))}
                {filteredSymptoms.length === 0 && (
                  <li className="text-gray-400 px-3 py-2">Нічого не знайдено</li>
                )}
              </ul>
            </div>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-5">
          {selectedSymptoms.map((symptom) => (
            <div key={symptom}>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {symptom.charAt(0).toUpperCase() + symptom.slice(1)}
              </label>
              <select
                value={form[symptom] || ""}
                onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                  handleChange(symptom, e.target.value)
                }
                className="w-full border-gray-300 rounded-lg shadow-sm p-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
              >
                <option value="">Оберіть вираженість</option>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </select>
            </div>
          ))}
          {selectedSymptoms.length > 0 && (
            <div className="text-center">
              <button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700 transition text-white font-semibold px-6 py-2 rounded-full shadow"
              >
                🧾 Отримати діагноз
              </button>
            </div>
          )}
        </form>

        {results && (
          <div className="mt-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-3">
              🧬 Ймовірність захворювання:
            </h2>
            <ul className="space-y-2">
              {Object.entries(results).map(([disease, value]) => (
                <li key={disease} className="flex justify-between border-b pb-1">
                  <span className="capitalize text-gray-700 font-medium">{disease}</span>
                  <span className="text-blue-600 font-bold">{value.toFixed(2)}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;