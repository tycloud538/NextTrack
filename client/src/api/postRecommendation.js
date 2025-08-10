import axios from "axios";

export const postRecommendation = ({ tracks, tags }) => {
  return axios
    .post("http://127.0.0.1:5000/tracks/recommendation", {
      track_history: tracks,
      tags: tags,
    })
    .then((response) => response.data)
    .catch((e) => console.error(e));
};
