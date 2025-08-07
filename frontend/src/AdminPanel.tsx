import { useEffect, useState } from "react";
import axios from "axios";
import { User, Sheet } from './types';

export const AdminPanel = ({ token }: { token: string }) => {
  const [users, setUsers] = useState<User[]>([]);
  const [sheets, setSheets] = useState<Sheet[]>([]);

  useEffect(() => {
    axios.get("/api/users", { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setUsers(res.data));
    axios.get("/api/sheets", { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setSheets(res.data));
  }, [token]);

  return (
    <div>
      <h3>Пользователи</h3>
      <ul>{users.map(u => <li key={u.id}>{u.username} ({u.role})</li>)}</ul>
      <h3>Листы</h3>
      <ul>{sheets.map(s => <li key={s.id}>{s.name}</li>)}</ul>
    </div>
  );
};
