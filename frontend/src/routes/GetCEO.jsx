import { useLoaderData, Link } from "react-router-dom";

export async function loader() {
  const url = "http://localhost:8000/ceos";
  const data = await fetch(url).then((response) => response.json());

  return { data };
}

const Ceos = () => {
  return;
};

export default Ceos;
