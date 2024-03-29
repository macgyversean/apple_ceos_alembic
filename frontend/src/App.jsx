import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./routes/Home";
import Ceos, { loader as ceoLoader } from "./routes/GetCEO";
import ErrorPage from "./pages/ErrorPage";
// import SingleCeo, { loader as SingleCeoLoader } from "./routes/SingleCeo";
// import AddCeo, { action as addCeoAction } from "./routes/AddCeo";

const router = createBrowserRouter([
  {
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/ceos",
        element: <Ceos />,
        loader: ceoLoader,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
