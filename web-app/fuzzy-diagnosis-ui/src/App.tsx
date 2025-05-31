import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AuthPage from "./pages/AuthPage";
import SurveyPage from "./pages/SurveyPage";
import ResultPage from "./pages/ResultPage";
import type { DiagnosisResult } from "./types";

const mockResult: DiagnosisResult = {
  flu: 72,
  covid: 56,
  allergy: 20,
};

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthPage />} />
        <Route path="/survey" element={<SurveyPage />} />
        <Route path="/result" element={<ResultPage result={mockResult} />} />
      </Routes>
    </Router>
  );
};

export default App;