import { Button, Center } from "@mantine/core";
import { useMutation } from "@tanstack/react-query";

import { postRecommendation } from "../api/postRecommendation";

const Recommendation = () => {
  const mutation = useMutation({
    mutationFn: postRecommendation,
    onSuccess: (response) => {
      console.log("TCL ~ Recommendation ~ response:", response);
    },
  });

  return (
    <Center>
      <Button
        color="indigo"
        variant="filled"
        size="lg"
        onClick={() => mutation.mutateAsync()}
      >
        Get Recommendation
      </Button>
    </Center>
  );
};

export default Recommendation;
