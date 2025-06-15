import axios from "axios";
import type { DiagnosisResult } from "./types";

const apiClient = axios.create({
  baseURL: "http://localhost:5000",
  headers: { "Content-Type": "application/json" },
});

export const getSymptoms = () => apiClient.get<string[]>("/symptoms");
export const getDiagnosis = (data: Record<string, string>) =>
  apiClient.post<DiagnosisResult>("/diagnose", data);
