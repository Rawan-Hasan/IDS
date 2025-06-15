import React, { useState } from "react";
import Login from "./Login";
import Predict from "./Predict";

function App() {
  const [token, setToken] = useState("");

  return (
    <div className="App">
      {token ? <Predict token={token} /> : <Login onLogin={setToken} />}
    </div>
  );
}

export default App;
