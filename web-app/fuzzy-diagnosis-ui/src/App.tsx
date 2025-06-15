import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AuthPage from "./pages/AuthPage";
import SurveyPage from "./pages/SurveyPage";
import ResultPage from "./pages/ResultPage";
import Header from "./pages/Header";

const App: React.FC = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<AuthPage />} />
        <Route path="/survey" element={<SurveyPage />} />
        <Route path="/result" element={<ResultPage />} />
      </Routes>
    </Router>
  );
};

export default App;