import React, { useState } from "react";
import { predict } from "./api";

export default function Predict({ token }) {
  const [features, setFeatures] = useState({
    proto: "tcp", service: "http", state: "FIN", dur: 0.5, sbytes: 1000, dbytes: 500
  });
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await predict(features, token);
      setResult(res.data.prediction === 1 ? "⚠️ Attack" : "✅ Normal");
    } catch (err) {
      setResult("Prediction failed!");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        {Object.keys(features).map(key => (
          <input
            key={key}
            placeholder={key}
            value={features[key]}
            onChange={e => setFeatures({ ...features, [key]: e.target.value })}
          />
        ))}
        <button type="submit">Predict</button>
      </form>
      <div>Result: {result}</div>
    </div>
  );
}
