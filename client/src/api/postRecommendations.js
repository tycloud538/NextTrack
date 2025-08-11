import axios from "axios";

export const postRecommendations = ({ tracks, tags }) => {
  return axios
    .post("http://127.0.0.1:5000/tracks/recommendations", {
      track_history: tracks,
      tags: tags,
    })
    .then((response) => response.data)
    .catch((e) => console.error(e));
};
