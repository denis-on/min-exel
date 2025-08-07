import { useState, useEffect } from "react";
import { Login } from "./Login";
import { TableView } from "./TableView";
import { SheetTabs } from "./SheetTabs";
import { ThemeToggle } from "./ThemeToggle";
import axios from "axios";

function App() {
  const [token, setToken] = useState("");
  const [sheetId, setSheetId] = useState<number | null>(null);
  const [sheets, setSheets] = useState([]);

  useEffect(() => {
    if (token) {
      axios.get("/api/sheets", { headers: { Authorization: `Bearer ${token}` } })
        .then(res => setSheets(res.data));
    }
  }, [token]);

  if (!token) return <Login onLogin={setToken} />;

  return (
    <div>
      <ThemeToggle />
      <SheetTabs sheets={sheets} onSelect={setSheetId} />
      {sheetId && <TableView sheetId={sheetId} token={token} />}
    </div>
  );
}

export default App;
