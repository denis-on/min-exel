import { useState, useEffect } from "react";
import axios from "axios";

export const TableView = ({ sheetId, token }: { sheetId: number; token: string }) => {
  const [rows, setRows] = useState([]);
  const [columns, setColumns] = useState([]);
  const [editing, setEditing] = useState<{ [key: number]: any }>({});

  useEffect(() => {
    axios.get(`/api/sheets/${sheetId}/columns`, { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setColumns(res.data));
    axios.get(`/api/sheets/${sheetId}/rows`, { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setRows(res.data));
  }, [sheetId]);

  const saveRow = async (row: any) => {
    try {
      await axios.put(`/api/rows/${row.id}`, {
        data: editing[row.id],
        version: row.version
      }, { headers: { Authorization: `Bearer ${token}` } });
    } catch (err: any) {
      if (err.response?.status === 409) {
        alert("Конфликт! Строка уже изменена.");
      }
    }
  };

  return (
    <table>
      <thead>
        <tr>{columns.map((col: any) => <th key={col.id}>{col.name}</th>)}</tr>
      </thead>
      <tbody>
        {rows.map((row: any) => (
          <tr key={row.id}>
            {columns.map((col: any) => (
              <td key={col.id}>
                <input
                  value={editing[row.id]?.[col.name] ?? row.data[col.name] ?? ""}
                  onChange={e => setEditing(prev => ({
                    ...prev,
                    [row.id]: { ...prev[row.id], [col.name]: e.target.value }
                  }))}
                />
              </td>
            ))}
            <td><button onClick={() => saveRow(row)}>💾</button></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
