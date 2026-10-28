import "./globals.css";

export const metadata = { title: "KRS" };

export default function RootLayout({ children }) {
  return (
    <html lang="id">
      <body>{children}</body>
    </html>
  );
}
