import axios from "axios";

export const postRecommendation = (
  params = {
    surprise_me: true,
    listening_history: [123, 345, 567, 789],
    favourite_genres: ["pop", "rock", "alternative"],
  }
) => {
  return axios
    .post("http://127.0.0.1:5000/track/recommendation", params)
    .then((response) => response.data)
    .catch((e) => console.error(e));
};
