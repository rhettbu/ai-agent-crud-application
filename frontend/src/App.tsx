import React, { useState } from "react";
import { createAgent, getAgent, updateAgent, deleteAgent } from "./api/api";

const App: React.FC = () => {
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [response, setResponse] = useState("");

    const handleCreate = async () => {
        await createAgent(name, description);
        setResponse(`Agent ${name} created!`);
    };

    const handleGet = async () => {
        const res = await getAgent(name);
        setResponse(res.data.description);
    };

    const handleUpdate = async () => {
        await updateAgent(name, description);
        setResponse(`Agent ${name} updated!`);
    };

    const handleDelete = async () => {
        await deleteAgent(name);
        setResponse(`Agent ${name} deleted!`);
    };

    return (
        <div>
            <h1>AI Agent CRUD</h1>
            <input type="text" placeholder="Agent Name" value={name} onChange={(e) => setName(e.target.value)} />
            <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
            <button onClick={handleCreate}>Create</button>
            <button onClick={handleGet}>Read</button>
            <button onClick={handleUpdate}>Update</button>
            <button onClick={handleDelete}>Delete</button>
            <p>{response}</p>
        </div>
    );
};

export default App;
