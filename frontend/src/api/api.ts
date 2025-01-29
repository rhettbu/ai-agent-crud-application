import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const createAgent = async (name: string, description: string) => {
    return await axios.post(`${API_URL}/agents/`, { name, description });
};

export const getAgent = async (name: string) => {
    return await axios.get(`${API_URL}/agents/${name}`);
};

export const updateAgent = async (name: string, description: string) => {
    return await axios.put(`${API_URL}/agents/${name}`, { name, description });
};

export const deleteAgent = async (name: string) => {
    return await axios.delete(`${API_URL}/agents/${name}`);
};
