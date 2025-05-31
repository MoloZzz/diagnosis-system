import axios from 'axios';

export const getSymptoms = () => axios.get<string[]>("http://localhost:5000/symptoms");
export const getDiagnosis = (data: Record<string, string>) => axios.post("http://localhost:5000/diagnose", data);
