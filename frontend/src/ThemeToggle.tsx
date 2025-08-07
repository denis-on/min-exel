export const ThemeToggle = () => {
  const toggle = () => {
    const current = document.documentElement.getAttribute("data-theme");
    document.documentElement.setAttribute("data-theme", current === "dark" ? "light" : "dark");
  };
  return <button onClick={toggle}>🌗</button>;
};
