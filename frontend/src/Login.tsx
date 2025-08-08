import axios from "axios";
import { useState } from "react";

export const Login = ({ onLogin }: { onLogin: (token: string) => void }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    const res = await axios.post("/api/login", { username, password });
    onLogin(res.data.access_token);
  };

  return (
    <div>
      <h2>Вход</h2>
      <input placeholder="Логин" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Пароль" onChange={e => setPassword(e.target.value)} />
      <button onClick={login}>Войти</button>
    </div>
  );
};
