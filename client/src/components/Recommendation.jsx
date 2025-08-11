import { useState } from "react";

import { Button, Flex, Space } from "@mantine/core";
import { useMutation } from "@tanstack/react-query";

import { postRecommendations } from "../api";

import { RecommendationDetails } from "./RecommendationDetails";
import { TagMultiSelect } from "./TagMultiSelect";
import { TrackMultiSelect } from "./TrackMultiSelect";

export const Recommendation = () => {
  const [selectedTags, setSelectedTags] = useState([12, 34]);
  const [selectedTracks, setSelectedTracks] = useState([56, 78]);
  const [recommendation, setRecommendation] = useState(null);

  const mutation = useMutation({
    mutationFn: postRecommendations,
    onSuccess: (response) => {
      setRecommendation(response);
    },
  });

  const handleGetRecommendation = () => {
    mutation.mutate({
      tracks: selectedTracks,
      tags: selectedTags,
    });
  };

  return (
    <Flex align="center" direction="column">
      <Flex w="700" justify="space-between" align="center" direction="row">
        <TrackMultiSelect onChange={setSelectedTracks} />
        <Space w="xl" />
        <TagMultiSelect onChange={setSelectedTags} />
      </Flex>
      <Space h="xl" />
      <Space h="xl" />
      <Space h="xl" />
      <Flex align="center" direction="column">
        <Button
          color="indigo"
          radius="lg"
          variant="filled"
          size="lg"
          onClick={handleGetRecommendation}
        >
          Get Recommendation
        </Button>
        <Space h="xl" />
        <RecommendationDetails recommendation={recommendation} />
      </Flex>
    </Flex>
  );
};
