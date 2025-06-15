import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const AuthPage: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please fill in all fields");
      return;
    }
    // TODO: Додати запит до API для авторизації, якщо потрібно
    navigate("/survey");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-2xl shadow w-full max-w-sm">
        <h1 className="text-2xl font-bold text-center mb-6 flex items-center justify-center gap-2">
          <span role="img" aria-label="brain">🧠</span> Fuzzy Diagnosis
        </h1>
        {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}
        <form className="space-y-4" onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <div className="text-sm text-right text-blue-500 cursor-pointer hover:underline">
            Forgot password?
          </div>
          <button
            type="submit"
            className="w-full bg-blue-600 text-white rounded-full py-2 font-semibold hover:bg-blue-700"
          >
            Sign up or sign in
          </button>
        </form>
      </div>
    </div>
  );
};

export default AuthPage;