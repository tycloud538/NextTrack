import { useState } from "react";

import { Button, Flex, Space } from "@mantine/core";
import { useMutation } from "@tanstack/react-query";

import { postRecommendation } from "../api/postRecommendation";

import { RecommendationDetails } from "./RecommendationDetails";

const Recommendation = () => {
  const [recommendation, setRecommendation] = useState(null);

  const mutation = useMutation({
    mutationFn: postRecommendation,
    onSuccess: (response) => {
      setRecommendation(response);
    },
  });

  return (
    <Flex align="center" direction="column">
      <Button
        color="indigo"
        radius="lg"
        variant="filled"
        size="lg"
        onClick={() => mutation.mutateAsync()}
      >
        Get Recommendation
      </Button>
      <Space h="xl" />
      <RecommendationDetails recommendation={recommendation} />
    </Flex>
  );
};

export default Recommendation;
