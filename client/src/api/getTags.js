import axios from "axios";

export const getTags = (search = "") => {
  const params = new URLSearchParams([["search", search]]);
  return axios
    .get("http://127.0.0.1:5000/tags", { params })
    .then((response) => response.data)
    .catch((e) => console.error(e));
};
