import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom"
import Layout from "./components/layout/Layout"
import Cadastro from "./pages/cadastro/index"
import Login from "./pages/login/index"
// import Jaguar from "./pages/jaguar"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/cadastro" element={<Cadastro />} />
          <Route path="/login" element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
