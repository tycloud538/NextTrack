import { MantineProvider, Container } from "@mantine/core";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

import "@mantine/core/styles.css";

import Recommendation from "./components/Recommendation";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider>
        <Container fluid>
          <Recommendation />
        </Container>
      </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;
