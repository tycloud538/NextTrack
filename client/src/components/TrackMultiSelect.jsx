import AsyncSelect from "react-select/async";

import { getTracks } from "../api";

const selectStyles = {
  control: (provided) => ({
    ...provided,
    width: "300px",
    borderRadius: "0.75rem",
  }),
  multiValueRemove: (provided) => ({
    ...provided,
    ":hover": {
      backgroundColor: "hsl(0 0 80)",
      color: undefined,
    },
  }),
};

export const TrackMultiSelect = ({ onChange }) => {
  const getTrackOptions = async (search) => {
    const { tracks } = await getTracks(search);

    return tracks.map((track) => {
      const label = track.artist
        ? `${track.name} - ${track.artist.name}`
        : `${track.name}`;

      return {
        value: track.id,
        label,
      };
    });
  };

  const handleChange = (selectedOptions) => {
    onChange(selectedOptions.map((option) => option.value));
  };

  return (
    <AsyncSelect
      styles={selectStyles}
      isMulti
      cacheOptions
      defaultOptions
      loadOptions={getTrackOptions}
      onChange={handleChange}
      placeholder="Select songs that you listen to.."
    />
  );
};
