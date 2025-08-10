import { Anchor, Flex, Space, Text } from "@mantine/core";

const Placeholder = ({ size = "md" }) => <Text size={size}>{"\u200e"}</Text>;

export const RecommendationDetails = ({ recommendation }) => {
  if (!recommendation) {
    return (
      <>
        <Placeholder size="lg" />
        <Space h="md" />
        <Placeholder />
        <Space h="md" />
        <Placeholder />
        <Space h="md" />
        <Placeholder />
      </>
    );
  }

  const tagText =
    recommendation.tags.length > 0 ? (
      <Text size="md">Tags: {recommendation.tags.slice(0, 5).join(", ")}</Text>
    ) : (
      <Placeholder />
    );

  const urlText =
    recommendation.urls.length > 0 ? (
      <Text size="md">
        {"Links: "}
        {recommendation.urls.slice(0, 5).map((url) => {
          return (
            <>
              <Anchor href={url} target="_blank" rel="noreferrer noopener">
                {new URL(url).hostname}
              </Anchor>
              {"  "}
            </>
          );
        })}
      </Text>
    ) : (
      <Placeholder />
    );

  return (
    <Flex align="center" direction="column">
      <Text size="lg" fw="bolder">
        Your next track is: {recommendation.name} - {recommendation.artist.name}
      </Text>
      <Space h="md" />
      <Text size="md">Rating: {recommendation.rating}</Text>
      <Space h="md" />
      {tagText}
      <Space h="md" />
      {urlText}
    </Flex>
  );
};
