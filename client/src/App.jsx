import { MantineProvider, Container, Title } from "@mantine/core";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import "@mantine/core/styles.css";

import { Recommendation } from "./components/Recommendation";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider>
        <Container fluid>
          <Title align="center" mb={96} size={28}>
            NextTrack: Your Music Recommendation App
          </Title>
          <Recommendation />
        </Container>
      </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;
