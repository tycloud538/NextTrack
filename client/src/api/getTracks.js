import axios from "axios";

export const getTracks = (search = "") => {
  const params = new URLSearchParams([["search", search]]);
  return axios
    .get("http://127.0.0.1:5000/tracks", { params })
    .then((response) => response.data)
    .catch((e) => console.error(e));
};
