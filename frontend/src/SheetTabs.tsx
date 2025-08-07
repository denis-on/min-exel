export const SheetTabs = ({ sheets, onSelect }: { sheets: any[]; onSelect: (id: number) => void }) => (
  <div>
    {sheets.map(sheet => (
      <button key={sheet.id} onClick={() => onSelect(sheet.id)}>
        {sheet.name}
      </button>
    ))}
  </div>
);
